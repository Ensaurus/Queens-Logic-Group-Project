from functools import total_ordering
from os import umask
from nnf import Var
from lib204 import Encoding

from nnf import true

import varSetup.py


#For using iff(F1,F2), >> for implication and ~ for negation.
from nnf import NNF
from nnf.operators import iff

def implication(l, r):
    return l.negate() | r

def neg(f):
    return f.negate()

NNF.__rshift__ = implication
NNF.__invert__ = neg

#values that are common for all stores
class setup(object):
    def __init__(self, season, INshirts, INswim, INpants, INjackets, INboots):
        self.season = season
        self.INshirts = INshirts
        self.INswim = INswim
        self.INpants = INpants
        self.INjackets = INjackets
        self.INboots = INboots

    

#values that are specific to each store
class store(object):
    def __init__(self, population, urban, region, bestSeller):
        self.population = population
        self.urban = urban
        self.region = region
        self.bestSeller = bestSeller

    def __hash__(self):
        return hash("(%d) %s %s %s" % (self.population, self.urban, self.region, self.bestSeller))


#setup general values
#Season = summer, spring, autumn, winter
#inventory = 0, 20, 40, 60, 80, 100
#only works for inventory 100, season summer
generalConditions = setup('summer', 100, 100, 100, 100, 100)

#Only 1 season is true at a time
#For inventory, if a number (say 100) is true, then all lower values (80, 60, 40, 20, 0) would be true as well

#Setup the variables
varSetup.variableSetup()

#Exclusive OR functions
def exclusiveOr2(a, b):
    return (a & ~b) | (~a & b)

def exclusiveOr3(a, b, c):
    return (a & ~b & ~c) | (~a & b & ~c) | (~a & ~b & c)

def exclusiveOr4(a, b, c, d):
    return (a & ~b & ~c & ~d) | (~a & b & ~c & ~d) | (~a & ~b & c & ~d) | (~a & ~b & ~c & d)

def exclusiveOr5(a, b, c, d, e):
    return (a & ~b & ~c & ~d & ~e) | (~a & b & ~c & ~d & ~e) | (~a & ~b & c & ~d & ~e) | (~a & ~b & ~c & d & ~e) | (~a & ~b & ~c & ~d & e)


def invert(thing):
    return ~thing

def example_theory():
    E = Encoding()

    #general setup
    generalConditions = setup('spring', 100, 100, 100, 100, 100)

    #stores setup (5 stores)
    storeOb = []
    storeOb.append(store('500k', 'urban', 'central', 'swimwear'))
    storeOb.append(store('20k', 'rural', 'atlantic', 'shirts'))
    storeOb.append(store('100k', 'urban', 'atlantic', 'swimwear'))
    storeOb.append(store('100k', 'urban', 'central', 'shirts'))
    storeOb.append(store('0k', 'rural', 'territory', 'shirts'))

    if(generalConditions.season == 'summer'):
        E.add_constraint(S_summer)
    elif(generalConditions.season == 'winter'):
        E.add_constraint(S_winter)
    elif(generalConditions.season == 'spring'):
        E.add_constraint(S_spring)
    elif(generalConditions.season == 'autumn'):
        E.add_constraint(S_autumn)

    for i in range(5):
        #if(storeOb[i].region == 'central'):
        #    E.add_constraint(regionCentral[i])
        #if(storeOb[i].region == 'atlantic'):
        #    E.add_constraint(regionAtlantic[i])
        #if(storeOb[i].region == 'territory'):
        #    E.add_constraint(regionTerritory[i])        
        '''
        if(storeOb[i].population == '500k'):
            E.add_constraint(population500[i])
        elif(storeOb[i].population == '100k'):
            E.add_constraint(population100[i])    
        elif(storeOb[i].population == '50k'):
            E.add_constraint(population50[i])    
        elif(storeOb[i].population == '20k'):
            E.add_constraint(population20[i])    
        elif(storeOb[i].population == '0k'):
            E.add_constraint(population0[i])    
        '''




    for i in range(5):

        #only one population
        E.add_constraint(exclusiveOr5(population500[i], population100[i], population50[i], population20[i], population0[i]))

        #only one region
        E.add_constraint(exclusiveOr3(regionAtlantic[i], regionCentral[i], regionTerritory[i]))

        #Don't Need this
        #only urban or rural
        #E.add_constraint(urbanVal[i] | ~urbanVal[i])

        #only one season
        E.add_constraint(exclusiveOr4(S_autumn, S_spring, S_summer, S_winter))

        #Only one size pack of items
        E.add_constraint(exclusiveOr3(shirtsS[i], shirtsM[i], shirtsL[i]))#always selling
        E.add_constraint(exclusiveOr4(swimN[i], swimS[i], swimM[i], swimL[i]))
        E.add_constraint(exclusiveOr3(pantsS[i], pantsM[i], pantsL[i]))#always selling
        E.add_constraint(exclusiveOr4(jacketsN[i], jacketsS[i], jacketsM[i], jacketsL[i]))
        E.add_constraint(exclusiveOr3(bootsS[i], bootsM[i], bootsL[i]))#always selling

        #Atlantic region seasonal shipments
        E.add_constraint((regionAtlantic[i] & S_spring).negate() | (shirtsL[i] & swimL[i] & pantsL[i] & jacketsL[i] & bootsL[i]))
        E.add_constraint((regionAtlantic[i] & S_summer).negate() | (shirtsL[i] & swimL[i] & pantsM[i] & jacketsS[i] & bootsM[i]))
        E.add_constraint((regionAtlantic[i] & S_autumn).negate() | (shirtsL[i] & swimM[i] & pantsL[i] & jacketsL[i] & bootsL[i]))
        E.add_constraint((regionAtlantic[i] & S_winter).negate() | (shirtsL[i] & swimS[i] & pantsL[i] & jacketsL[i] & bootsL[i]))

        #Central region seasonal shipments
        E.add_constraint((regionCentral[i] & S_spring).negate() | (shirtsL[i] & swimL[i] & pantsL[i] & jacketsS[i] & bootsS[i]))
        E.add_constraint((regionCentral[i] & S_summer).negate() | (shirtsL[i] & swimL[i] & pantsM[i] & jacketsS[i] & bootsS[i]))
        E.add_constraint((regionCentral[i] & S_autumn).negate() | (shirtsL[i] & swimM[i] & pantsL[i] & jacketsL[i] & bootsL[i]))
        E.add_constraint((regionCentral[i] & S_winter).negate() | (shirtsL[i] & swimS[i] & pantsL[i] & jacketsL[i] & bootsL[i]))

        #Territories seasonal shipments
##        E.add_constraint((regionTerritory[i] & S_spring).negate() | (shirtsL[i] & swimN[i] & pantsL[i] & jacketsL[i] & bootsL[i]))
        #this gives an error, help wanted
        E.add_constraint((regionTerritory[i] & S_summer).negate() | (shirtsL[i] & swimS[i] & pantsL[i] & jacketsL[i] & bootsM[i]))
        E.add_constraint((regionTerritory[i] & S_autumn).negate() | (shirtsL[i] & swimN[i] & pantsL[i] & jacketsL[i] & bootsL[i]))
        E.add_constraint((regionTerritory[i] & S_winter).negate() | (shirtsL[i] & swimN[i] & pantsL[i] & jacketsL[i] & bootsL[i]))

        #population >100k
        E.add_constraint((population100[i] | population500[i]).negate() | (~shirtsS[i] & ~swimS[i] & ~pantsS[i] & ~jacketsS[i] & ~bootsS[i]))
        
        #population <20k range
        E.add_constraint((population0[i] | population20[i]).negate() | (~shirtsL[i] & ~swimL[i] & ~pantsL[i] & ~jacketsL[i] & ~bootsL[i]))
        
        #E.add_constraint()

        #bestseller shirts (small populations (<50k) get a medium shipment if shirts are the most popular item)
        E.add_constraint((bestsellerShirts[i] & (population0[i] | population20[i])).negate() | shirtsM[i])
        #large shipment shirts (large populations get a large shipment if shirts are the most popular item)
        E.add_constraint((bestsellerShirts[i] & (~population0[i] & ~population20[i])).negate() | shirtsL[i])

        #bestseller swimwear
        E.add_constraint((bestsellerSwimwear[i] & (population0[i] | population20[i])).negate() | swimM[i])
        #large shipments swimwear
        E.add_constraint((bestsellerSwimwear[i] & (~population0[i] & ~population20[i])).negate() | swimL[i])

    return E


if __name__ == "__main__":

    T = example_theory()


 
    print("\nSatisfiable: %s" % T.is_satisfiable())
    print("# Solutions: %d" % T.count_solutions())
    print("   Solution: %s" % T.solve())

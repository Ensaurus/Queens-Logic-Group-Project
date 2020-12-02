 from functools import total_ordering
from os import umask
from nnf import Var
from lib204 import Encoding

from nnf import true

import varSetup


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

#Only 1 season is true at a time
#For inventory, if a number (say 100) is true, then all lower values (80, 60, 40, 20, 0) would be true as well

S_summer = Var('S_summer')
S_spring = Var('S_spring')
S_winter = Var('S_winter')
S_autumn = Var('S_autumn')

population500 = {}
population100 = {}
population50 = {}
population20 = {}
population0 = {}
urbanVal = {}
regionAtlantic = {}
regionCentral = {}
regionTerritory = {}
#regionPraries = {}													#remove comments to include praries/pacific
#regionPacific = {}
bestsellerShirts = {}
bestsellerSwimwear = {}
for i in range(5):
    print(i)
    population500[i] = Var("population500_" + str(i))
    population100[i] = Var("population100_" + str(i))
    population50[i] = Var("population50_" + str(i))
    population20[i] = Var("population20_" + str(i))
    population0[i] = Var("population0_" + str(i))
    urbanVal[i] = Var("urbanVal_" + str(i))
    regionAtlantic[i] = Var("regionAtlantic_" + str(i))
    regionCentral[i] = Var("regionCentral_" + str(i))
    regionTerritory[i] = Var("regionTerritory_" + str(i))
	#regionPraries[i] = Var("regionPraries_" + str(i))				#remove comments to include praries/pacific
    #regionPacific[i] = Var("regionPacific_" + str(i))
    bestsellerShirts[i] = Var("bestsellerShirts_" + str(i))
    bestsellerSwimwear[i] = Var("bestsellerSwimwear_" + str(i))


#shipment sizes, array because its for 5 stores (0-4)
shirtsN = {}
shirtsS = {}
shirtsM = {}
shirtsL = {}
for i in range(5):
    shirtsN[i] = Var("shirtsN_" + str(i))
    shirtsS[i] = Var("shirtsS_" + str(i))
    shirtsM[i] = Var("shirtsM_" + str(i))
    shirtsL[i] = Var("shirtsL_" + str(i))

swimN = {}
swimS = {}
swimM = {}
swimL = {}
for i in range(5):
    swimN[i] = Var("swimN_" + str(i))
    swimS[i] = Var("swimS_" + str(i))
    swimM[i] = Var("swimM_" + str(i))
    swimL[i] = Var("swimL_" + str(i))
    
pantsN = {}
pantsS = {}
pantsM = {}
pantsL = {}
for i in range(5):
    pantsN[i] = Var("pantsN_" + str(i))
    pantsS[i] = Var("pantsS_" + str(i))
    pantsM[i] = Var("pantsM_" + str(i))
    pantsL[i] = Var("pantsL_" + str(i))

jacketsN = {}
jacketsS = {}
jacketsM = {}
jacketsL = {}
for i in range(5):
    jacketsN[i] = Var("jacketsN_" + str(i))
    jacketsS[i] = Var("jacketsS_" + str(i))
    jacketsM[i] = Var("jacketsM_" + str(i))
    jacketsL[i] = Var("jacketsL_" + str(i))

bootsN = {}
bootsS = {}
bootsM = {}
bootsL = {}
for i in range(5):
    bootsN[i] = Var("bootsN_" + str(i))
    bootsS[i] = Var("bootsS_" + str(i))
    bootsM[i] = Var("bootsM_" + str(i))
    bootsL[i] = Var("bootsL_" + str(i))



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
	#Season = summer, spring, autumn, winter
	#inventory = 0, 20, 40, 60, 80, 100
    generalConditions = setup('winter', 100, 100, 100, 100, 100)

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
        #Set urban/rural for the specific store
        if(storeOb[i].urban == 'urban'):
            E.add_constraint(urbanVal[i])
        elif(storeOb[i].urban == 'rural'):
            E.add_constraint(~urbanVal[i])
        
        #Set region for each store
        if(storeOb[i].region == 'central'):
            E.add_constraint(regionCentral[i])
        if(storeOb[i].region == 'atlantic'):
            E.add_constraint(regionAtlantic[i])
        if(storeOb[i].region == 'territory'):
            E.add_constraint(regionTerritory[i])
		#if(storeOb[i].region == 'praries'):						#remove comments to include praries/pacific
        #    E.add_constraint(regionPraries[i])
        #if(storeOb[i].region == 'pacific'):
        #    E.add_constraint(regionPacific[i])
        
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
        
		#Considerations:
		#narrowing down regions to 3, or include last ones
		#include or exclude XS and XL sizes
		#possibly use table to narrow options down to 2, then size determines which of the 2 so sizes don't contradict table

    for i in range(5):

		#E.add_constraint()

        #only one population
        E.add_constraint(exclusiveOr5(population500[i], population100[i], population50[i], population20[i], population0[i]))
        
        #only one region
        E.add_constraint(exclusiveOr3(regionAtlantic[i], regionCentral[i], regionTerritory[i]))

        #Don't Need this
        #only urban or rural
        E.add_constraint(urbanVal[i] | ~urbanVal[i])

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
        E.add_constraint((regionTerritory[i] & S_spring).negate() | (shirtsL[i] & swimN[i] & pantsL[i] & jacketsL[i] & bootsL[i]))
        E.add_constraint((regionTerritory[i] & S_summer).negate() | (shirtsL[i] & swimS[i] & pantsL[i] & jacketsL[i] & bootsM[i]))
        E.add_constraint((regionTerritory[i] & S_autumn).negate() | (shirtsL[i] & swimN[i] & pantsL[i] & jacketsL[i] & bootsL[i]))
        E.add_constraint((regionTerritory[i] & S_winter).negate() | (shirtsL[i] & swimN[i] & pantsL[i] & jacketsL[i] & bootsL[i]))

		#Praries seasonal shipments
		#E.add_constraint((regionPraries[i] & S_spring).negate() | (shirtsL[i] & swimM[i] & pantsL[i] & jacketsM[i] & bootsM[i]))
        #E.add_constraint((regionPraries[i] & S_summer).negate() | (shirtsL[i] & swimL[i] & pantsM[i] & jacketsS[i] & bootsM[i]))
        #E.add_constraint((regionPraries[i] & S_autumn).negate() | (shirtsL[i] & swimS[i] & pantsL[i] & jacketsL[i] & bootsL[i]))
        #E.add_constraint((regionPraries[i] & S_winter).negate() | (shirtsL[i] & swimS[i] & pantsL[i] & jacketsL[i] & bootsL[i]))

		#Pacific seasonal shipments
		#E.add_constraint((regionPacific[i] & S_spring).negate() | (shirtsL[i] & swimM[i] & pantsL[i] & jacketsS[i] & bootsL[i]))
        #E.add_constraint((regionPacific[i] & S_summer).negate() | (shirtsL[i] & swimL[i] & pantsM[i] & jacketsN[i] & bootsL[i]))
        #E.add_constraint((regionPacific[i] & S_autumn).negate() | (shirtsL[i] & swimM[i] & pantsL[i] & jacketsS[i] & bootsL[i]))
        #E.add_constraint((regionPacific[i] & S_winter).negate() | (shirtsL[i] & swimS[i] & pantsL[i] & jacketsL[i] & bootsL[i]))



		##BOTH OF THE FOLLOWING BREAK THE CODE, currently 'hardcoded' using the table which contradicts these
        #population >100k
        #E.add_constraint((population100[i] | population500[i]).negate() | (~shirtsS[i] & ~swimS[i] & ~pantsS[i] & ~jacketsS[i] & ~bootsS[i]))
        #population <20k range
        #E.add_constraint((population0[i] | population20[i]).negate() | (~shirtsL[i] & ~swimL[i] & ~pantsL[i] & ~jacketsL[i] & ~bootsL[i]))
        
		#Bestsellers not yet implemented
        #bestseller shirts (small populations (<50k) get a medium shipment if shirts are the most popular item)
        #E.add_constraint((bestsellerShirts[i] & (population0[i] | population20[i])).negate() | shirtsM[i])
        #large shipment shirts (large populations get a large shipment if shirts are the most popular item)
        #E.add_constraint((bestsellerShirts[i] & (~population0[i] & ~population20[i])).negate() | shirtsL[i])

        #bestseller swimwear
        #E.add_constraint((bestsellerSwimwear[i] & (population0[i] | population20[i])).negate() | swimM[i])
        #large shipments swimwear
        #E.add_constraint((bestsellerSwimwear[i] & (~population0[i] & ~population20[i])).negate() | swimL[i])

    return E


if __name__ == "__main__":

    T = example_theory()


 
    print("\nSatisfiable: %s" % T.is_satisfiable())
    print("# Solutions: %d" % T.count_solutions())
    print("   Solution: %s" % T.solve())

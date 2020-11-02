from functools import total_ordering
from os import umask
from nnf import Var
from lib204 import Encoding

from nnf import true

"""
000
001
010
011 <- pre
100 <- post
101
110
111
"""
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
bestsellerShirts = {}
bestsellerSwimwear = {}
for i in range(5):
    population500[i] = Var("population500%d", i)
    population100[i] = Var("population100%d", i)
    population50[i] = Var("population50%d", i)
    population20[i] = Var("population20%d", i)
    population0[i] = Var("population0%d", i)
    urbanVal[i] = Var("urbanVal%d", i)
    regionAtlantic[i] = Var("regionAtlantic%d", i)
    regionCentral[i] = Var("regionCentral%d", i)
    regionTerritory[i] = Var("regionTerritory%d", i)
    bestsellerShirts[i] = Var("bestsellerShirts%d", i)
    bestsellerSwimwear[i] = Var("bestsellerSwimwear%d", i)


#shipment sizes, array because its for 5 stores (0-4)
shirtsN = {}
shirtsS = {}
shirtsM = {}
shirtsL = {}
for i in range(5):
    shirtsN[i] = Var("shirtsN%d", i)
    shirtsS[i] = Var("shirtsS%d", i)
    shirtsM[i] = Var("shirtsM%d", i)
    shirtsL[i] = Var("shirtsL%d", i)

swimN = {}
swimS = {}
swimM = {}
swimL = {}
for i in range(5):
    swimN[i] = Var("swimN%d", i)
    swimS[i] = Var("swimS%d", i)
    swimM[i] = Var("swimM%d", i)
    swimL[i] = Var("swimL%d", i)
    
pantsN = {}
pantsS = {}
pantsM = {}
pantsL = {}
for i in range(5):
    pantsN[i] = Var("pantsN%d", i)
    pantsS[i] = Var("pantsS%d", i)
    pantsM[i] = Var("pantsM%d", i)
    pantsL[i] = Var("pantsL%d", i)

jacketsN = {}
jacketsS = {}
jacketsM = {}
jacketsL = {}
for i in range(5):
    jacketsN[i] = Var("jacketsN%d", i)
    jacketsS[i] = Var("jacketsS%d", i)
    jacketsM[i] = Var("jacketsM%d", i)
    jacketsL[i] = Var("jacketsL%d", i)

bootsN = {}
bootsS = {}
bootsM = {}
bootsL = {}
for i in range(5):
    bootsN[i] = Var("bootsN%d", i)
    bootsS[i] = Var("bootsS%d", i)
    bootsM[i] = Var("bootsM%d", i)
    bootsL[i] = Var("bootsL%d", i)

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
        E.add_constraint(population500[i] | population100[i] | population50[i] | population20[i] | population0[i])

        #only one region
        E.add_constraint(regionAtlantic[i] | regionCentral[i] | regionTerritory[i])

        #only urban or rural
        E.add_constraint(urbanVal[i] | ~urbanVal[i])

        #only one season
        E.add_constraint(S_autumn | S_spring | S_summer | S_winter)

        #Only one size pack of items
        E.add_constraint(shirtsS[i] | shirtsM[i] | shirtsL[i])#always selling
        E.add_constraint(swimN[i] | swimS[i] | swimM[i] | swimL[i])
        E.add_constraint(pantsS[i] | pantsM[i] | pantsL[i])#always selling
        E.add_constraint(jacketsN[i] | jacketsS[i] | jacketsM[i] | jacketsL[i])
        E.add_constraint(bootsS[i] | bootsM[i] | bootsL[i])#always selling

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

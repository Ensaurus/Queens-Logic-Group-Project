
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

inshirts100 = Var('var_inshirts100')
inshirts80 = Var('var_inshirts80')
inshirts60 = Var('var_inshirts60')
inshirts40 = Var('var_inshirts40')
inshirts20 = Var('var_inshirts20')
inshirts0 = Var('var_inshirts0')

if generalConditions.season == 'summer':
    S_summer = True
    S_spring = False
    S_winter = False
    S_autumn = False
if generalConditions.INshirts == 100:
    inshirts100 = True
    inshirts80 = True
    inshirts60 = True
    inshirts40 = True
    inshirts20 = True
    inshirts0 = True
if generalConditions.INswim == 100:
    inswim100 = True
    inswim80 = True
    inswim60 = True
    inswim40 = True
    inswim20 = True
    inswim0 = True
if generalConditions.INpants == 100:
    inpants100 = True
    inpants80 = True
    inpants60 = True
    inpants40 = True
    inpants20 = True
    inpants0 = True
if generalConditions.INjackets == 100:
    injackets100 = True
    injackets80 = True
    injackets60 = True
    injackets40 = True
    injackets20 = True
    injackets0 = True
if generalConditions.INboots == 100:
    inboots100 = True
    inboots80 = True
    inboots60 = True
    inboots40 = True
    inboots20 = True
    inboots0 = True

#Setup store values
#population = 500k, 100k, 50k, 20k, 0k
#urban = urban, rural
#region = atlantic, pacific, prairies, central, territory
#bestseller = shirts, swimwear, pants, jackets, boots
#regions = atlantic or territory or central
#bestseller values = shirts or swimwear
if (population[i] == '500k'):
    E.addConstraint(population500[i])
storeOb = []
storeOb.append(store('500k', 'urban', 'central', 'swimwear'))
storeOb.append(store('20k', 'rural', 'atlantic', 'shirts'))
storeOb.append(store('100k', 'urban', 'atlantic', 'swimwear'))
storeOb.append(store('100k', 'urban', 'central', 'shirts'))
storeOb.append(store('0k', 'rural', 'territory', 'shirts'))

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


def storeAssign():
    for i in range(5):
        if storeOb[i].population == '500k':
            population500[i] = True
            population100[i] = True
            population50[i] = True
            population20[i] = True
            population0[i] = True
        elif storeOb[i].population == '100k':    
            population500[i] = False
            population100[i] = True
            population50[i] = True
            population20[i] = True
            population0[i] = True
        elif storeOb[i].population == '50k':    
            population500[i] = False
            population100[i] = False
            population50[i] = True
            population20[i] = True
            population0[i] = True
        elif storeOb[i].population == '20k':    
            population500[i] = False
            population100[i] = False
            population50[i] = False
            population20[i] = True
            population0[i] = True
        elif storeOb[i].population == '0k':    
            population500[i] = False
            population100[i] = False
            population50[i] = False
            population20[i] = False
            population0[i] = True

        if storeOb[i].urban == 'urban':
            urbanVal[i] = True
        else:
            urbanVal[i] = False

        if storeOb[i].region == 'atlantic':
            regionAtlantic[i] = True
            regionCentral[i] = False
            regionTerritory[i] = False
        elif storeOb[i].region == 'central':
            regionAtlantic[i] = False
            regionCentral[i] = True
            regionTerritory[i] = False
        elif storeOb[i].region == 'territory':
            regionAtlantic[i] = False
            regionCentral[i] = False
            regionTerritory[i] = True

        if storeOb[i].bestSeller == 'shirts':
            bestsellerShirts[i] = True
            bestsellerSwimwear[i] = False
        elif storeOb[i].bestSeller == 'swimwear':
            bestsellerShirts[i] = False
            bestsellerSwimwear[i] = True
            

#run storeAssign
storeAssign()

#shipment sizes, array because its for 5 stores (0-4)
shirtsN = []
shirtsS = []
shirtsM = []
shirtsL = []

swimN = []
swimS = []
swimM = []
swimL = []

pantsN = []
pantsS = []
pantsM = []
pantsL = []

jacketsN = {}
jacketsS = {}
jacketsM = {}
jacketsL = {}
for i in range(5):
    jacketsN[i] = Var("jacketsN%d", i)
    jacketsS[i] = Var("jacketsS%d", i)
    jacketsM[i] = Var("jacketsM%d", i)
    jacketsL[i] = Var("jacketsL%d", i)

bootsN = []
bootsS = []
bootsM = []
bootsL = []

def example_theory():
    E = Encoding()

    for i in range(5):
        #Only one size pack of items
        #E.add_constraint(shirtsN[i] | shirtsS[i] | shirtsM[i] | shirtsL[i])
        #E.add_constraint(swimN[i] | swimS[i] | swimM[i] | swimL[i])
        #E.add_constraint(pantsN[i] | pantsS[i] | pantsM[i] | pantsL[i])
        #E.add_constraint(jacketsN[i] | jacketsS[i] | jacketsM[i] | jacketsL[i])
        #E.add_constraint(bootsN[i] | bootsS[i] | bootsM[i] | bootsL[i])
    
        #summer and not territories means jackets can't be sold
        E.add_constraint(~(S_summer & regionTerritory[i]) | jacketsN[i])

        #for selling jackets in summer
        E.add_constraint(~regionTerritory[i] | ~jacketsN[i])
        E.add_constraint(~S_summer | (~jacketsM[i] & ~jacketsL[i]))


    return E


if __name__ == "__main__":

    T = example_theory()

 
    print("\nSatisfiable: %s" % T.is_satisfiable())
    print("# Solutions: %d" % T.count_solutions())
    print("   Solution: %s" % T.solve())


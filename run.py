from functools import total_ordering
from os import umask
from nnf import Var
from lib204 import Encoding

from nnf import true

from display import display_solution
from checkBestCondition import check_best_conditions


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
'''
Only 1 season is true at a time
For inventory, number between 0 and 5.
For 4 and 5, we operate normally.
For 2 and 3, we usually reduce by 1 size, minimum small.
For 1, we usually reduce by 2 sizes, smaller stores may not get any.
For 0, no product shipped.
'''

S_summer = Var('S_summer')
S_spring = Var('S_spring')
S_winter = Var('S_winter')
S_autumn = Var('S_autumn')

IN_shirts45 = Var('IN_shirts45')
IN_swim45 = Var('IN_swim45')
IN_pants45 = Var('IN_pants45')
IN_jackets45 = Var('IN_jackets45')
IN_boots45 = Var('IN_boots45')

IN_shirts23 = Var('IN_shirts23')
IN_swim23 = Var('IN_swim23')
IN_pants23 = Var('IN_pants23')
IN_jackets23 = Var('IN_jackets23')
IN_boots23 = Var('IN_boots23')

IN_shirts1 = Var('IN_shirts1')
IN_swim1 = Var('IN_swim1')
IN_pants1 = Var('IN_pants1')
IN_jackets1 = Var('IN_jackets1')
IN_boots1 = Var('IN_boots1')

IN_shirts0 = Var('IN_shirts0')
IN_swim0 = Var('IN_swim0')
IN_pants0 = Var('IN_pants0')
IN_jackets0 = Var('IN_jackets0')
IN_boots0 = Var('IN_boots0')


population500 = {}
population100 = {}
population50 = {}
population20 = {}
population0 = {}

urbanVal = {}

regionAtlantic = {}
regionCentral = {}
regionTerritory = {}
regionPrairies = {}
regionPacific = {}

bestsellerShirts = {}
bestsellerSwimwear = {}
bestsellerPants = {}
bestsellerJackets = {}
bestsellerBoots = {}

for i in range(5):
    population500[i] = Var("population500_" + str(i))
    population100[i] = Var("population100_" + str(i))
    population50[i] = Var("population50_" + str(i))
    population20[i] = Var("population20_" + str(i))
    population0[i] = Var("population0_" + str(i))

    urbanVal[i] = Var("urbanVal_" + str(i))

    regionAtlantic[i] = Var("regionAtlantic_" + str(i))
    regionCentral[i] = Var("regionCentral_" + str(i))
    regionTerritory[i] = Var("regionTerritory_" + str(i))
    regionPrairies[i] = Var("regionPrairies_" + str(i))
    regionPacific[i] = Var("regionPacific_" + str(i))

    bestsellerShirts[i] = Var("bestsellerShirts_" + str(i))
    bestsellerSwimwear[i] = Var("bestsellerSwimwear_" + str(i))
    bestsellerPants[i] = Var("bestsellerPants_" + str(i))
    bestsellerJackets[i] = Var("bestsellerJackets_" + str(i))
    bestsellerBoots[i] = Var("bestsellerBoots_" + str(i))


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

def example_theory(generalConditions, storeOb):
    E = Encoding()

    '''
    Season
    '''
    if(generalConditions.season == 'summer'):
        E.add_constraint(S_summer)
    elif(generalConditions.season == 'winter'):
        E.add_constraint(S_winter)
    elif(generalConditions.season == 'spring'):
        E.add_constraint(S_spring)
    elif(generalConditions.season == 'autumn'):
        E.add_constraint(S_autumn)

    '''
    Inventory
    '''

    #shirts
    if(generalConditions.INshirts == 4 or generalConditions.INshirts == 5):
        E.add_constraint(IN_shirts45)
    elif(generalConditions.INshirts == 2 or generalConditions.INshirts == 3):
        E.add_constraint(IN_shirts23)
    elif(generalConditions.INshirts == 1):
        E.add_constraint(IN_shirts1)
    elif(generalConditions.INshirts == 0):
        E.add_constraint(IN_shirts0)

    #swimwear
    if(generalConditions.INswim == 4 or generalConditions.INswim == 5):
        E.add_constraint(IN_swim45)
    elif(generalConditions.INswim == 2 or generalConditions.INswim == 3):
        E.add_constraint(IN_swim23)
    elif(generalConditions.INswim == 1):
        E.add_constraint(IN_swim1)
    elif(generalConditions.INswim == 0):
        E.add_constraint(IN_swim0)

    #pants
    if(generalConditions.INpants == 4 or generalConditions.INpants == 5):
        E.add_constraint(IN_pants45)
    elif(generalConditions.INpants == 2 or generalConditions.INpants == 3):
        E.add_constraint(IN_pants23)
    elif(generalConditions.INpants == 1):
        E.add_constraint(IN_pants1)
    elif(generalConditions.INpants == 0):
        E.add_constraint(IN_pants0)

    #Jackets
    if(generalConditions.INjackets == 4 or generalConditions.INjackets == 5):
        E.add_constraint(IN_jackets45)
    elif(generalConditions.INjackets == 2 or generalConditions.INjackets == 3):
        E.add_constraint(IN_jackets23)
    elif(generalConditions.INjackets == 1):
        E.add_constraint(IN_jackets1)
    elif(generalConditions.INjackets == 0):
        E.add_constraint(IN_jackets0)

    #Boots
    if(generalConditions.INboots == 4 or generalConditions.INboots == 5):
        E.add_constraint(IN_boots45)
    elif(generalConditions.INboots == 2 or generalConditions.INboots == 3):
        E.add_constraint(IN_boots23)
    elif(generalConditions.INboots == 1):
        E.add_constraint(IN_boots1)
    elif(generalConditions.INboots == 0):
        E.add_constraint(IN_boots0)

    for i in range(5):
        #Set urban/rural for the specific store
        if(storeOb[i].urban == 'urban'):
            E.add_constraint(urbanVal[i])
        elif(storeOb[i].urban == 'rural'):
            E.add_constraint(~urbanVal[i])
        
        #Set region for each store
        if(storeOb[i].region == 'central'):
            E.add_constraint(regionCentral[i])
        elif(storeOb[i].region == 'atlantic'):
            E.add_constraint(regionAtlantic[i])
        elif(storeOb[i].region == 'territory'):
            E.add_constraint(regionTerritory[i])
        elif(storeOb[i].region == 'prairies'):   
            E.add_constraint(regionPrairies[i])
        elif(storeOb[i].region == 'pacific'):
            E.add_constraint(regionPacific[i])
        
        #Set population for each store
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

        #bestseller
        if(storeOb[i].bestSeller == 'shirts'):
            E.add_constraint(bestsellerShirts[i])
        elif(storeOb[i].bestSeller == 'swimwear'):
            E.add_constraint(bestsellerSwimwear[i])
        elif(storeOb[i].bestSeller == 'pants'):
            E.add_constraint(bestsellerPants[i])
        elif(storeOb[i].bestSeller == 'jackets'):
            E.add_constraint(bestsellerJackets[i])
        elif(storeOb[i].bestSeller == 'boots'):
            E.add_constraint(bestsellerBoots[i])

    for i in range(5):
        '''
        Basic Constraints
		Ensuring that each shipment can only be of one size, and each location can only have one size/region during one season
        '''
        #only one population
        E.add_constraint(exclusiveOr5(population500[i], population100[i], population50[i], population20[i], population0[i]))
        
        #only one region
        E.add_constraint(exclusiveOr5(regionAtlantic[i], regionCentral[i], regionTerritory[i], regionPacific[i], regionPrairies[i]))

        #only one season
        E.add_constraint(exclusiveOr4(S_autumn, S_spring, S_summer, S_winter))

        #Only one size pack of items
        E.add_constraint(exclusiveOr4(shirtsN[i], shirtsS[i], shirtsM[i], shirtsL[i]))
        E.add_constraint(exclusiveOr4(swimN[i], swimS[i], swimM[i], swimL[i]))
        E.add_constraint(exclusiveOr4(pantsN[i], pantsS[i], pantsM[i], pantsL[i]))
        E.add_constraint(exclusiveOr4(jacketsN[i], jacketsS[i], jacketsM[i], jacketsL[i]))
        E.add_constraint(exclusiveOr4(bootsN[i], bootsS[i], bootsM[i], bootsL[i]))

        #Only one inventory size
        E.add_constraint(exclusiveOr4(IN_shirts45, IN_shirts23, IN_shirts1, IN_shirts0))
        E.add_constraint(exclusiveOr4(IN_swim45, IN_swim23, IN_swim1, IN_swim0))
        E.add_constraint(exclusiveOr4(IN_pants45, IN_pants23, IN_pants1, IN_pants0))
        E.add_constraint(exclusiveOr4(IN_jackets45, IN_jackets23, IN_jackets1, IN_jackets0))
        E.add_constraint(exclusiveOr4(IN_boots45, IN_boots23, IN_boots1, IN_boots0))

        #only one best seller item
        E.add_constraint(exclusiveOr5(bestsellerShirts[i], bestsellerSwimwear[i], bestsellerPants[i], bestsellerJackets[i], bestsellerBoots[i]))

        '''
        What we could consider as the 'actual' constraints
        '''
        #
        #Constraints divided w.r.t clothing categories
        #
        '''
        Shirts

        Shirts are liked in every season, every region and in both urban and rural populations,
        so the quantity only depends upon the population and bestseller category.
        No splitting of code between each supply category.
        '''
        #Adequate supply of shirts
        if (E.is_constraint(IN_shirts45)):
            #population >100k
            E.add_constraint((population100[i] | population500[i]) >> shirtsL[i])

            #population <100k, >50k
            E.add_constraint(population50[i] >> (shirtsM[i] | shirtsL[i]))
            E.add_constraint((~bestsellerShirts[i] & population50[i]) >> shirtsM[i])
            
            #population <50k
            E.add_constraint((population0[i] | population20[i]) >> (shirtsS[i] | shirtsM[i]))
            E.add_constraint((~bestsellerShirts[i] & (population0[i] | population20[i])) >> shirtsS[i])

        #Low supply of shirts
        elif (E.is_constraint(IN_shirts23)):
            #population > 500k
            E.add_constraint(population500[i] >> shirtsL[i])

            #population >100k
            E.add_constraint(population100[i] >> (shirtsM[i] | shirtsL[i]))
            E.add_constraint((~bestsellerShirts[i] & population100[i]) >> shirtsM[i])

            #population < 100k
            E.add_constraint((population50[i] | population20[i]) >> (shirtsS[i] | shirtsM[i]))
            E.add_constraint((~bestsellerShirts[i] & (population50[i] | population20[i])) >> shirtsS[i])

            #population <20k
            E.add_constraint(population0[i] >> (shirtsN[i] | shirtsS[i]))
            E.add_constraint((~bestsellerShirts[i] & population0[i]) >> shirtsN[i])

        #Very low supply of shirts
        elif (E.is_constraint(IN_shirts1)):
            #population >100k
            E.add_constraint((population100[i] | population500[i]) >> (shirtsS[i] | shirtsM[i]))
            E.add_constraint((~bestsellerShirts[i] & (population100[i] | population500[i])) >> shirtsS[i])

            #population <100k
            E.add_constraint((population50[i] | population20[i] | population0[i]) >> (shirtsN[i] | shirtsS[i]))
            E.add_constraint((~bestsellerShirts[i] & (population50[i] | population20[i] | population0[i])) >> shirtsN[i])

        #No supply
        else:
            E.add_constraint(shirtsN[i])

        '''
        Swimwear

        Coastal regions (atlantic and pacific) and central have the highest demand for swimwear.
        Territories have very little demand. 
        Summers and spring are the best seasons.
        '''

        #General for winter
        E.add_constraint((S_winter & (regionTerritory[i] | regionPrairies[i])) >> swimN[i])
        
        #General for territores
        E.add_constraint((regionTerritory[i] & ~S_summer) >> swimN[i])

        #Adequate supply of swimwear
        if (E.is_constraint(IN_swim45)):
            
            #winter
            E.add_constraint(S_winter >> (swimN[i] | swimS[i]))

            #Not winter
            if(E.is_constraint(S_summer) | E.is_constraint(S_spring) | E.is_constraint(S_autumn)):
                #population >100k
                E.add_constraint((population100[i] | population500[i]) >> (swimL[i] | swimN[i]))

                #population <100k, >50k
                E.add_constraint(population50[i] >> (swimM[i] | swimL[i] | swimN[i]))
                E.add_constraint((~bestsellerSwimwear[i] & population50[i]) >> (swimM[i] | swimN[i]))
                
                #population <50k
                E.add_constraint((population0[i] | population20[i]) >> (swimS[i] | swimM[i] |swimN[i]))
                E.add_constraint((~bestsellerSwimwear[i] & (population0[i] | population20[i])) >> (swimS[i] | swimN[i]))

        #Low supply of swimwear
        elif (E.is_constraint(IN_swim23)):
            
            #winter
            E.add_constraint(S_winter >> (swimN[i] | swimS[i]))

            #other seasons
            if(E.is_constraint(S_summer) | E.is_constraint(S_spring) | E.is_constraint(S_autumn)):
                #population >100k
                E.add_constraint((population500[i] | population100[i]) >> (swimM[i] | swimS[i] | swimN[i]))
                E.add_constraint(((population500[i] | population100[i]) & ~bestsellerSwimwear[i]) >> (swimS[i] | swimN[i]))

                #population <100k
                E.add_constraint((population50[i] | population20[i] | population0[i]) >> (swimM[i] | swimS[i] | swimN[i]))
                E.add_constraint(((population50[i] | population20[i] | population0[i]) & ~bestsellerSwimwear[i]) >> (swimS[i] | swimN[i]))

        #Very low supply of swimwear        
        elif (E.is_constraint(IN_swim1)):
            
            #winter
            E.add_constraint(S_winter >> (swimN[i] | swimS[i]))

            #other seasons
            if(E.is_constraint(S_summer) | E.is_constraint(S_spring) | E.is_constraint(S_autumn)):
                #population >100k
                E.add_constraint((population500[i] | population100[i]) >> (swimM[i] | swimS[i] | swimN[i]))
                E.add_constraint(((population500[i] | population100[i]) & ~bestsellerSwimwear[i]) >> (swimS[i] | swimN[i]))

                #population <100k
                E.add_constraint((population50[i] | population20[i] | population0[i]) >> (swimS[i] | swimN[i]))

            
        
        #No supply
        else:
            E.add_constraint(swimN[i])
        '''  
        Pants

        Except the territories, all regions have slighly lower requirements for pants in the 
        summers since some people switch to wearing shorts.
        Generally pretty stable requirements just like shirts.
        Split the code between summers and non summers.
        ''' 
        #Adequate supply of Pants
        if (E.is_constraint(IN_pants45)):

            if(E.is_constraint(S_summer)):
                #population >500k
                E.add_constraint(population500[i] >> pantsL[i])

                #population >50k
                E.add_constraint((population100[i] | population50[i]) >> (pantsM[i] | pantsL[i]))
                E.add_constraint(((population100[i] | population50[i]) & (~regionTerritory[i] | ~bestsellerPants[i])) >> pantsM[i])
            
                #population <50k
                E.add_constraint((population0[i] | population20[i]) >> (pantsS[i] | pantsM[i]))
                E.add_constraint(((population0[i] | population20[i]) & (~regionTerritory[i] | ~bestsellerPants[i])) >> pantsS[i])

            else:
                #population >100k
                E.add_constraint((population100[i] | population500[i]) >> pantsL[i])

                #population <100k, >50k
                E.add_constraint(population50[i] >> (pantsM[i] | pantsL[i]))
                E.add_constraint((~bestsellerPants[i] & population50[i]) >> pantsM[i])
                
                #population <50k
                E.add_constraint((population0[i] | population20[i]) >> (pantsS[i] | pantsM[i]))
                E.add_constraint((~bestsellerPants[i] & (population0[i] | population20[i])) >> pantsS[i])

        #Low supply of Pants
        elif (E.is_constraint(IN_pants23)):

            if(E.is_constraint(S_summer)):

                #population >100k
                E.add_constraint((population500[i] | population100[i] | population50[i]) >> (pantsM[i] | pantsL[i]))
                E.add_constraint(((population500[i] | population100[i] | population50[i]) & (~regionTerritory[i] | ~bestsellerPants[i])) >> pantsM[i])

                #population <100k
                E.add_constraint((population50[i] | population20[i]) >> (pantsM[i] | pantsL[i]))
                E.add_constraint(((population50[i] | population20[i]) & (~regionTerritory[i] | ~bestsellerPants[i])) >> pantsM[i])

                #population <20k
                E.add_constraint(population0[i] >> (pantsN[i] | pantsS[i]))
                E.add_constraint((~bestsellerPants[i] & population0[i]) >> pantsN[i])

            else:
                #population > 500k
                E.add_constraint(population500[i] >> pantsL[i])

                #population >100k
                E.add_constraint(population100[i] >> (pantsM[i] | pantsL[i]))
                E.add_constraint((~bestsellerPants[i] & population100[i]) >> pantsM[i])

                #population < 100k
                E.add_constraint((population50[i] | population20[i]) >> (pantsS[i] | pantsM[i]))
                E.add_constraint((~bestsellerPants[i] & (population50[i] | population20[i])) >> pantsS[i])

                #population <20k
                E.add_constraint(population0[i] >> (pantsN[i] | pantsS[i]))
                E.add_constraint((~bestsellerPants[i] & population0[i]) >> pantsN[i])
        
        #Very low supply of Pants        
        elif (E.is_constraint(IN_pants1)):
            #population >100k
            E.add_constraint((population100[i] | population500[i]) >> (pantsS[i] | pantsM[i]))
            E.add_constraint((~bestsellerPants[i] & (population100[i] | population500[i])) >> pantsS[i])

            #population <100k
            E.add_constraint((population50[i] | population20[i] | population0[i]) >> (pantsN[i] | pantsS[i]))
            E.add_constraint((~bestsellerPants[i] & (population50[i] | population20[i] | population0[i])) >> pantsN[i])
        
        #No supply
        else:
            E.add_constraint(pantsN[i])
        ''' 
        Jackets

        The requirements for jackets varies heavily across the different regions and seasons.
        Split the code based on the region, since demand is more dependent upon region as compared to season.
        ''' 
        #Adequate supply of Jackets
        if (E.is_constraint(IN_jackets45)):

            #territory
            if(E.is_constraint(regionTerritory[i])):
                
                E.add_constraint(regionTerritory[i] >> (jacketsL[i] | jacketsM[i]))
                #population <50k
                E.add_constraint((population20[i] | population0[i]) >> jacketsM[i])
            
            #atlantic and pacific
            elif(E.is_constraint(regionAtlantic[i]) | E.is_constraint(regionPacific[i])):

                #population >100k
                E.add_constraint((population500[i] | population100[i]) >> (jacketsM[i] | jacketsL[i]))
                E.add_constraint(((population500[i] | population100[i]) & S_summer & ~bestsellerJackets[i]) >> jacketsM[i])

                #population >50k
                E.add_constraint(population50[i] >> (jacketsS[i] | jacketsM[i]))
                E.add_constraint((population50[i] & ~bestsellerJackets[i]) >> jacketsS[i])

                #population <50k
                E.add_constraint((population20[i] | population0[i]) >> (jacketsS[i] | jacketsM[i]))
                E.add_constraint(((population20[i] | population0[i]) & (S_summer | ~bestsellerJackets[i])) >> jacketsS[i])
            
            #central
            elif(E.is_constraint(regionCentral[i])):
                
                #Summers
                E.add_constraint(S_summer >> jacketsN[i])

                #spring
                E.add_constraint(S_spring >> jacketsS[i])

                #population > 100k
                E.add_constraint(((S_winter | S_autumn) & (population500[i] | population100[i])) >> jacketsL[i])

                #population >50k
                E.add_constraint(((S_winter | S_autumn) & population50[i]) >> (jacketsL[i] | jacketsM[i]))
                E.add_constraint(((S_winter | S_autumn) & population50[i] & ~bestsellerJackets[i]) >> jacketsM[i])

                #population <50k
                E.add_constraint(((S_winter | S_autumn) & (population20[i] | population0[i])) >> (jacketsM[i] | jacketsS[i]))
                E.add_constraint(((S_winter | S_autumn) & (population20[i] | population0[i]) & ~bestsellerJackets[i]) >> jacketsS[i])
            
            #prairies
            elif(E.is_constraint(regionPrairies[i])):
                
                #population >100k
                E.add_constraint(((S_winter | S_autumn) & (population500[i] | population100[i])) >> jacketsL[i])
                E.add_constraint(((S_spring | S_summer) & (population500[i] | population100[i])) >> (jacketsL[i] | jacketsM[i]))
                E.add_constraint((S_spring & (population100[i] & ~bestsellerJackets[i])) >> jacketsM[i])
                E.add_constraint((S_summer & (population100[i] & ~bestsellerJackets[i])) >> jacketsM[i])
                
                #population >50k
                E.add_constraint(((S_winter | S_autumn) & population50[i]) >> jacketsM[i])
                E.add_constraint(((S_spring | S_summer) & population50[i]) >> (jacketsM[i] | jacketsS[i]))
                E.add_constraint(((S_spring | S_summer) & population50[i] & ~bestsellerJackets[i]) >> jacketsS[i])
                
                #population <50k
                E.add_constraint(population20[i] >> (jacketsS[i] | jacketsM[i]))
                E.add_constraint((population20[i] & (~bestsellerJackets[i] | S_spring | S_summer)) >> jacketsS[i])

                #population <20k
                E.add_constraint(population0[i] >> (jacketsN[i] | jacketsS[i]))
                E.add_constraint((population0[i] & S_summer & ~bestsellerJackets[i]) >> jacketsN[i])
                
        #Low supply of Jackets
        elif (E.is_constraint(IN_jackets23)):
            list_terr = []
            #If we have stores in territories, only they get jackets
            #The following code checks if we have any stores in territories,
            #if yes, only they get jackets,
            #if no, all stores get a small amount of jackets
            if(i == 0):
                for j in range(5):
                    if(E.is_constraint(regionTerritory[j])):
                        list_terr.append(j)

                if(len(list_terr) != 0):
                    for k in range(5):
                        
                        if k in list_terr:
                            E.add_constraint(jacketsM[k])
                        else:
                            E.add_constraint(jacketsS[k])
                else:
                    for k in range(5):
                        E.add_constraint(S_winter >> jacketsM[k])
                        E.add_constraint(~S_winter >> jacketsS[k])

        #Very low supply of Jackets        
        elif (E.is_constraint(IN_jackets1)):
            list_terr = []
            #If we have stores in territories, only they get jackets
            #The following code checks if we have any stores in territories,
            #if yes, only they get jackets,
            #if no, all stores get a small amount of jackets
            #unless the store is is small, pop <50k
            if(i == 0):
                for j in range(5):
                    if(E.is_constraint(regionTerritory[j])):
                        list_terr.append(j)
                        #print("appended " + str(j) + ".")

                if(len(list_terr) != 0):
                    for k in range(5):
                        
                        if k in list_terr:
                            E.add_constraint(jacketsS[k])
                            #print("small " + str(k) + ".")
                        else:
                            E.add_constraint(jacketsN[k])
                            #print("none " + str(k) + ".")
                
                else:
                    for k in range(5):
                        E.add_constraint(jacketsS[k] | jacketsN[k])
                        E.add_constraint((population0[k] | population20[k]) >> jacketsN[k])

        #No supply
        else:
            E.add_constraint(jacketsN[i])
        ''' 
        Boots

        Boots are slightly less popular in the central region (in spring and summer) as compared to rest of Canada. 
        Boots are also more popular in rural areas than in urban areas.
        Split between central and other areas.
        ''' 
        #Adequate supply of Boots
        if (E.is_constraint(IN_boots45)):
            
            #population >100k
            E.add_constraint((population500[i] | population100[i]) >> bootsL[i])

            #Central region
            if(E.is_constraint(regionCentral[i])):

                #population >50k
                E.add_constraint(((S_winter | S_autumn) & population50[i]) >> (bootsM[i] | bootsL[i]))
                E.add_constraint(((S_winter | S_autumn) & population50[i] & (~bestsellerBoots[i] | urbanVal[i])) >> bootsM[i])

                E.add_constraint(((S_summer | S_spring) & population50[i]) >> bootsM[i])

                #population <50k
                E.add_constraint(((S_winter | S_autumn) & (population20[i] | population0[i])) >> (bootsS[i] | bootsM[i]))
                E.add_constraint(((S_winter | S_autumn) & (population20[i] | population0[i]) & (~bestsellerBoots[i] | urbanVal[i])) >> bootsS[i])

                E.add_constraint(((S_summer | S_spring) & (population20[i] | population0[i])) >> bootsS[i])

            #Other regions
            else:
                #population <100k, >50k
                E.add_constraint(population50[i] >> (bootsM[i] | bootsL[i]))
                E.add_constraint(((~bestsellerBoots[i] | urbanVal[i]) & population50[i]) >> bootsM[i])
                
                #population <50k
                E.add_constraint((population0[i] | population20[i]) >> (bootsS[i] | bootsM[i]))
                E.add_constraint(((~bestsellerBoots[i] | urbanVal[i]) & (population0[i] | population20[i])) >> bootsS[i])

        
        #Low supply of Boots
        elif (E.is_constraint(IN_boots23)):
            
            #population >500k
            E.add_constraint(population500[i] >> bootsL[i])

            #Central region
            if(E.is_constraint(regionCentral[i])):

                #population >50k
                E.add_constraint(((S_winter | S_autumn) & (population50[i] | population100[i])) >> (bootsS[i] | bootsM[i]))
                E.add_constraint(((S_winter | S_autumn) & population50[i] & (~bestsellerBoots[i] | urbanVal[i])) >> bootsS[i])

                E.add_constraint(((S_summer | S_spring) & population50[i]) >> bootsS[i])

                #population <50k
                E.add_constraint((population0[i] | population20[i]) >> bootsS[i])

            #Other regions
            else:
                #population <100k, >50k
                E.add_constraint((population50[i] | population100[i]) >> (bootsS[i] | bootsM[i]))
                E.add_constraint(((~bestsellerBoots[i] | urbanVal[i]) & population50[i]) >> bootsS[i])
                
                #population <50k
                E.add_constraint((population0[i] | population20[i]) >> bootsS[i])
                

        #Very low supply of Boots        
        elif (E.is_constraint(IN_boots1)):
            #population >100k
            E.add_constraint((population100[i] | population500[i]) >> (bootsS[i] | bootsM[i]))
            E.add_constraint(((~bestsellerShirts[i] | urbanVal[i]) & (population100[i] | population500[i])) >> bootsS[i])

            #population <100k
            E.add_constraint((population50[i] | population20[i] | population0[i]) >> (bootsN[i] | bootsS[i]))
            E.add_constraint(((~bestsellerShirts[i] | urbanVal[i]) & (population50[i] | population20[i] | population0[i])) >> bootsN[i])

        
        #No supply
        else:
            E.add_constraint(bootsN[i])

    return E


	#A small function that gets which season the stores are currently operating under
def getSeason():
	isInvalid = True
	userInput = 0
	print("1 = Spring")
	print("2 = Summer")
	print("3 = Autumn")
	print("4 = Winter")
	while isInvalid:
		try:
			userInput = int(input("Please enter the current season as an integer between 1 and 4: "))
			if ((1 <= userInput) and (userInput <= 4)):
				isInvalid = False
			else:
				print("Value entered is out of bounds provided.")
		except Exception as e:
			print(e)
	if (userInput == 1):
		return 'spring'
	elif (userInput == 2):
		return 'summer'
	elif (userInput == 3):
		return 'autumn'
	else:
		return 'winter'


	#A function that loops for each article being shipped and gets its stock value from 0-5 from the user
def getSetup(product):
	isInvalid = True
	userInput = 0
	while isInvalid:
		try:
			userInput = int(input("Enter the integer stock value between 0 and 5 for " + product + ": "))
			if ((0 <= userInput) and (userInput <= 5)):
				isInvalid = False
			else:
				print("Value entered is out of bounds provided.")
		except Exception as e:
			print(e)
	return userInput

if __name__ == "__main__":

#general setup
	#Season = summer, spring, autumn, winter
	#inventory = 0, 1, 2, 3, 4, 5
	#products ordered shirts, swimwear, pants, jackets, boots
    generalConditions = setup(getSeason(), getSetup('shirts'), getSetup('swimwear'), getSetup('pants'), getSetup('jackets'), getSetup('boots'))

    #stores setup (5 stores)
    #500k, 100k,, 50k, 20k, 0k
    #urban, rural
    #central, atlantic, territory, prairies, pacific
    #shirts, swimwear, pants, jackets, boots
    storeOb = []
    storeOb.append(store('500k', 'urban', 'central', 'swimwear'))
    storeOb.append(store('100k', 'rural', 'territory', 'shirts'))
    storeOb.append(store('50k', 'urban', 'prairies', 'swimwear'))
    storeOb.append(store('20k', 'urban', 'pacific', 'pants'))
    storeOb.append(store('0k', 'rural', 'territory', 'shirts'))

    T = example_theory(generalConditions, storeOb)
    print("\nSatisfiable: %s" % T.is_satisfiable())
    print("# Solutions: %d" % T.count_solutions())
    #print(T.solve())
    if(T.is_satisfiable()):
        print("\n\nNow trying to find the best solution, \n")

        T = check_best_conditions(T, shirtsL, shirtsM, shirtsS, swimL, swimM, swimS, pantsL, pantsM, pantsS, jacketsL, jacketsM, jacketsS, bootsL, bootsM, bootsS)
 
        print("\nSatisfiable: %s" % T.is_satisfiable())
        print("# Solutions: %d" % T.count_solutions())
        print("\nPossible Solution:\n")
        display_solution(T.solve())

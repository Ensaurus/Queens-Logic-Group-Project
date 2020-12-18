'''
File has all of the code to properly format and display the solution given by the model
'''
#Define constants for the displaying information

SUMMER = "summer"
SPRING = "spring"
WINTER = "winter"
AUTUMN = "autumn"

P500K = "greater than 500 thousand"
P100K = "greater than 100 thousand"
P50K = "greater than 50 thousand"
P20K = "greater than 20 thousand"
P0K = "less than 20 thousand"

URBAN = "an urban"
RURAL = "a rural"

ATLANTIC = "atlantic"
PACIFIC = "pacific"
TERRITORIES = "territories"
PRAIRIES = "prairies"
CENTRAL = "central"

SHIRTS = "shirts"
SWIM = "swimwear"
PANTS = "pants"
JACKETS = "jackets"
BOOTS = "boots"

HIGH = "adequate"
MEDIUM = "low"
LOW = "very low"
NONE = "empty"

#print general values for each store
def set_store_vals(solution):
    
    for i in range(5):
        #population
        if(solution["population500_" + str(i)]):
            population = P500K
        elif(solution["population100_" + str(i)]):
            population = P100K
        elif(solution["population50_" + str(i)]):
            population = P50K
        elif(solution["population20_" + str(i)]):
            population = P20K
        else:
            population = P0K
        
        #urban
        if(solution["urbanVal_" + str(i)]):
            urbanRural = URBAN
        else:
            urbanRural = RURAL

        #region
        if(solution["regionAtlantic_" + str(i)]):
            region = ATLANTIC
        elif(solution["regionCentral_" + str(i)]):
            region = CENTRAL
        elif(solution["regionTerritory_" + str(i)]):
            region = TERRITORIES
        elif(solution["regionPrairies_" + str(i)]):
            region = PRAIRIES
        elif(solution["regionPacific_" + str(i)]):
            region = PACIFIC

        print("Store " + str(i+1) + " serves a population " + population + ", is in " + urbanRural + " area and is in the " + region + " region.")
    print()

#set values to be printed, depends upon input variables and model output
def set_vals(solution):
    #season
    if(solution["S_summer"]):
        season = SUMMER
    elif(solution["S_winter"]):
        season = WINTER
    elif(solution["S_spring"]):
        season = SPRING
    elif(solution["S_autumn"]):
        season = AUTUMN

    #inventory levels

    #shirts
    if(solution["IN_shirts45"]):
        IN_shirts = HIGH
    elif(solution["IN_shirts23"]):
        IN_shirts = MEDIUM
    elif(solution["IN_shirts1"]):
        IN_shirts = LOW
    else:
        IN_shirts = NONE

    #swim
    if(solution["IN_swim45"]):
        IN_swim = HIGH
    elif(solution["IN_swim23"]):
        IN_swim = MEDIUM
    elif(solution["IN_swim1"]):
        IN_swim = LOW
    else:
        IN_swim = NONE

    #pants
    if(solution["IN_pants45"]):
        IN_pants = HIGH
    elif(solution["IN_pants23"]):
        IN_pants = MEDIUM
    elif(solution["IN_pants1"]):
        IN_pants = LOW
    else:
        IN_pants = NONE

    #jackets
    if(solution["IN_jackets45"]):
        IN_jackets = HIGH
    elif(solution["IN_jackets23"]):
        IN_jackets = MEDIUM
    elif(solution["IN_jackets1"]):
        IN_jackets = LOW
    else:
        IN_jackets = NONE

    #boots
    if(solution["IN_boots45"]):
        IN_boots = HIGH
    elif(solution["IN_boots23"]):
        IN_boots = MEDIUM
    elif(solution["IN_boots1"]):
        IN_boots = LOW
    else:
        IN_boots = NONE

    return season, IN_shirts, IN_swim, IN_pants, IN_jackets, IN_boots

#Print the general details, i.e, input values
def display_general(Solution):
    sol = Solution
    #call set_vals
    season, IN_shirts, IN_swim, IN_pants, IN_jackets, IN_boots = set_vals(sol)

    #start printing
    print("The current season is " + season)
    print("The quantity of shirts is " + IN_shirts)
    print("The quantity of swimwear is " + IN_swim)
    print("The quantity of pants is " + IN_pants)
    print("The quantity of jackets is " + IN_jackets)
    print("The quantity of boots is " + IN_boots + '\n')

    set_store_vals(sol)
    
#Print the model solution
def display_solution(Solution):
    sol = Solution
    #call display_general
    display_general(sol)

    for i in range(5):
        
        print("STORE " + (str)(i+1))
        
        #Shirts
        if (Solution['shirtsN_' + str(i)]) == True:
            print("Shirts - None")
        elif (Solution['shirtsS_' + str(i)]) == True:
            print("Shirts - Small Pack")
        elif (Solution['shirtsM_' + str(i)]) == True:
            print("Shirts - Medium Pack")
        elif (Solution['shirtsL_' + str(i)]) == True:
            print("Shirts - Large Pack")

        #Swim
        if (Solution['swimN_' + str(i)]) == True:
            print("Swimwear - None")
        elif (Solution['swimS_' + str(i)]) == True:
            print("Swimwear - Small Pack")
        elif (Solution['swimM_' + str(i)]) == True:
            print("Swimwear - Medium Pack")
        elif (Solution['swimL_' + str(i)]) == True:
            print("Swimwear - Large Pack")

        #Pants
        if (Solution['pantsN_' + str(i)]) == True:
            print("Pants - None")
        elif (Solution['pantsS_' + str(i)]) == True:
            print("Pants - Small Pack")
        elif (Solution['pantsM_' + str(i)]) == True:
            print("Pants - Medium Pack")
        elif (Solution['pantsL_' + str(i)]) == True:
            print("Pants - Large Pack")

        #jackets
        if (Solution['jacketsN_' + str(i)]) == True:
            print("Jackets - None")
        elif (Solution['jacketsS_' + str(i)]) == True:
            print("Jackets - Small Pack")
        elif (Solution['jacketsM_' + str(i)]) == True:
            print("Jackets - Medium Pack")
        elif (Solution['jacketsL_' + str(i)]) == True:
            print("Jackets - Large Pack")

        #Boots
        if (Solution['bootsN_' + str(i)]) == True:
            print("Boots - None\n")
        elif (Solution['bootsS_' + str(i)]) == True:
            print("Boots - Small Pack\n")
        elif (Solution['bootsM_' + str(i)]) == True:
            print("Boots - Medium Pack\n")
        elif (Solution['bootsL_' + str(i)]) == True:
            print("Boots - Large Pack\n")

    
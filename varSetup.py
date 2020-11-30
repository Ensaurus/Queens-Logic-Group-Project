def variableSetup():

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
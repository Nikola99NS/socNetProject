def grafPlusToMap(graf):
    mapa = {}
    komsije = []
    komsijePlus = []
    
    for ime in graf.nodes :
        # print(ime)
        # print("Komsije za {} :".format(ime),list(graf.neighbors(ime)))
        for komsija in list(graf.neighbors(ime)):
            if graf.get_edge_data(ime,komsija)['znak'] == "+" :
                komsije.append(komsija)
        mapa[ime]=komsije
        komsije = []

    return mapa



    




from asyncio.windows_events import NULL
from gettext import NullTranslations
import networkx as nx
import random
from analiza import prosecanStepenGrafa, prosecanStepenKomponenti, prosecanDijametar
from komponente import proveriKoalicije
from rucniGraf import ucitaj_klasterabilan, ucitaj_neklasterabilan
from komponente import vratiKomponente, proveriKoalicije, vratiGrafoveAntiKoalicija, kreirajGrafKlastera, izbaciMinusGrane
from nacrtaj import nacrtaj
from msilib.schema import SelfReg
from ucitajTxt import ucitaj_wiki, ucitaj_slashdot, ucitaj_epinions
from os import path
import os



def main():


    brojGrafa =input ("Unesite koji graf zelite da analiziramo:\n 1. za rucni klasterabilan \n 2. za rucni neklasterabilan \n 3. za random generisan \n 4. za ucitavanje grafa iz wiki.txt fajla \n 5.za ucitavanje grafa iz slashdot.txt fajla \n 6. za ucitavanje grafa iz epinions.txt")   
    brGrafa = int(brojGrafa)
    g = ucitajGraf(brGrafa)
 
    print("Broj grana grafa : ",len(g.edges))
    print("Broj cvorova grafa : ", len(g.nodes))
    mapaKomponenti = vratiKomponente(g)
    print(mapaKomponenti)
    print("Broj komponenti je : ",len(mapaKomponenti.keys()))
    print("Broj povezanih komponenti : ",nx.number_connected_components(g))

    brAntikoalicija = proveriKoalicije(mapaKomponenti, g)

    if brAntikoalicija == 0 :
        print("Komponente su : ", list(mapaKomponenti.values()))
        print ("Ovako izgleda graf : ")
        nacrtaj(g)
        print("Graf je klasterabilan. Nema antikoalicija")
        print("Prosecan stepen grafa", str(round(prosecanStepenGrafa(g),2)))

       

    else :
        if brGrafa >0 and brGrafa < 4 :
            nacrtaj(g)
        print("Graf nije klasterabilan")
        antiKoalicijeListOfGrafs = vratiGrafoveAntiKoalicija(mapaKomponenti, len(mapaKomponenti.keys()),g)
        if brGrafa > 0 and brGrafa < 4 : 
            for i in  antiKoalicijeListOfGrafs :
                print("Graf antikoalicija")
                nacrtaj(i)

        print("postoji {} koalicija".format(len(mapaKomponenti.keys()) - brAntikoalicija))
        print("Postoji {} antikoalicija".format(brAntikoalicija))
        print("Broj grana koje narusavaju klasterabilnost ", SelfReg.brojac)
        # print(SelfReg.minusGrane) 

        grafPosleIzbacivanja = izbaciMinusGrane(antiKoalicijeListOfGrafs, g)
        # print(antiKoalicijeListOfGrafs[0].edges(data=True))
        # print("Graf posle izbacivanja")
        print("Graf posle izbacivanja grana koje smetaju", grafPosleIzbacivanja)
        
        if brGrafa > 0 and brGrafa <4:
            nacrtaj(grafPosleIzbacivanja)

        # mapaPosleIzbacivanjaMinusGrana = grafPlusToMap(grafPosleIzbacivanja)
        mapaKompPosleIzbacivanjaMinusGrana = vratiKomponente(grafPosleIzbacivanja)
        print("Nakon izbacivanja grana koje smetaju, postoji {} antikoalicija".format(proveriKoalicije(mapaKompPosleIzbacivanjaMinusGrana, grafPosleIzbacivanja)))


        print("Sledi analiza grafova")
        print("Prosecan stepen grafa", str(round(prosecanStepenGrafa(g),2)))
        print("Stepen grafa koalicija", str(round(prosecanStepenGrafa(grafPosleIzbacivanja),2)))
        print("prosecan stepen  antikoalicija", str(round(prosecanStepenKomponenti(NULL, g , antiKoalicijeListOfGrafs), 2)))    

        print("Proecan dijametar antikoalicija ",prosecanDijametar(antiKoalicijeListOfGrafs))
        





    




def ucitajGraf(brojGrafa):
    if brojGrafa == 1:
        g = ucitaj_klasterabilan()
        return g
    elif brojGrafa == 2:
        g = ucitaj_neklasterabilan()
        return g
    elif brojGrafa == 3:
        g = nx.tutte_graph()
        g = oznaci_grane_grafa(g)
        return g
    elif brojGrafa == 4:
        g = ucitaj_wiki(path.join(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)), "files", "wiki-RFA.txt"))
        return g
    elif brojGrafa == 5:
        g = ucitaj_slashdot(path.join(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)), "klase", "soc-sign-slashdot.txt"))
        return g
    elif brojGrafa == 6:
        g = ucitaj_epinions(path.join(path.join(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))), "files", "bitcoin-epinions.csv"))
        return g



def oznaci_grane_grafa(g):
    g.edges(data=True)
    nx.set_edge_attributes(g, "+", "znak")
    epsilon = 0.33
    for (u, v) in g.edges():
        if random.uniform(0, 1) < epsilon:
            g.add_edge(u, v, znak="-")
    return g



   
main()
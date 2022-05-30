import networkx as nx
import random
from komponente import proveriKoalicije
from rucniKlasterabilanGraf import ucitaj, ucitaj_neklasterabilan
from grafToMap import grafPlusToMap
from komponente import vratiKomponente, proveriKoalicije, vratiGrafoveAntiKoalicija, kreirajKlaster, izbaciMinusGrane
from nacrtaj import nacrtaj
from msilib.schema import SelfReg
from ucitajTxt import ucitaj_wiki
from os import path
import os



def main():


    brojGrafa =input ("Unesite koji graf zelite da analiziramo:\n 1. za rucni klasterabilan \n 2. za rucni neklasterabilan \n 3. za random generisan \n 4. za ucitavanje grafa iz .txt fajla ")   
    brGrafa = int(brojGrafa)
    g = ucitajGraf(brGrafa)
    # nacrtaj(g)
    # print(g.edges(data=True))
    print("Broj grana grafa : ",len(g.edges))
    grafPlusMap = grafPlusToMap(g)
    # print(grafPlusMap)
    mapaKomponenti = vratiKomponente(grafPlusMap)
    print("Broj komponenti je : ",len(mapaKomponenti.keys()))
    print(mapaKomponenti)
    daLiJeKlasterabilan = proveriKoalicije(mapaKomponenti, len(mapaKomponenti.keys()), g)


    antiKoalicijeListOfGrafs = []

    if daLiJeKlasterabilan==True :
        print("Graf je klasterabilan")
        print("Graf za {}. koaliciju ce biti prikazan".format(2))
        # nacrtaj(kreirajKlaster(mapaKomponenti[list(mapaKomponenti.keys())[1]], g))
        
    else :
        print("Graf nije klasterabilan")
        antiKoalicijeListOfGrafs = vratiGrafoveAntiKoalicija(mapaKomponenti, len(mapaKomponenti.keys()),g)
        print("Postoji {} antikoalicija".format(len(antiKoalicijeListOfGrafs)))
        for i in range (0,len(antiKoalicijeListOfGrafs)):
            print("Cvorovi {}. antiKoalicije".format(i),antiKoalicijeListOfGrafs[i].edges(data=True))

        # if antiKoalicijeListOfGrafs:
            # print("Graf antikoalicija")
            # nacrtaj(antiKoalicijeListOfGrafs[0])
        # print("Broj grana koje treba izbaciti", SelfReg.minusGraneList)
        print("Grane koje treba izbaciti da bi graf bio klasterabilan" , SelfReg.minusGraneList)
        grafPosleIzbacivanja = izbaciMinusGrane(antiKoalicijeListOfGrafs, g)
        # print("Graf posle izbacivanja grana koje smetaju")
        # nacrtaj(grafPosleIzbacivanja)

        mapaPosleIzbacivanjaMinusGrana = grafPlusToMap(grafPosleIzbacivanja)
        mapaKompPosleIzbacivanjaMinusGrana = vratiKomponente(mapaPosleIzbacivanjaMinusGrana)
        print("Nakon izbacivanja grana koje smetaju, graf je klasterabilan " ,proveriKoalicije(mapaKompPosleIzbacivanjaMinusGrana, len(mapaKompPosleIzbacivanjaMinusGrana.keys()), grafPosleIzbacivanja))




def ucitajGraf(brojGrafa):
    if brojGrafa == 1:
        g = ucitaj()
        return g
    elif brojGrafa == 2:
        g = ucitaj_neklasterabilan()
        return g
    elif brojGrafa == 3:
        g = nx.tutte_graph()
        g = oznaci_grane_grafa(g)
        return g
    elif brojGrafa == 3:
        g = ucitaj_wiki(path.join(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)), "klase", "wiki-RFA.txt"))
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
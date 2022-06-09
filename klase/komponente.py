from asyncio.windows_events import NULL
import networkx as nx
from itertools import chain
from msilib.schema import SelfReg
import sys
from rucniGraf import ucitaj_klasterabilan, ucitaj_klasterabilan
from rucniGraf import ucitaj_neklasterabilan
from nacrtaj import nacrtaj
import random
import itertools

sys.setrecursionlimit(1000000)



SelfReg.minusGrane ={}
SelfReg.minusGraneList = []
SelfReg.brojac = 0
    
def vratiKomponente(g):
    mapaKomp = {}
    for c in g.nodes:
        if c not in list(chain(*list(mapaKomp.values()))) :
            lista = []
            lista.append(c)
            for komsija in list(g.neighbors(c)):
                if komsija not in lista:
                    if g.get_edge_data(c,komsija)['znak'] == "+" :
                        lista.append(komsija)
                        lista = rek(lista, komsija, g)
            mapaKomp[c] = lista
            # print(mapaKomp[c])
            lista = []
    # print("kraj")
    return mapaKomp

def rek (lista, komsija, g):
    for k in list(g.neighbors(komsija)):
        if k not in lista:
            if g.get_edge_data(komsija,k)['znak'] == "+" :
                lista.append(k) 
                rek(lista, k, g)
    
    return lista


def proveriKoalicije(mapaKomponenti, g):
    brAnti = 0
    for i in range (0, len(mapaKomponenti.keys())) :
        daLiJeKoalicija = proveriDaLiJeKlasterKoalicija(mapaKomponenti[list(mapaKomponenti.keys())[i]], g)
        if daLiJeKoalicija =="nije koalicija":
            brAnti = brAnti + 1
    return brAnti
            

def proveriDaLiJeKlasterKoalicija(elementiKlastera, g):
    for a, b in itertools.combinations(elementiKlastera, 2):
        if g.has_edge(a, b):
            z = g.get_edge_data(a, b)['znak']
            if z=="-" : return "nije koalicija"
    return "je koalicija"


def vratiGrafoveAntiKoalicija(mapaKomponenti, n, g):
    grafovi = []
    for i in range (0, n) :
        elementiKlastera = mapaKomponenti[list(mapaKomponenti.keys())[i]]
        graf = vratiGrafAntikoalicije(elementiKlastera, g)
        if graf is not None:
            grafovi.append(graf)
            SelfReg.minusGraneList.append(SelfReg.minusGrane)
    return grafovi

def vratiGrafAntikoalicije (elementiKlastera, g):
    for a, b in itertools.combinations(elementiKlastera, 2):
        if g.has_edge(a, b):
            z = g.get_edge_data(a, b)['znak']
            if z=="-" :  
                    g2 = kreirajGrafKlastera(elementiKlastera, g)
                    return g2

def kreirajGrafKlastera(elementiKlastera, g):
    g2 = nx.Graph()
    for a, b in itertools.combinations(elementiKlastera, 2):
        if g.has_edge(a, b):
            z = g.get_edge_data(a, b)['znak']
            g2.add_node(a)
            g2.add_node(b)
            g2.add_edge(a, b, znak=z)
            if z=="-" :  
                SelfReg.minusGrane[SelfReg.brojac]=[a, b]
                SelfReg.brojac = SelfReg.brojac + 1
    return g2
        

def izbaciMinusGrane(antiKoalicijeListOfGrafs, g):

    grafNovi = g.copy()

    for i in range (0, len(antiKoalicijeListOfGrafs)):

        for j in range(0, len(SelfReg.minusGrane)):
            if antiKoalicijeListOfGrafs[i].has_edge(SelfReg.minusGrane[j][0], SelfReg.minusGrane[j][1]) :
                grafNovi.remove_edge(SelfReg.minusGrane[j][0], SelfReg.minusGrane[j][1])        

    return grafNovi


def oznaci_grane_grafa(grafNovi):
    grafNovi.edges(data=True)
    nx.set_edge_attributes(grafNovi, "+", "znak")
    epsilon = 0.33
    for (u, v) in grafNovi.edges():
        if random.uniform(0, 1) < epsilon:
            grafNovi.add_edge(u, v, znak="-")
    return grafNovi


        




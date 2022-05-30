import networkx as nx
from itertools import chain
from msilib.schema import SelfReg
import sys
sys.setrecursionlimit(10000)



SelfReg.minusGrane ={}
SelfReg.minusGraneList = []

# def vratiKomponente(map):
    
#     komp = []
#     kompMap = {}
#     mapToList = list()

    
#     for i in range (list(map.keys())[0],list(map)[-1]+1):

#         mapToList = list(kompMap.values())
#         if i not in list(chain(*list(mapToList))) :
#             komp.append(i)
#             kompMap[i]=komp
#             for j in range(0,len(map[i])):
#                 if map[i][j] not in komp :
#                     komp.append(map[i][j])
#                     komp = bfs(komp, map[i][j], map)
#             kompMap[i]=komp
#             komp=[]
#     return kompMap
def vratiKomponente(map):
    
    komp = []
    kompMap = {}
    mapToList = list()

    
    for i in list(map.keys()):

        mapToList = list(kompMap.values())
        if i not in list(chain(*list(mapToList))) :
            komp.append(i)
            kompMap[i]=komp
            for j in range(0,len(map[i])):
                if map[i][j] not in komp :
                    komp.append(map[i][j])
                    komp = bfs(komp, map[i][j], map)
            kompMap[i]=komp
            komp=[]
    return kompMap
    

def bfs(komp, broj, map):
    for i in range (0, len(map[broj])):
        if map[broj][i] not in komp:
            komp.append(map[broj][i])
            komp = bfs(komp, map[broj][i], map)
    return komp


def proveriKoalicije(mapaKomponenti, n, g):
    for i in range (0, n) :
        daLiJeKoalicija = proveriDaLiJeKlasterKoalicija(mapaKomponenti[list(mapaKomponenti.keys())[i]], g)
        if daLiJeKoalicija =="nije koalicija":
            return False
    return True
            

def proveriDaLiJeKlasterKoalicija(elementiKlastera, g):
    
    for i in range (0, len(elementiKlastera)):
        for j in range(1, len(elementiKlastera)) :
            if i>=j : continue
            if g.has_edge(elementiKlastera[i], elementiKlastera[j]):
                z = g.get_edge_data(elementiKlastera[i], elementiKlastera[j])['znak']
                if z=="-" : return "nije koalicija"
    return "je koalicija"


def vratiGrafoveAntiKoalicija(mapaKomponenti, n, g):
    grafovi = []

    minusGrane={}
    for i in range (0, n) :
        graf = vratiAntikoalicije(mapaKomponenti[list(mapaKomponenti.keys())[i]], g)
        if graf is not None:
            grafovi.append(graf)
            SelfReg.minusGraneList.append(SelfReg.minusGrane)
    return grafovi

def vratiAntikoalicije (elementiKlastera, g):
    antiMap = {}
    antiList = []
    minusGrane = {}

    for i in range (0, len(elementiKlastera)):
        for j in range(1, len(elementiKlastera)) :
            if i>=j : continue
            if g.has_edge(elementiKlastera[i], elementiKlastera[j]):
                z = g.get_edge_data(elementiKlastera[i], elementiKlastera[j])['znak']
                if z=="-" :  
                    g2 = kreirajKlaster(elementiKlastera, g)
                    return g2
                   



def kreirajKlaster(elementiKlastera, g):
    g2 = nx.Graph()

    brojac = 0
    for i in range (0, len(elementiKlastera)):
        for j in range(1, len(elementiKlastera)) :
            if i>=j : continue
            if g.has_edge(elementiKlastera[i], elementiKlastera[j]):
                z = g.get_edge_data(elementiKlastera[i], elementiKlastera[j])['znak']
                g2.add_node(elementiKlastera[i])
                g2.add_node(elementiKlastera[j])
                g2.add_edge(elementiKlastera[i], elementiKlastera[j], znak=z)

                if z == '-':
                    SelfReg.minusGrane[brojac]=[elementiKlastera[i],elementiKlastera[j]]
                    brojac = brojac + 1
    # print("grane koje treba izbaciti " , SelfReg.minusGrane)
    return g2  
        

def izbaciMinusGrane(antiKoalicijeListOfGrafs, g):
    for i in range (0, len(antiKoalicijeListOfGrafs)):

        for j in range(0, len(SelfReg.minusGrane)):
            if antiKoalicijeListOfGrafs[i].has_edge(SelfReg.minusGrane[j][0], SelfReg.minusGrane[j][1]) :
                g.remove_edge(SelfReg.minusGrane[j][0], SelfReg.minusGrane[j][1])

    return g

        




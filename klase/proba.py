from msilib.schema import SelfReg
import networkx as nx
from itertools import chain
from os import path
import os
from nacrtaj import nacrtaj


SelfReg.minusGrane ={}
SelfReg.minusGraneList = []


def ucitaj_wiki(putanja):

    graf = nx.Graph()
    graf.add_node(1)
    graf.add_node(2)
    graf.add_node(3)

    graf.add_edge(1,3)
    graf.add_edge(2,3)
    graf.add_edge(1,2)
    print(len(graf.edges))

#     file = open(putanja, "r", encoding="utf8")
#     graf_wiki= nx.DiGraph()
#     linije = file.read().splitlines()
#     cvor_A = None
#     cvor_B = None
#     for line in linije:
#         if line.startswith("SRC"):
#             cvor_A = line.split(":")[1]
#         if line.startswith("TGT"):
#             cvor_B = line.split(":")[1]
#         if line.startswith("RES"):
#             znak = line.split(":")[1]
#             if znak == "1":
#                 znak = "+"
#             else:
#                 znak = "-"
#             graf_wiki.add_edge(cvor_A, cvor_B, znak=znak)

#     print(list(graf_wiki.neighbors("Mika")))

#     # print(graf_wiki.edges(data=True))
#     graf = pretvori_u_neusmeren(graf_wiki)
    

#     # print(graf_wiki.edges(data=True))
#     print('---------------------------')

#     # print(list(map.keys()))
#     mapaPlus = grafPlusToMap(graf)
#     # print(mapaPlus)
#     mapaKomponenti = vratiKomponente(mapaPlus)
#     # print(mapaKomponenti)

#     daLiJeKlasterabilan = proveriKoalicije(mapaKomponenti, len(mapaKomponenti.keys()), graf)

#     antiKoalicijeListOfGrafs = []

#     if daLiJeKlasterabilan==True :
#         print("Graf je klasterabilan")
#         print("Graf za {}. koaliciju ce biti prikazan".format(2))
#         nacrtaj(kreirajKlaster(mapaKomponenti[list(mapaKomponenti.keys())[1]], graf))
        
#     else :
#         print("Graf nije klasterabilan")
#         antiKoalicijeListOfGrafs = vratiGrafoveAntiKoalicija(mapaKomponenti, len(mapaKomponenti.keys()),graf)
#         for i in range (0,len(antiKoalicijeListOfGrafs)):
#             print("Cvorovi {}. antiKoalicije".format(i),antiKoalicijeListOfGrafs[i].edges(data=True))

#         if antiKoalicijeListOfGrafs:
#             print("Graf antikoalicija")
#             nacrtaj(antiKoalicijeListOfGrafs[0])

#         print("Grane koje treba izbaciti da bi graf bio klasterabilan" , SelfReg.minusGraneList)
#         grafPosleIzbacivanja = izbaciMinusGrane(antiKoalicijeListOfGrafs, graf)
#         print("Graf posle izbacivanja grana koje smetaju")
#         nacrtaj(graf)


    

#     # print("komsija",list(graf_wiki.neighbors("Steel1943")))
#     # mapPlus = {}
    
#     # for u, v, d in graf_wiki.edges(data=True):
#     #     komsije = list(graf_wiki.neighbors(u))
    


# def pretvori_u_neusmeren(graf):
#     usmeren_graf = nx.Graph()
#     usmeren_graf.add_edges_from(graf.edges(), znak="")
#     for u, v, d in graf.edges(data=True):
#         znak1 = graf[u][v]['znak']
#         znak2 = ""
#         if (v, u) in graf.edges:
#             znak2 = graf[v][u]['znak']
#         if znak1 == "-" or znak2 == "-":
#             usmeren_graf[u][v]['znak'] = "-"
#         else:
#             usmeren_graf[u][v]['znak'] = "+"
#     print("Zavrseno ucitavanje!")
#     return usmeren_graf


# def grafPlusToMap(graf):
#     mapa = {}
#     komsije = []
#     komsijePlus = []
    
#     for ime in graf.nodes :
#         # print(ime)
#         # print("Komsije za {} :".format(ime),list(graf.neighbors(ime)))
#         for komsija in list(graf.neighbors(ime)):
#             if graf.get_edge_data(ime,komsija)['znak'] == "+" :
#                 komsije.append(komsija)
#         mapa[ime]=komsije
#         komsije = []

#     return mapa
    
# def vratiKomponente(map):
    
#     komp = []
#     kompMap = {}
#     mapToList = list()

    
#     for i in list(map.keys()):

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

# def bfs(komp, broj, map):
#     for i in range (0, len(map[broj])):
#         if map[broj][i] not in komp:
#             komp.append(map[broj][i])
#             komp = bfs(komp, map[broj][i], map)
#     return komp

# def proveriKoalicije(mapaKomponenti, n, g):
#     for i in range (0, n) :
#         daLiJeKoalicija = proveriDaLiJeKlasterKoalicija(mapaKomponenti[list(mapaKomponenti.keys())[i]], g)
#         if daLiJeKoalicija =="nije koalicija":
#             return False
#     return True

# def proveriDaLiJeKlasterKoalicija(elementiKlastera, g):
    
#     for i in range (0, len(elementiKlastera)):
#         for j in range(1, len(elementiKlastera)) :
#             if i>=j : continue
#             if g.has_edge(elementiKlastera[i], elementiKlastera[j]):
#                 z = g.get_edge_data(elementiKlastera[i], elementiKlastera[j])['znak']
#                 if z=="-" : return "nije koalicija"
#     return "je koalicija"




# def vratiGrafoveAntiKoalicija(mapaKomponenti, n, g):
#     grafovi = []

#     minusGrane={}
#     for i in range (0, n) :
#         graf = vratiAntikoalicije(mapaKomponenti[list(mapaKomponenti.keys())[i]], g)
#         if graf is not None:
#             grafovi.append(graf)
#             SelfReg.minusGraneList.append(SelfReg.minusGrane)
#     return grafovi

# def vratiAntikoalicije (elementiKlastera, g):
#     antiMap = {}
#     antiList = []
#     minusGrane = {}

#     for i in range (0, len(elementiKlastera)):
#         for j in range(1, len(elementiKlastera)) :
#             if i>=j : continue
#             if g.has_edge(elementiKlastera[i], elementiKlastera[j]):
#                 z = g.get_edge_data(elementiKlastera[i], elementiKlastera[j])['znak']
#                 if z=="-" :  
#                     g2 = kreirajKlaster(elementiKlastera, g)
#                     return g2
                   



# def kreirajKlaster(elementiKlastera, g):
#     g2 = nx.Graph()

#     brojac = 0
#     for i in range (0, len(elementiKlastera)):
#         for j in range(1, len(elementiKlastera)) :
#             if i>=j : continue
#             if g.has_edge(elementiKlastera[i], elementiKlastera[j]):
#                 z = g.get_edge_data(elementiKlastera[i], elementiKlastera[j])['znak']
#                 g2.add_node(elementiKlastera[i])
#                 g2.add_node(elementiKlastera[j])
#                 g2.add_edge(elementiKlastera[i], elementiKlastera[j], znak=z)

#                 if z == '-':
#                     SelfReg.minusGrane[brojac]=[elementiKlastera[i],elementiKlastera[j]]
#                     brojac = brojac + 1
#     # print("grane koje treba izbaciti " , SelfReg.minusGrane)
#     return g2  
        

# def izbaciMinusGrane(antiKoalicijeListOfGrafs, g):
#     for i in range (0, len(antiKoalicijeListOfGrafs)):

#         for j in range(0, len(SelfReg.minusGrane)):
#             if antiKoalicijeListOfGrafs[i].has_edge(SelfReg.minusGrane[j][0], SelfReg.minusGrane[j][1]) :
#                 g.remove_edge(SelfReg.minusGrane[j][0], SelfReg.minusGrane[j][1])

#     return g

        



# vratiBrojKomponenti()
ucitaj_wiki(path.join(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)), "klase", "fajl.txt"))





           
       



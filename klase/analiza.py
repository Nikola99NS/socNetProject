from asyncio.windows_events import NULL
from nacrtaj import nacrtaj
from os import path
import os
import networkx as nx


def prosecanStepenGrafa(graf):
    sum = 0
    for cvor in graf.nodes:
        sum += graf.degree(cvor)
    return sum*1.0/len(graf.nodes)




def prosecanStepenKomponenti(elementiKompontente, graf, gListAnti ):
    if gListAnti is not NULL:
        prosekJednog = 0
        prosek = 0
        sum = 0 
        for i in gListAnti:
            for c in  i.nodes:
                sum += graf.degree(c)
            prosekJednog = sum*1.0/len(i)
            sum = 0
            prosek = prosek + prosekJednog
            prosekJednog = 0
        return prosek / len(gListAnti)
    else :
        sum = 0
        for cvor in elementiKompontente:
            sum += graf.degree(cvor)
        return sum*1.0/(len(elementiKompontente))


def prosecanDijametar(listOfGrafs):
    sum=0
    for g in listOfGrafs:
        sum = sum + nx.diameter(g)

    return sum/len(listOfGrafs)
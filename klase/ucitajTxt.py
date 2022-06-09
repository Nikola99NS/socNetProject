from asyncio.windows_events import NULL
from calendar import c
from contextlib import nullcontext
import networkx as nx
import csv


def ucitaj_wiki(putanja):

    
    file = open(putanja, "r", encoding="utf8")
    graf_wiki= nx.DiGraph()
    linije = file.read().splitlines()
    cvor_A = None
    cvor_B = None
    for line in linije:
        if line.startswith("SRC"):
            cvor_A = line.split(":")[1]
        if line.startswith("TGT"):
            cvor_B = line.split(":")[1]
        if line.startswith("RES"):
            znak = line.split(":")[1]
            if znak == "1":
                znak = "+"
            else:
                znak = "-"
            graf_wiki.add_edge(cvor_A, cvor_B, znak=znak)
    
    graf = pretvori_u_neusmeren(graf_wiki)

    return graf



def ucitaj_slashdot(putanja):
    brojac = 0
    file = open(putanja, "r", encoding="utf8")
    linije = file.read().splitlines()
    cvor_A = None
    cvor_B = None
    graf = nx.DiGraph()
    for line in linije:
        brojac = brojac + 1
        if line.startswith("#"):
            continue
        line = line.split("\t")
        if "-1" in line[2]:
            znak = "-"
            cvor_A = line[0]
            cvor_B = line[1]
        else:
            znak = "+"
            cvor_A = line[0]
            cvor_B = line[1]
        # element = (line[0].strip(), line[1].strip(), {'znak': znak})
        graf.add_edge(cvor_A, cvor_B, znak=znak)
        if brojac == 100000:
            return pretvori_u_neusmeren(graf)
    
    return pretvori_u_neusmeren(graf)


def pretvori_u_neusmeren(graf):
    usmeren_graf = nx.Graph()
    usmeren_graf.add_edges_from(graf.edges(), znak="")
    for u, v, d in graf.edges(data=True):
        znak1 = graf[u][v]['znak']
        znak2 = ""
        if (v, u) in graf.edges:
            znak2 = graf[v][u]['znak']
        if znak1 == "-" or znak2 == "-":
            usmeren_graf[u][v]['znak'] = "-"
        else:
            usmeren_graf[u][v]['znak'] = "+"
    return usmeren_graf


def ucitaj_epinions(putanja):
    graf_epinions = nx.DiGraph()
    with open(putanja, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if int(row[2]) > 0:
                znak = "+"
            else:
                znak = "-"
            graf_epinions.add_edge(row[0], row[1], znak=znak)
    csv_file.close()
    return pretvori_u_neusmeren(graf_epinions)
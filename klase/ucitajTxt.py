import networkx as nx

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
    print("Zavrseno ucitavanje!")
    return usmeren_graf
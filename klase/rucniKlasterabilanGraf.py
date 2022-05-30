import networkx as nx

def ucitaj():
 
    g = nx.Graph()

    for i in range(1,16):
        g.add_node(i)
    
    g.add_edge(1, 2, znak="+")
    g.add_edge(1, 3, znak="+")   

    g.add_edge(2, 3, znak="+") 
    g.add_edge(2, 4, znak="-") 
    g.add_edge(2, 5, znak="+")

    g.add_edge(3, 6, znak="-")

    g.add_edge(4, 7, znak="+")
    g.add_edge(4,9, znak="-")

    g.add_edge(5, 6, znak="-")
    
    g.add_edge(6, 8, znak="+")
    g.add_edge(6, 11, znak="-")

    g.add_edge(7,12, znak="+")
    
    g.add_edge(8, 11, znak="-")
    
    g.add_edge(9, 12, znak="+")

    g.add_edge(10, 11, znak="-")
    g.add_edge(10, 12, znak="+")

    g.add_edge(11, 13, znak="-")
    g.add_edge(11, 14, znak="-")

    g.add_edge(12, 13, znak="+")

    g.add_edge(13, 15, znak="-")

    g.add_edge(14, 15, znak="-")


     

    

    return g

def ucitaj_neklasterabilan():
    graf = nx.Graph()
    nx.set_edge_attributes(graf, "+", "znak")
    for i in range(1, 21):
        graf.add_node(i)
        
    graf.add_edge(1, 2, znak="+")
    graf.add_edge(2, 3, znak="+")
    graf.add_edge(3, 4, znak="+")
    graf.add_edge(4, 5, znak="+")
    graf.add_edge(5, 6, znak="+")
    graf.add_edge(6, 7, znak="-")
    graf.add_edge(6, 8, znak="+")
    graf.add_edge(7, 8, znak="-")
    graf.add_edge(1, 4, znak="-")

    graf.add_edge(9, 10, znak="+")
    graf.add_edge(10, 11, znak="+")
    graf.add_edge(11, 12, znak="+")
    graf.add_edge(12, 13, znak="+")
    graf.add_edge(13, 14, znak="+")
    graf.add_edge(14, 15, znak="+")
    graf.add_edge(14, 16, znak="+")
    graf.add_edge(14, 11, znak="+")
    graf.add_edge(14, 12, znak="+")
    
    graf.add_edge(17, 18, znak="+")
    graf.add_edge(18, 19, znak="+")
    graf.add_edge(19, 20, znak="+")
    graf.add_edge(20, 17, znak="+")
    graf.add_edge(20, 18, znak="+")
    
    graf.add_edge(1, 20, znak="-")
    graf.add_edge(2, 20, znak="-")
    graf.add_edge(7, 20, znak="-")
    graf.add_edge(4, 14, znak="-")
    graf.add_edge(5, 14, znak="-")
    graf.add_edge(4, 14, znak="-")
    graf.add_edge(14, 20, znak="-")
    graf.add_edge(15, 20, znak="-")
    
    return graf

ucitaj()

import networkx as nx
import matplotlib.pyplot as plt

# #metoda za iscrtavanje malog grafa
# def nacrtaj_mali(G, title):
#     nacrtaj(G, title, False)


# #metoda za iscrtavanje velikog grafa
# def nacrtaj_veliki(G, title):
#     nacrtaj(G, title, True)
    
def nacrtaj(graf):
    # if velika:
    #     pozicija = nx.circular_layout(graf)
    # else:
    pozicija = nx.circular_layout(graf)
    nx.draw_networkx_labels(graf, pozicija, font_weight='bold')
    nx.draw_networkx_nodes(graf.nodes, pos = pozicija, label=True, node_color= 'red')
    e_plus = [(u, v) for (u, v, d) in graf.edges(data=True) if d['znak'] == "+"]
    e_minus = [(u, v) for (u, v, d) in graf.edges(data=True) if d['znak'] == "-"]
    nx.draw_networkx_edges(graf, pozicija, edgelist = e_plus, width=3.0, edge_color='blue')
    nx.draw_networkx_edges(graf, pozicija, edgelist = e_minus, width=2.0, edge_color= 'blue', style='dashed')
    # plt.title(title)
    plt.show()
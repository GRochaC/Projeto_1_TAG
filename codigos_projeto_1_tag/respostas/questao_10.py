import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import cm
from main import grafo
from respostas import questao_9

def solve():
    # Para cada clique do grafo, é dado um identificador para cada vértice pertencente aquele clique
    cliques = {}
    id_clique = 0
    for clique in questao_9.cliques_maximais:
        add = False
        for v in clique:    
            if v not in cliques: 
                cliques[v] = id_clique
                add = True

        if add: id_clique += 1

    # Visualização dos cliques do grafo
    clq = [cliques[v] for v in grafo]

    cor = cm.get_cmap("Pastel2", id_clique+1)

    nx.draw_spring(grafo, cmap = cor, node_color = clq, edge_color = "gray")
    plt.show()

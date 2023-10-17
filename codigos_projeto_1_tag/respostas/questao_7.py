import networkx as nx
from cdlib import algorithms
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from main import grafo
from respostas import questao_5, questao_6

def solve():
    # Visualização do grafo color-coded da comunidade de Louvain
    comunidades = questao_5.comunidades_louvain.to_node_community_map()
    comunidades = [comunidades[v].pop() for v in grafo]

    cor = cm.get_cmap("Pastel2", max(comunidades)+1)

    np.random.seed(123)
    nx.draw_spring(grafo, cmap = cor, node_color = comunidades, edge_color = "gray")
    plt.show()

    # Visualização do grafo color-coded dos departamentos "ground truth"
    depts = [questao_6.dicio[v] for v in grafo]

    cor = cm.get_cmap("Pastel2", len(questao_6.departamentos)+1)

    nx.draw_spring(grafo, cmap = cor, node_color = depts, edge_color = "gray")
    plt.show()

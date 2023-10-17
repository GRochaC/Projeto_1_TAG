import networkx as nx
import pandas as pd
from cdlib import algorithms
from main import grafo

def solve():
    return df_l

# Usa o algoritmo de Louvain para determinar a estrutura de comunidade com modularidade ótima
comunidades_louvain = algorithms.louvain(grafo)
df_l = pd.DataFrame(comunidades_louvain.communities).transpose()

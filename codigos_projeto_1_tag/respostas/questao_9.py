import networkx as nx
from main import grafo

def solve():
    return max_clique, num_max_clique

# Encontra o clique máximo do grafo
max_clique = nx.graph_clique_number(grafo)
print(f"Clique máximo: {max_clique}")

# Obtém todos os cliques do grafo
cliques = nx.find_cliques(grafo)
cliques_maximais = sorted(cliques, key = len, reverse = True)

# Procura pelos cliques de tamanho máximo
num_max_clique = 0
for clique in cliques_maximais: 
    if len(clique) == max_clique: num_max_clique += 1
import networkx as nx

def solve(grafo):
    # Obtem os componentes conexos do grafo
    comp_conexos = nx.connected_components(grafo)

    # Obtem os subgrafos a partir dos componentes conexos
    subgrafos = [grafo.subgraph(componente).copy() for componente in comp_conexos]

    # Inicializa o maior componente conexo e seu tamanho
    maior_comp_conexo, maior_tam = None, 0

    # Procura o maior componente conexo dentre todos os subgrafos
    for subgrafo in subgrafos:
        if len(subgrafo) > maior_tam:
            maior_tam = len(subgrafo)
            maior_comp_conexo = subgrafo

    return maior_comp_conexo


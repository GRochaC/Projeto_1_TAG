import pandas as pd
import networkx as nx

# Lê da planilha as arestas e vértices do grafo
tabela_arestas = pd.read_csv("https://ona-book.org/data/email_edgelist.csv")
tabela_vertices = pd.read_csv("https://ona-book.org/data/email_vertices.csv")

# Cria um grafo não-direcionado a partir das planilhas
grafo = nx.from_pandas_edgelist(
    tabela_arestas,
    source = "from",
    target = "to"
)

if __name__ == "__main__":
    from respostas import *

    # Questão 4
    print(f"Maior componente conexo do grafo: {questao_4.solve(grafo)}")

    # Questao 5
    print(questao_5.solve())

    # Questao 6
    print(questao_6.solve())

    # Questao 7
    questao_7.solve()

    # Questao 8
    print(questao_8.solve())
    questao_8.show_heatmap()

    # Questao 9
    max_clique, num_max_clique = questao_9.solve()
    print(f"Quantidade de cliques de tamanho {max_clique}: {num_max_clique}")

    #Questao 10
    questao_10.solve()
import pandas as pd
import networkx
from main import grafo
from respostas import questao_5, questao_6

def solve():
    return df_porcentagem

def show_heatmap():
    # Visualização da tabela usando um heatmap
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    sns.heatmap(df_porcentagem, annot = True, cmap = "YlGnBu")
    plt.title("Mapa de calor Departamento x Comunidade, em %")
    plt.xlabel("Comunidade")
    plt.ylabel("Departamento")
    plt.show()

matriz = []
com = questao_5.comunidades_louvain.to_node_community_map()
for no in grafo:
    matriz.append([com[no].pop(), questao_6.dicio[no]])

df_com_dept = pd.DataFrame(matriz,columns = ["Comunidade","Departamento"])
print(df_com_dept)

matriz = []
for i in range(questao_5.df_l.shape[1]):
    matriz.append([0.0] * questao_6.df_dept.shape[1])

for i,row in df_com_dept.iterrows():
    c = row["Comunidade"]
    d = row["Departamento"]
    matriz[c][d] += (1/df_com_dept.shape[0])*100

df_porcentagem = pd.DataFrame(matriz).transpose()
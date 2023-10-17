import pandas as pd
from main import tabela_vertices

def solve():
    return df_dept

departamentos, dicio = {}, {}

# Agrupa todos os vértices do grafo em seus respectivos departamentos
for i, row in tabela_vertices.iterrows():
    id = row["id"]
    dept = row["dept"]

    if dept not in departamentos.keys(): departamentos[dept] = [id]
    else: departamentos[dept].append(id)
        
    dicio[id] = dept

# Cria uma matriz de M colunas, onde M é o número de departamentos
matriz = []
for i in range(len(departamentos)): matriz.append([])
# Popula a matriz com seus respectivos valores
for dept, lista_id in departamentos.items():
    for id in lista_id:
        matriz[dept].append(id)

df_dept = pd.DataFrame(matriz).transpose()
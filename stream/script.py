import os
import pandas as pd

dataframe_bus = pd.read_csv("./buses.csv", chunksize=500000)

dataframe_pararutas = pd.read_csv("./paraderosrutas.csv", chunksize=500000)

group_chunks = []
for chunk_number, chunk in enumerate(dataframe_bus):
    if chunk_number > 1:
        break
    print(f'Chunk number {chunk_number + 1} \r')
    row_chunks = chunk.iterrows()
    temp = chunk.groupby(['vendor', 'bus'], group_keys=True, as_index=True).apply(lambda x: x)
    group_chunks.append(temp)
result = pd.concat(group_chunks)

#print(type(result.index))
#print(result.index.names)
#print(result.index.values)
#print(result.index.levels)

[rutas, micros, _] = result.index.levels

# Ejemplo de acceso a filas por ruta --> result.loc["T101"]

# Ejemplo de acceso a filas por ruta y bus --> result.loc["T101","BJFD-18"]

# Ejemplo de convertir uno de los elementos anteriores (o columna de estos) en una lista normal de python --> result.loc["T101","BJFD-18"]["velocidad"].tolist()

print(len(rutas))

print(result.loc["T101"]["pasajeros"])





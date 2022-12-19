import os
import pandas as pd
from datetime import datetime
import numpy as np
#*************************
'''

- Calcular o Agrupar inicio y fin de un bus en un paradero
- Calcular la media de tiempo de un bus en un paradero
- Seperar el dataframe en intervalos de tiempo segun hora, tipo valle, punta, etc

- 1 Hora cuantos buses hay en un paradero. #CHECK

PUNTA: 7:00 a 8:59 - 18:00 a 19:59
VALLE: 9:00 a 17:59 - 20:00 a 20:44
BAJO: 0:00 a 6:59 - 20:45 a 23:59

'''
csv = ['510I','D03I','D08I','D18I','B13I']
arr_data_frec = list()
arr_data_regularidad = list()
arr_data_regularidad_t = list()
#*************************
for i in range(len(csv)):
    arr_data_frec.append(pd.read_csv("./"+csv[i]+"/"+csv[i]+"Frecuencia.csv"))
    arr_data_regularidad.append(pd.read_csv("./"+csv[i]+"/"+csv[i]+"Regularidad ALL.csv"))
    arr_data_regularidad_t.append(pd.read_csv("./"+csv[i]+"/"+csv[i]+"Regularidad Tiempos.csv"))


df_frec = pd.concat(arr_data_frec,keys=['114I','211I','104I'],ignore_index=True)
df_regularidad = pd.concat(arr_data_regularidad)
df_regularidad_t = pd.concat(arr_data_regularidad_t)

df_frec.to_csv("./DATA/Frecuencia.csv")
df_regularidad.to_csv("./DATA/Regularidad.csv")
df_regularidad_t.to_csv("./DATA/Regularidad Tiempos.csv")

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
#*************************
def H_Punta(data_k,geo,geo_lat,geo_lon,dataframe_buses,n,S):
    #HORA PUNTA
    Hora_PUNTA = ['2018-06-13 07:00:00+00','2018-06-13 08:59:59+00','2018-06-13 18:00:00+00','2018-06-13 19:59:59+00']
    df_sh = data_k
    if S == 'S1':
        df_sh = data_k[(data_k['fechahora'] >= Hora_PUNTA[0]) & (data_k['fechahora'] <= Hora_PUNTA[1])]
    elif S == 'S2':
        df_sh = data_k[(data_k['fechahora'] >= Hora_PUNTA[2]) & (data_k['fechahora'] <= Hora_PUNTA[3])]
    data_ord = df_sh.sort_values(by=['fechahora'])
    data_ord['fechahora'] = pd.to_datetime(data_ord['fechahora'], infer_datetime_format=True)
    date_list = data_ord['fechahora'].tolist()
    dif_times = []

    for k in range(len(date_list)):
        if k > 0:
            dif_times.append((date_list[k]-date_list[k-1]).total_seconds())

    mean = np.mean(dif_times)
    dataframe_buses['paradero'].append(n)
    dataframe_buses['tiempo_promedio'].append(mean)
    dataframe_buses['geo_parader'].append(geo)
    dataframe_buses['geo_parader_lat'].append(geo_lat)
    dataframe_buses['geo_parader_lon'].append(geo_lon)
    dataframe_buses['zona_h'].append('Punta')
    dataframe_buses['zona_h_num'].append(1)
    dataframe_buses['seccion'].append(S)
    if mean < 600:
        dataframe_buses['calificacion'].append(2)
    elif mean == 600:
        dataframe_buses['calificacion'].append(1)
    else:
        dataframe_buses['calificacion'].append(0)

    return dataframe_buses

def H_Valle(data_k,geo,geo_lat,geo_lon,dataframe_buses,n,S):
    #HORA VALLE
    Hora_VALLE = ['2018-06-13 09:00:00+00','2018-06-13 17:59:59+00','2018-06-13 20:00:00+00','2018-06-13 20:44:59+00']
    df_sh = data_k
    if S == 'S1':
        df_sh = data_k[(data_k['fechahora'] >= Hora_VALLE[0]) & (data_k['fechahora'] <= Hora_VALLE[1])]
    elif S == 'S2':
        df_sh = data_k[(data_k['fechahora'] >= Hora_VALLE[2]) & (data_k['fechahora'] <= Hora_VALLE[3])]
    data_ord = df_sh.sort_values(by=['fechahora'])
    data_ord['fechahora'] = pd.to_datetime(data_ord['fechahora'], infer_datetime_format=True)
    date_list = data_ord['fechahora'].tolist()
    dif_times = []

    for k in range(len(date_list)):
        if k > 0:
            dif_times.append((date_list[k]-date_list[k-1]).total_seconds())

    mean = np.mean(dif_times)
    dataframe_buses['paradero'].append(n)
    dataframe_buses['tiempo_promedio'].append(mean)
    dataframe_buses['geo_parader'].append(geo)
    dataframe_buses['geo_parader_lat'].append(geo_lat)
    dataframe_buses['geo_parader_lon'].append(geo_lon)
    dataframe_buses['zona_h'].append('Valle')
    dataframe_buses['zona_h_num'].append(2)
    dataframe_buses['seccion'].append(S)
    if mean < 600:
        dataframe_buses['calificacion'].append(2)
    elif mean == 600:
        dataframe_buses['calificacion'].append(1)
    else:
        dataframe_buses['calificacion'].append(0)

    return dataframe_buses
def H_Bajo(data_k,geo,geo_lat,geo_lon,dataframe_buses,n,S):
    #HORA BAJO
    Hora_BAJO = ['2018-06-13 00:00:00+00','2018-06-13 06:59:00+00','2018-06-13 20:45:00+00','2018-06-13 23:59:59+00']
    df_sh = data_k
    if S == 'S1':
        df_sh = data_k[(data_k['fechahora'] >= Hora_BAJO[0]) & (data_k['fechahora'] <= Hora_BAJO[1])]
    elif S == 'S2':
        df_sh = data_k[(data_k['fechahora'] >= Hora_BAJO[2]) & (data_k['fechahora'] <= Hora_BAJO[3])]
    data_ord = df_sh.sort_values(by=['fechahora'])
    data_ord['fechahora'] = pd.to_datetime(data_ord['fechahora'], infer_datetime_format=True)
    date_list = data_ord['fechahora'].tolist()
    dif_times = []

    for k in range(len(date_list)):
        if k > 0:
            dif_times.append((date_list[k]-date_list[k-1]).total_seconds())

    mean = np.mean(dif_times)
    dataframe_buses['paradero'].append(n)
    dataframe_buses['tiempo_promedio'].append(mean)
    dataframe_buses['geo_parader'].append(geo)
    dataframe_buses['geo_parader_lat'].append(geo_lat)
    dataframe_buses['geo_parader_lon'].append(geo_lon)
    dataframe_buses['zona_h'].append('Bajo')
    dataframe_buses['zona_h_num'].append(3)
    dataframe_buses['seccion'].append(S)
    if mean < 600:
        dataframe_buses['calificacion'].append(2)
    elif mean == 600:
        dataframe_buses['calificacion'].append(1)
    else:
        dataframe_buses['calificacion'].append(0)

    return dataframe_buses

def H_All(data_k,geo,geo_lat,geo_lon,dataframe_buses,n):
    data_ord = data_k.sort_values(by=['fechahora'])
    data_ord['fechahora'] = pd.to_datetime(data_ord['fechahora'], infer_datetime_format=True)
    date_list = data_ord['fechahora'].tolist()
    dif_times = []

    for k in range(len(date_list)):
        if k > 0:
            dif_times.append((date_list[k]-date_list[k-1]).total_seconds())

    mean = np.mean(dif_times)
    dataframe_buses['paradero'].append(n)
    dataframe_buses['tiempo_promedio'].append(mean)
    dataframe_buses['geo_parader'].append(geo)
    dataframe_buses['geo_parader_lat'].append(geo_lat)
    dataframe_buses['geo_parader_lon'].append(geo_lon)
    if mean < 600:
        dataframe_buses['calificacion'].append(2)
    elif mean == 600:
        dataframe_buses['calificacion'].append(1)
    else:
        dataframe_buses['calificacion'].append(0)

    return dataframe_buses

#*************************
def getPromRegcBus():#Regularidad
    Hour_list_from = ['2018-06-13 00:00:00+00','2018-06-13 01:00:00+00','2018-06-13 02:00:00+00','2018-06-13 03:00:00+00','2018-06-13 04:00:00+00','2018-06-13 05:00:00+00','2018-06-13 06:00:00+00','2018-06-13 07:00:00+00','2018-06-13 08:00:00+00','2018-06-13 09:00:00+00','2018-06-13 10:00:00+00','2018-06-13 11:00:00+00','2018-06-13 12:00:00+00','2018-06-13 13:00:00+00','2018-06-13 14:00:00+00','2018-06-13 15:00:00+00','2018-06-13 16:00:00+00','2018-06-13 18:00:00+00','2018-06-13 19:00:00+00','2018-06-13 20:00:00+00','2018-06-13 21:00:00+00','2018-06-13 22:00:00+00','2018-06-13 23:00:00+00']
    Hour_list_to = ['2018-06-13 00:59:59+00','2018-06-13 01:59:59+00','2018-06-13 02:59:59+00','2018-06-13 03:59:59+00','2018-06-13 04:59:59+00','2018-06-13 05:59:59+00','2018-06-13 06:59:59+00','2018-06-13 07:59:59+00','2018-06-13 08:59:59+00','2018-06-13 09:59:59+00','2018-06-13 10:59:59+00','2018-06-13 11:59:59+00','2018-06-13 12:59:59+00','2018-06-13 13:59:59+00','2018-06-13 14:59:59+00','2018-06-13 15:59:59+00','2018-06-13 16:59:59+00','2018-06-13 18:59:59+00','2018-06-13 19:59:59+00','2018-06-13 20:59:59+00','2018-06-13 21:59:59+00','2018-06-13 22:59:59+00','2018-06-13 23:59:59+00']




    dataframe_ruta = pd.read_csv("./E04I.csv")
    #temp2 = dataframe_ruta.groupby(['parader'], group_keys=True, as_index=True).apply(lambda x: x)
    temp4 = dataframe_ruta.groupby(['bus'], group_keys=True, as_index=True).apply(lambda x: x)
    #print(temp2)
    #temp4 = dataframe_ruta.groupby(['parder_geom'], group_keys=True, as_index=True).apply(lambda x: x)
    #list_bus = temp2.index.levels[0]

    #temp3 = temp2.loc['PA146']
    list_bus = temp4.index.levels[0]
    #print(list_bus)
    #temp5 = temp4.loc['BJFS-70']
    #a = temp2.loc['PA146']['fechahora'].tolist()[0]
    
    #b = a.sort_values(by=['fechahora'])
    #print(temp3)
    
    #w = temp3.groupby(['bus'], group_keys=True, as_index=True).apply(lambda x: x)
    #temp6 = temp5.sort_values(by=['fechahora'])
    #del temp6['parder_geom']
    #del temp6['nombre_par']
    
    #print(temp6)
    dataframe_list = list()
    for i in list_bus:
        x = temp4.loc[i]
        a = x.sort_values(by=['fechahora'])
        del a['nombre_par']
        #del a['parder_geom']
        for j in range(23):
            #print(j)
            df = a[(a['fechahora'] >= Hour_list_from[j]) & (a['fechahora'] <= Hour_list_to[j])]
            #if i == 'BJFS-70':
                #print(df)
            df_g = df.loc[df.groupby('parader')['d'].idxmin()]
            #if i == 'BJFS-70':
                #print(df_g)
            dataframe_list.append(df_g)


    dataframe_buses = {'paradero':[],'tiempo_promedio':[],'geo_parader':[],'geo_parader_lat':[],'geo_parader_lon':[],'calificacion':[]}
    # ESTAN ASI PORQUE NO SE Q WEA CON LOS PUNTEROS
    dataframe_buses_p1 = {'paradero':[],'tiempo_promedio':[],'geo_parader':[],'geo_parader_lat':[],'geo_parader_lon':[],'calificacion':[],'zona_h':[],'zona_h_num':[],'seccion':[]}
    dataframe_buses_p2 = {'paradero':[],'tiempo_promedio':[],'geo_parader':[],'geo_parader_lat':[],'geo_parader_lon':[],'calificacion':[],'zona_h':[],'zona_h_num':[],'seccion':[]}
    dataframe_buses_v1 = {'paradero':[],'tiempo_promedio':[],'geo_parader':[],'geo_parader_lat':[],'geo_parader_lon':[],'calificacion':[],'zona_h':[],'zona_h_num':[],'seccion':[]}
    dataframe_buses_v2 = {'paradero':[],'tiempo_promedio':[],'geo_parader':[],'geo_parader_lat':[],'geo_parader_lon':[],'calificacion':[],'zona_h':[],'zona_h_num':[],'seccion':[]}
    dataframe_buses_b1 = {'paradero':[],'tiempo_promedio':[],'geo_parader':[],'geo_parader_lat':[],'geo_parader_lon':[],'calificacion':[],'zona_h':[],'zona_h_num':[],'seccion':[]}
    dataframe_buses_b2 = {'paradero':[],'tiempo_promedio':[],'geo_parader':[],'geo_parader_lat':[],'geo_parader_lon':[],'calificacion':[],'zona_h':[],'zona_h_num':[],'seccion':[]}


    dataf = pd.concat(dataframe_list)
    
    data_gp = dataf.groupby(['parader'], group_keys=True, as_index=True).apply(lambda x: x)
    #print(data_gp)
    list_parader = data_gp.index.levels[0]
    #mean_list = []
    for n in list_parader:
        data_k = data_gp.loc[n]
        geo = data_k['parder_geom'].iat[0]
        geo_lat = data_k['parder_lat'].iat[0]
        geo_lon = data_k['parder_lon'].iat[0]
        
        H_Punta(data_k,geo,geo_lat,geo_lon,dataframe_buses_p1,n,'S1')
        H_Punta(data_k,geo,geo_lat,geo_lon,dataframe_buses_p2,n,'S2')
        H_Valle(data_k,geo,geo_lat,geo_lon,dataframe_buses_v1,n,'S1')
        H_Valle(data_k,geo,geo_lat,geo_lon,dataframe_buses_v2,n,'S2')
        H_Bajo(data_k,geo,geo_lat,geo_lon,dataframe_buses_b1,n,'S1')
        H_Bajo(data_k,geo,geo_lat,geo_lon,dataframe_buses_b2,n,'S2')
        H_All(data_k,geo,geo_lat,geo_lon,dataframe_buses,n)

   
        
    dataframe_total_busparadero_punta1 = pd.DataFrame(dataframe_buses_p1)
    dataframe_total_busparadero_punta2 = pd.DataFrame(dataframe_buses_p2)
    dataframe_total_busparadero_valle1 = pd.DataFrame(dataframe_buses_v1)
    dataframe_total_busparadero_valle2 = pd.DataFrame(dataframe_buses_v2)
    dataframe_total_busparadero_bajo1 = pd.DataFrame(dataframe_buses_b1)
    dataframe_total_busparadero_bajo2 = pd.DataFrame(dataframe_buses_b2)
    dataframe_total_busparadero = pd.DataFrame(dataframe_buses)
    #print(dataframe_total_busparadero_punta1,dataframe_total_busparadero_punta2,dataframe_total_busparadero_valle1,dataframe_total_busparadero_valle2,dataframe_total_busparadero_bajo1,dataframe_total_busparadero_bajo2,dataframe_total_busparadero)

    dataframe_total_busparadero_punta1.to_csv('E04I_PUNTA1.csv')
    dataframe_total_busparadero_punta2.to_csv('E04I_PUNTA2.csv')
    dataframe_total_busparadero_valle1.to_csv('E04I_VALLE1.csv')
    dataframe_total_busparadero_valle2.to_csv('E04I_VALLE2.csv')
    dataframe_total_busparadero_bajo1.to_csv('E04I_BAJO1.csv')
    dataframe_total_busparadero_bajo2.to_csv('E04I_BAJO2.csv')
    dataframe_total_busparadero.to_csv('E04I_ALL.csv')

def get_Bus_Cant_Prom_Por_Paredero():#Frecuenica
    Hour_list_from = ['2018-06-13 00:00:00+00','2018-06-13 01:00:00+00','2018-06-13 02:00:00+00','2018-06-13 03:00:00+00','2018-06-13 04:00:00+00','2018-06-13 05:00:00+00','2018-06-13 06:00:00+00','2018-06-13 07:00:00+00','2018-06-13 08:00:00+00','2018-06-13 09:00:00+00','2018-06-13 10:00:00+00','2018-06-13 11:00:00+00','2018-06-13 12:00:00+00','2018-06-13 13:00:00+00','2018-06-13 14:00:00+00','2018-06-13 15:00:00+00','2018-06-13 16:00:00+00','2018-06-13 18:00:00+00','2018-06-13 19:00:00+00','2018-06-13 20:00:00+00','2018-06-13 21:00:00+00','2018-06-13 22:00:00+00','2018-06-13 23:00:00+00']

    Hour_list_to = ['2018-06-13 00:59:59+00','2018-06-13 01:59:59+00','2018-06-13 02:59:59+00','2018-06-13 03:59:59+00','2018-06-13 04:59:59+00','2018-06-13 05:59:59+00','2018-06-13 06:59:59+00','2018-06-13 07:59:59+00','2018-06-13 08:59:59+00','2018-06-13 09:59:59+00','2018-06-13 10:59:59+00','2018-06-13 11:59:59+00','2018-06-13 12:59:59+00','2018-06-13 13:59:59+00','2018-06-13 14:59:59+00','2018-06-13 15:59:59+00','2018-06-13 16:59:59+00','2018-06-13 18:59:59+00','2018-06-13 19:59:59+00','2018-06-13 20:59:59+00','2018-06-13 21:59:59+00','2018-06-13 22:59:59+00','2018-06-13 23:59:59+00']
    #*************************
    #print(type(result.index))
    #print(result.index.names)
    #print(result.index.values)
    #print(result.index.levels)

    dataframe_ruta = pd.read_csv("./E04I.csv")
    temp2 = dataframe_ruta.groupby(['parader'], group_keys=True, as_index=True).apply(lambda x: x)
    #temp4 = dataframe_ruta.groupby(['parder_geom'], group_keys=True, as_index=True).apply(lambda x: x)
    list_paredors = temp2.index.levels[0]
    #temp3 = temp2.loc['PA146']
    #a = temp2.loc['PA146']['fechahora'].tolist()[0]

    dataframe_buses = {'paradero':[],'promedio_bus_hora':[],'geo_parader':[],'geo_parader_lat':[],'geo_parader_lon':[],'calificacion':[]}
    #print(len(Hour_list_from))
    #print(len(Hour_list_to))

    for i in list_paredors: 
        x = temp2.loc[i]
        List_total_buses = list()
        geo = x['parder_geom'].iat[0]
        geo_lat = x['parder_lat'].iat[0]
        geo_lon = x['parder_lon'].iat[0]
        #paradero_list = list()
        #print(geo)
        for j in range(23):
            #print(j)
            df = x[(x['fechahora'] >= Hour_list_from[j]) & (x['fechahora'] <= Hour_list_to[j])]
            List_total_buses.append(df['bus'].nunique())
            #Lista_interval.append(Hour_list_from[j]+' to '+Hour_list_to[j])
        mean = (sum(List_total_buses) / 24)
        dataframe_buses['paradero'].append(i)
        dataframe_buses['promedio_bus_hora'].append(mean)
        dataframe_buses['geo_parader'].append(geo)
        dataframe_buses['geo_parader_lat'].append(geo_lat)
        dataframe_buses['geo_parader_lon'].append(geo_lon)
        if mean < 5:
            dataframe_buses['calificacion'].append(0)
        elif mean > 6:
            dataframe_buses['calificacion'].append(1)
        else:
            dataframe_buses['calificacion'].append(2)


        
        #dataframe_buses['rango_hora'] += Lista_interval


    dataframe_total_busparadero = pd.DataFrame(dataframe_buses)
    print(dataframe_total_busparadero)
    dataframe_total_busparadero.to_csv('E04I_NOTED.csv')

    
#getHoraProm()  
getPromRegcBus()

#print(df['bus'].nunique())

#dataframe_bus = pd.read_csv("./buses.csv", chunksize=500000)

#dataframe_pararutas = pd.read_csv("./paraderosrutas.csv", chunksize=500000)

#print(dataframe_ruta)

#temp = dataframe_ruta.groupby(['bus'], group_keys=True, as_index=True).apply(lambda x: x)

#row_chunks = chunk.iterrows()
#temp = chunk.groupby(['vendor', 'bus'], group_keys=True, as_index=True).apply(lambda x: x)



'''
b = a[0:19]

t1 = datetime.strptime('2018-06-13 00:13:51', '%Y-%m-%d %H:%M:%S')
t2 = datetime.strptime('2018-06-13 00:14:21', '%Y-%m-%d %H:%M:%S')
print(t1>t2)
print(t1<t2)

date_object = datetime.strptime(b, '%Y-%m-%d %H:%M:%S')



group_chunks = []
for chunk_number, chunk in enumerate(dataframe_bus):
    if chunk_number > 1:
        break
    print(f'Chunk number {chunk_number + 1} \r')

    group_chunks.append(temp)
result = pd.concat(group_chunks)
'''


#[rutas, micros, _] = result.index.levels

# Ejemplo de acceso a filas por ruta --> result.loc["T101"]

# Ejemplo de acceso a filas por ruta y bus --> result.loc["T101","BJFD-18"]

# Ejemplo de convertir uno de los elementos anteriores (o columna de estos) en una lista normal de python --> result.loc["T101","BJFD-18"]["velocidad"].tolist()

#print(len(rutas))

#print(result.loc["T101"]["pasajeros"])




'''
    aux = temp2.loc['PA146']
    
    for i in range(len(dataframe_list)):
        if i > 0:
            aux = pd.concat(aux,dataframe_list[i])
        else:
            aux = dataframe_list[i]
    
    dataf = aux
    print(dataf)
        #print(df_g)
    #w['fechahora'] = pd.to_datetime(w['fechahora'], infer_datetime_format=True)
    #y = w.loc['BJFS-70']
    #dfs = [x for _, x in y.groupby('fechahora')]
    #print(y['velocidad'])
    
    horas = y['fechahora'].tolist()
    d = y['d'].tolist()
    #print(horas,d)
    new_horas = list()
    new_d = list()
    aux_d = 0.0
    aux_h = 0.0
    d_next = 0.0
    h_next = 0.0
    for i in range(len(horas)):
        #print(i)
        if i > 0:
            #print(d[i],aux_d)
            if aux_d > d[i]: #0.000594 > 0.001921 NOT - 0.000594 > 0.002052 NOT - 0.000594 > 0.002677 NOT - 0.000594 > 0.001976 NOT - 0.001976 > 0.000927 YES
                new_d.append(aux_d) #0.001976
                new_horas.append(aux_h)
                aux_d = d[i] #0.000927
                d_next = d[i] #0.000927
                aux_h = horas[i]
            elif d[i]>d_next: #0.001921 > 0.000594 YES - 0.002052 > 0.001921 YES - 0.002677 > 0.002052 YES - 0.001976 > 0.002677 NOT 
                d_next = d[i] #0.001921 - 0.00205 - 0.002677
            else:
                new_d.append(aux_d) #0.000594
                new_horas.append(aux_h) 
                aux_d = d[i] #0.001976
                d_next = d[i] #0.001976
                aux_h = horas[i]
        else:
            #print(d[i])
            #print(aux_d)
            aux_d = d[i] #0.000594
            #print(aux_d)
            d_next = d[i] #0.000594
            aux_h = horas[i]

    print(new_horas,new_d)
 
    
    
    a = df.loc[df.groupby('bus')['d'].idxmax()]
    b = a.sort_values(by=['fechahora'])

    LB = b['bus'].tolist()
    l1 = b['fechahora'].tolist()

    d = df.loc[df.groupby('bus')['d'].idxmin()]
    e = d.sort_values(by=['fechahora'])
    l2 = e['fechahora'].tolist()
    print(b)
    print(e)
'''
    #z = pd.concat([b, e])
    #z['fechahora'] = pd.to_datetime(z['fechahora'], infer_datetime_format=True)
    #print(z)
    #l2 = z['fechahora'].tolist()
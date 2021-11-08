"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import shellsort as sa
import time
import datetime
import folium 
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newAnalyzer():
    analyzer = { 'UFOS': None,
                'city': None,
                'duration(seconds)': None,
                'duration(hours/min)': None,
                'datetime': None,
                'latitud': None, 
                'longitud': None}

    analyzer['UFOS'] = lt.newList('SINGLE_LINKED')

    #Lab 8: analyzer['city'] = om.newMap(omaptype = 'RBT',comparefunction = compareCityLab) 

    analyzer['city'] = om.newMap(omaptype = 'RBT',
                                      comparefunction = compareHM)
    analyzer['duration(seconds)'] = om.newMap(omaptype = 'RBT',
                                      comparefunction = compareDS)
    analyzer['datetime'] = om.newMap(omaptype = 'RBT',
                                      comparefunction =compareHM)
    analyzer['time'] = om.newMap(omaptype = 'RBT',
                                      comparefunction =compareHM)
    analyzer['latitud'] = om.newMap(omaptype = 'RBT',
                                      comparefunction =compareLL)  
    analyzer['longitud'] = om.newMap(omaptype = 'RBT',
                                      comparefunction =compareLL)  


    return analyzer

# Funciones para agregar informacion al catalogo
def addEvent(analyzer, event):
    lt.addLast(analyzer['UFOS'], event)
    #Lab 8: addCityLab(analyzer['city'], event)
    addCity(analyzer['city'], event)
    addDurationSeconds(analyzer['duration(seconds)'], event)
    #addDurationMinuteHour(analyzer['duration(hours/min)'], event)
    addDateTime(analyzer['datetime'], event)
    addTime(analyzer['time'], event)
    addLongitud(analyzer['longitud'], event)
    return analyzer

def addCity(map, event):

    city = event['city']
    entry = om.get(map, city)
    if entry is None:
        newEntry = newDataCity()
        om.put(map, city, newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry['events'], event)
    return map

def addDurationSeconds(map, evento):
    durationS = evento['duration (seconds)']
    entry = om.get(map, durationS)
    if entry is None:
        newEntry = newdataDS()
        om.put(map, durationS, newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry['events'], evento)
    return map

def addDateTime(map, evento):
    occureddate = evento['datetime']
    eventdate = datetime.datetime.strptime(occureddate, '%Y-%m-%d %H:%M:%S')
    
    entry = om.get(map, eventdate.date())
    if entry is None:
        newEntry = newdataDatetime(evento)
        om.put(map, eventdate.date(), newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry['events'], evento)
    return map
    
def addTime(map, evento):
    occureddate = evento['datetime']
    eventdate = datetime.datetime.strptime(occureddate, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, eventdate.time())
    if entry is None:
        newEntry = newdataDatetime(evento)
        om.put(map, eventdate.time(), newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry['events'], evento)
    return map

def addDateTimeCity(map, evento):
    occureddate = evento['datetime']
    
    eventdate = datetime.datetime.strptime(occureddate, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, eventdate.date())
    if entry is None:
        newEntry = newdataDatetime(evento)
        om.put(map, eventdate.date(), newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry['events'], evento)
    return map

def addLongitud(map, evento):
    log = float(evento['longitude'])
    longitud = round(log, 2)
    entry = om.get(map, longitud)
    if entry is None:
        newEntry = newLongitud()
        om.put(map, longitud, newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry['events'], evento)
    return map

def addLatitud(map, evento):
    lat = float(evento['latitude'])
    latitud = round(lat, 2)
    entry = om.get(map, latitud)
    if entry is None:
        newEntry = newLatitud()
        om.put(map, latitud, newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry['events'], evento)
    return map

# Funciones para creacion de datos
def newDataCity():
    entry = {'events': None}
    entry['events'] = lt.newList('SINGLE_LINKED', '')
    return entry

def newdataDS():
    entry = {'events': None}
    entry['events'] = lt.newList('ARRAY_LIST', compareDS)
    return entry

def newData():
    entry = {'events': None}
    entry['events'] = lt.newList('ARRAY_LIST', compareHM)
    return entry

def newdataDatetime(evento):
    entry = {'events': None}
    entry['events'] = lt.newList('ARRAY_LIST', compareHM)
    return entry

def newLatitud():
    entry = {'events': None}
    entry['events'] = lt.newList('ARRAY_LIST', compareLL)
    return entry

def newLongitud():
    entry = {'events': None}
    entry['events'] = lt.newList('ARRAY_LIST', compareLL)
    return entry

# Funciones de consulta


# ==============================
#Lab 8:
def addCityLab(map, evento):
    city = evento['city']
    entry = om.get(map, city)
    if entry is None:
        newEntry = newdataCity(city)
        om.put(map, city, newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry['events'], evento)
    return map
def newdataCity(city):
    entry = {'city': None, 'events': None}
    entry['city'] = city
    entry['events'] = lt.newList('SINGLE_LINKED', '')
    return entry

def Size(analyzer):
    """
    Número de crimenes
    """
    return om.size(analyzer['city'])


def Height(analyzer):
    """
    Altura del arbol
    """
    return om.height(analyzer['city'])
# ==============================

#---------------------------------------------------------------------------------------------------------------------------------------
#Req 1:
def getEventsByCity(analyzer,ciudad):
    start_time = time.process_time()
    ciudadTree = analyzer['city']
    keys = om.keySet(ciudadTree)
    eye_city = ""
    sightings = 0
    for ciudads in lt.iterator(keys):
        par = om.get(analyzer['city'], ciudads) 
        city_value = me.getValue(par)
        if lt.size(city_value['events']) > sightings:
            eye_city = ciudads
            sightings = lt.size(city_value['events'])
    city_especific = om.get(analyzer['city'], ciudad)
    specific = me.getValue(city_especific)
    list_specific = specific['events']
    sortDurationHM(list_specific)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000 
    return sightings, list_specific, elapsed_time_mseg, eye_city
    
#---------------------------------------------------------------------------------------------------------------------------------------
#Req 2:
def getEventsByDurationS(analyzer, minSeg, maxSeg):
    start_time = time.process_time()
    durationSegTree = analyzer['duration(seconds)']
    maxK = om.maxKey(durationSegTree)
    maxget = om.get(durationSegTree, maxK)
    maxvalues = me.getValue(maxget)
    maxsize = lt.size(maxvalues['events'])
   
    lst = om.values(analyzer['duration(seconds)'], minSeg, maxSeg)
    lista_duracionSeg = lt.newList('ARRAY_LIST')

    for i in lt.iterator(lst):
        i = i['events']
        for j in lt.iterator(i):
            lt.addLast(lista_duracionSeg, j)

    sortDurationS(lista_duracionSeg) #Se organiza cronologicamente
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000        
    return maxsize, lista_duracionSeg, elapsed_time_mseg, maxK

#---------------------------------------------------------------------------------------------------------------------------------------
#Req 3:
def getEventsByRangeDate(analyzer, minDate, maxDate):

    start_time = time.process_time()
    datetimetree = analyzer['datetime']
    maxK = om.maxKey(datetimetree)
    maxget = om.get(datetimetree, maxK)
    maxvalues = me.getValue(maxget)
    maxsize = lt.size(maxvalues['events'])
    fminDate=datetime.datetime.strptime(minDate, '%H:%M:%S')
    fmaxDate=datetime.datetime.strptime(maxDate, '%H:%M:%S')
    lst = om.values(analyzer['time'], fminDate.time(), fmaxDate.time())
    lista_datesinrange = lt.newList('ARRAY_LIST')

    for i in lt.iterator(lst):
        i = i['events']
        for j in lt.iterator(i):
            lt.addLast(lista_datesinrange, j)

    sortDurationHM(lista_datesinrange) 
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000        
    return maxsize,lista_datesinrange, elapsed_time_mseg, maxK


#---------------------------------------------------------------------------------------------------------------------------------------
#Req 4:
def geteventsByDatetime(analyzer, datemin, datemax):
    start_time = time.process_time()
    datetimetree = analyzer['datetime']
    minK = om.minKey(datetimetree)
    minget = om.get(datetimetree, minK)
    minvalues = me.getValue(minget)
    minsize = lt.size(minvalues['events'])
    fminDate = datetime.datetime.strptime(datemin, '%Y-%m-%d')
    fmaxDate = datetime.datetime.strptime(datemax, '%Y-%m-%d')
    lst = om.values(analyzer['datetime'], fminDate.date(), fmaxDate.date())
    lista_datesinrange = lt.newList('ARRAY_LIST')

    for i in lt.iterator(lst):
        i = i['events']
        for j in lt.iterator(i):
            lt.addLast(lista_datesinrange, j)

    sortDurationHM(lista_datesinrange) 
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000        
    return minsize,lista_datesinrange, elapsed_time_mseg, minK

#---------------------------------------------------------------------------------------------------------------------------------------
#Req 5:

def eventLongLat(analyzer, latmin, latmax, longmin, longmax):
    start_time = time.process_time()
    longmap = analyzer['longitud']
    lst1 = om.values(longmap, longmin, longmax)
    comb = om.newMap(omaptype='RBT', comparefunction=compareLL)
    lista_filtrada = lt.newList('ARRAY_LIST')

    for i in lt.iterator(lst1):
        i = i['events']
        for j in lt.iterator(i):
            addLatitud(comb, j)
     
    listasemifiltrada =  om.values(comb, latmin, latmax)

    for i in lt.iterator(listasemifiltrada):
        i = i['events']
        for j in lt.iterator(i):
            lt.addLast(lista_filtrada, j)

    sortLatitud(lista_filtrada)
    total = lt.size(lista_filtrada)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000        
    return lista_filtrada, elapsed_time_mseg, total

#---------------------------------------------------------------------------------------------------------------------------------------
#Req 6:

def vicualizarEventoZonaG(eventLL, latmin, latmax, longmin, longmax):
    promedio_lat = (latmax + latmin)/ 2
    latP = round(promedio_lat, 2)
    promedio_long = (longmax + longmin)/ 2
    longP = round(promedio_long, 2)

    mapaF = folium.Map(location=(latP, longP), zoom_start = 8)

    folium.Rectangle([(latmin, latmax), (longmin, longmax)],
                        fill=True,
                        weight=5,
                        fill_color="orange",
                        color="green").add_to(mapaF)

    cityL = []
    datetimeL = []
    durationSL = []
    shapeL = []
    commentsL = []
    countryL = []
    latL = []
    longL = []
    for element in lt.iterator(eventLL[0]):
        cityL.append(element['city'])
        datetimeL.append(element['datetime'])
        durationSL.append(element['duration (seconds)']) 
        shapeL.append(element['shape'])
        commentsL.append(element['comments'])
        countryL.append(element['country'])
        latL.append(element['latitude'])
        longL.append(element['longitude'])

    for  city, datetime, durationS, shape, comments, country, lat, long in zip(cityL, datetimeL, durationSL, shapeL, commentsL, countryL, latL, longL):
        
        info = 'Datetime: ' + str(datetime) + ', City: ' + str(city) + ', Country:' + str(country) + ', Shape: ' + str(shape) + ', Duration(seconds): ' + str(durationS) +', Comments: ' + str(comments) + ', Latitude: ' + str(lat) + ', Longitude: ' + str(long)
    
        folium.Marker(
                    location=[lat,long], 
                    popup=folium.Popup(info, max_widht=500), 
                    icon=folium.Icon(color='green', icon_color='white', icon='info-sign', angle=0, prefix='glyphicon')).add_to(mapaF)
    

    mapaF.save(outfile='eventos.html')

# Funciones utilizadas para comparar elementos dentro de una lista

def compareCatalog(category, entry):
    categoryentry = me.getKey(entry)
    if (category == categoryentry):
        return 0
    elif (category > categoryentry):
        return 1
    else:
        return -1

def compareCityLab(city1, entry):
    
    
    #cityLab = me.getKey(entry)
    if (city1 == entry):
        return 0
    elif (city1 > entry):
        return 1
    else:
        return -1

def compareDS(eve1, eve2):
  
    if (float(eve1) == float(eve2)):
        return 0
    elif (float(eve1) > float(eve2)):
        return 1
    else:
        return -1
def compareHM(eve1, eve2):
  
    if (eve1 == eve2):
        return 0
    elif (eve1 > eve2):
        return 1
    else:
        return -1  

def compareLL(eve1, eve2):
  
    if (float(eve1) == float(eve2)):
        return 0
    elif (float(eve1) > float(eve2)):
        return 1
    else:
        return -1      

def cmpDatetime(ds1, ds2):
    ds_1 = ds1['datetime']
    s1 = datetime.datetime.strptime(ds_1, '%Y-%m-%d %H:%M:%S')
    ds_2 = ds2['datetime']
    s2 = datetime.datetime.strptime(ds_2, '%Y-%m-%d %H:%M:%S')
    return s2.date() > s1.date()

def cmpDate(ds1, ds2):
    ds_1 = ds1['datetime']
    s1 = datetime.datetime.strptime(ds_1, '%Y-%m-%d %H:%M:%S')
    ds_2 = ds2['datetime']
    s2 = datetime.datetime.strptime(ds_2, '%Y-%m-%d %H:%M:%S')
    if (s1.date() == s2.date()):
        return 0
    elif (s1.date() > s2.date()):
        return 1
    else:
        return -1

def cmpDS(ds1, ds2):
    ds_1 = ds1['duration (seconds)']
    ds_2 = ds2['duration (seconds)']
    return float(ds_1) < float(ds_2)

def compListDS(event, events):
    if str(event) in str(events['Duration_seg']):
        return 0
    else:
        return -1

def cmpLAT(lat1, lat2):
    lat1 = lat1['latitude']
    lat2 = lat2['latitude']
    return float(lat1) < float(lat2)

# Funciones de ordenamiento

def sortDurationS(lista_duracionSeg):
    return ms.sort(lista_duracionSeg, cmpDS)

def sortDurationHM(lista_duracionSeg):
    return ms.sort(lista_duracionSeg, cmpDatetime)
def sortLatitud(listfiltrada):
    return ms.sort(listfiltrada, cmpLAT)
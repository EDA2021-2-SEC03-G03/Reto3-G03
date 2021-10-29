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
                'datetime': None}

    analyzer['UFOS'] = lt.newList('SINGLE_LINKED')

    #Lab 8: analyzer['city'] = om.newMap(omaptype = 'RBT',comparefunction = compareCityLab) 

    analyzer['city'] = mp.newMap(10000,
                                 maptype='PROBING',
                                 loadfactor=0.5,
                                 comparefunction=compareCatalog)
    analyzer['duration(seconds)'] = om.newMap(omaptype = 'RBT',
                                      comparefunction = compareDS)
    analyzer['duration(hours/min)'] = om.newMap(omaptype = 'RBT',
                                      comparefunction = cmpDatetime)
    analyzer['datetime'] = om.newMap(omaptype = 'RBT',
                                      comparefunction ='')


    return analyzer

# Funciones para agregar informacion al catalogo
def addEvent(analyzer, event):
    lt.addLast(analyzer['UFOS'], event)
    #Lab 8: addCityLab(analyzer['city'], event)
    #addCity(analyzer, event['city'], event)
    addDurationSeconds(analyzer['duration(seconds)'], event)
    #addDurationMinuteHour(analyzer['duration(hours/min)'], event)
    #addDateTime(analyzer['datetime'], event)
    return analyzer

def addCity(analyzer, ciudad, event):

    cities = analyzer['city']
    existmedium = mp.contains(cities, ciudad)
    if existmedium:
        entry = mp.get(cities, ciudad)
        city = me.getValue(entry)
    else:
        city = newdataCity()
        mp.put(cities, ciudad, city)
    #lt.addLast(city['events'], event)

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

def addDurationMinuteHour(map, evento):
    durationHM = evento['duration (hours/min)']
    entry = om.get(map, durationHM)
    if entry is None:
        newEntry = newData()
        om.put(map, durationHM, newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry['events'], evento)
    return map

def addDateTime(map, evento):
    occureddate = evento['datetime']
    eventdate = datetime.datetime.strptime(occureddate, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, eventdate)
    if entry is None:
        newEntry = newdataDatetime()
        om.put(map, eventdate, newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry['events'], evento)
    return map


# Funciones para creacion de datos
def newdataCity():
    entry = {'events': None}
    entry['events'] = om.newMap(omaptype = 'RBT', comparefunction= '')
    return entry

def newdataDS():
    entry = {'events': None}
    entry['events'] = lt.newList('ARRAY_LIST', compareDS)
    return entry

def newData():
    entry = {'events': None}
    entry['events'] = lt.newList('ARRAY_LIST', '')
    return entry

def newdataDatetime():
    entry = {'events': None}
    entry['events'] = lt.newList('ARRAY_LIST', cmpDatetime)
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
def getEventsByCity(ciudad):
    pass 

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



#---------------------------------------------------------------------------------------------------------------------------------------
#Req 4:
def geteventsByDatetime(analyzer, datemin, datemax):
    pass


#---------------------------------------------------------------------------------------------------------------------------------------
#Req 5:

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

def cmpDatetime(ds1, ds2):
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

# Funciones de ordenamiento

def sortDurationS(lista_duracionSeg):
    return ms.sort(lista_duracionSeg, cmpDS)

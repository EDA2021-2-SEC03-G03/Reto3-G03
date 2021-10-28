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
from DISClib.Algorithms.Sorting import shellsort as sa
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
                                      comparefunction = compare)
    analyzer['duration(hours/min)'] = om.newMap(omaptype = 'RBT',
                                      comparefunction = compare)
    analyzer['datetime'] = om.newMap(omaptype = 'RBT',
                                      comparefunction = compare)


    return analyzer

# Funciones para agregar informacion al catalogo
def addEvent(analyzer, event):
    lt.addLast(analyzer['UFOS'], event)
    #Lab 8: addCity(analyzer['city'], event)
    addCity(analyzer, event['city'], event)
    addDurationSeconds(analyzer['duration(seconds)'], event)
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
    lt.addLast(city['events'], event)

def addDurationSeconds(map, evento):
    durationS = evento['duration(seconds)']
    entry = om.get(map, durationS)
    if entry is None:
        newEntry = newdata(durationS)
        om.put(map, durationS, newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry['events'], evento)
    return map

# Funciones para creacion de datos
def newdataCity():
    entry = {'events': None}
    entry['events'] = om.newMap(omaptype = 'RBT', comparefunction= compare)
    return entry

def newdata(index):
    entry = {'Index': None, 'events': None}
    entry['city'] = index
    entry['events'] = lt.newList('ARRAY_LIST', compare)
    return entry

# Funciones de consulta


# ==============================
#Lab 8:
def addCity(map, evento):
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
    entry['events'] = lt.newList('SINGLE_LINKED', compare)
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

def compare(eve1, eve2):
  
    if (eve1 == eve2):
        return 0
    elif (eve1 > eve2):
        return 1
    else:
        return -1

# Funciones de ordenamiento

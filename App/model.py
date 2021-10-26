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
                'datetime': None,
                'city': None}
    analyzer['UFOS'] = lt.newList('SINGLE_LINKED')

    analyzer['datetime'] = om.newMap(omaptype = 'RBT',
                                      comparefunction = compare)
    analyzer['city'] = om.newMap(omaptype = 'RBT',
                                      comparefunction = compare)
    return analyzer

# Funciones para agregar informacion al catalogo
def addEvent(analyzer, event):
    lt.addLast(analyzer['UFOS'], event)
    addCity(analyzer['city'], event)
    return analyzer

def addCity(analyzer, evento):
    entry = om.get(analyzer, evento['city'])
    if entry is None:
        newEntry = newdata()
        om.put(analyzer, evento['city'], newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry, evento)
    return analyzer

# Funciones para creacion de datos
def newdata():
    entry = lt.newList('SINGLE_LINKED', compare)
    return entry
# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def compareIds(id1, id2):
    if (id1 == id2):
        return 0
    elif (id1 > id2):
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

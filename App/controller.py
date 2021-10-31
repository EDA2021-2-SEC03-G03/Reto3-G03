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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initAnalyzer():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos
def loadData(analyzer):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    namefile = cf.data_dir + 'UFOS/UFOS-utf8-small.csv'
    input_file = csv.DictReader(open(namefile, encoding="utf-8"), delimiter=",")
    for event in input_file:
        model.addEvent(analyzer, event)

#Funciones de Consulta - Lab 8

def Size(analyzer):
    """
    Numero de crimenes leidos
    """
    return model.Size(analyzer)


def Height(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.Height(analyzer)


#Funciones de Consulta

#Req 1:
def getEventsByCity(analyzer,ciudad):
    return model.getEventsByCity(analyzer,ciudad)

#Req 2:
def getEventsByDurationS(analyzer, minSeg, maxSeg):
    return model.getEventsByDurationS(analyzer, minSeg, maxSeg)

#Req 3:
def getEventsByRangeDate(analyzer, minDate, maxDate):
    return model.getEventsByRangeDate(analyzer,minDate,maxDate)

#Req 4:
def geteventsByDatetime(analyzer, datemin, datemax):
    return model.geteventsByDatetime(analyzer, datemin, datemax)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

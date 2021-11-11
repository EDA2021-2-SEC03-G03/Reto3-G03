"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Contar los avisamientos en una ciudad")
    print("3 - Datos caracterìsticos del árbol")
    #print("3- Contar los avistamientos por duración")
    print("4- Contar avistamientos por Hora/Minutos del día")
    print("5- Contar los avistamientos en un rango de fechas")
    print("6- Contar los avistamientos por Zonas Geográficas")
    print("7- Visualizar los avistamientos de una zona geográfica (opción 6)")
    print("0- Salir")
    print("*******************************************")

analyzer = None
eventLL = None
latmin = None
latmax =None
longmin = None
longmax = None


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        analyzer = controller.initAnalyzer()
        controller.loadData(analyzer)

    #Lab 8:
    #elif int(inputs[0]) == 2:
        #Lab 8:
        #print("\nCargando información de eventos ....")
        #controller.loadData(analyzer)    
    #elif int(inputs[0]) == 3:
        #Lab 8: 
        #print('Cargando información de características')
        #print('Ciudades cargadas: ' + str(controller.Size(analyzer)))
        #print('Altura del arbol: ' + str(controller.Height(analyzer)))
    elif int(inputs[0]) == 2:

        #Req 1:
        ciudad = input("Ingrese el nombre de la ciudad a consultar: ").lower()
        EventC = controller.getEventsByCity(analyzer, ciudad)
        lista = EventC[1]

        print('There are ' + str(EventC[0]) + ' sightings in the city with more sightings: ' + str(EventC[3]))
        print('There are ' + str(lt.size(lista)) + ' sightings in ' + ciudad.upper())
        print("--------------------------------------------------------------------------")
        print("First three")
        primeros=lt.subList(lista,1,3)
        for avistamiento in lt.iterator(primeros):
            print("| Datetime: " + avistamiento["datetime"] + " | City / Country: "  + avistamiento['city'] + " / " + avistamiento['country'] + "\t| Duration(in seconds): " + avistamiento['duration (seconds)']+"\t| Shape: " + avistamiento['shape'])
        print("--------------------------------------------------------------------------")
        print('Last three: ')
        ultimos=lt.subList(lista,lt.size(lista)-2,3)
        for avistamiento in lt.iterator(ultimos):
            print("| Datetime: " + avistamiento["datetime"] + " | City / Country: "  + avistamiento['city'] + " / " + avistamiento['country'] + "\t| Duration(in seconds): " + avistamiento['duration (seconds)']+"\t| Shape: " + avistamiento['shape'])
        print("--------------------------------------------------------------------------")
        print("Tiempo utilizado en el ordenamiento: " + str(EventC[2]) + " Milisegundos")

    elif int(inputs[0]) == 3:
        #Req 2:
        minSeg = input("Ingrese el límite inferior en segundos: ")
        maxSeg = input("Ingrese el límite superior en segundos: ")
        eventDS = controller.getEventsByDurationS(analyzer, minSeg, maxSeg)
        lista = eventDS[1]

        print('There are ' + str(eventDS[0]) + ' sightings with the maximun duration in seconds: ' + str(eventDS[3]))
        print('There are ' + str(lt.size(lista)) + ' sightings between: ' + str(minSeg) + ' and ' + str(maxSeg) + ' duration')
        print("--------------------------------------------------------------------------")
        print("First three")
        print(lista['elements'][0:3])
        print("--------------------------------------------------------------------------")
        print('Last three: ')
        print(lista['elements'][-3:])
        print("--------------------------------------------------------------------------")
        print("Tiempo utilizado en el ordenamiento: " + str(eventDS[2]) + " Milisegundos")

    elif int(inputs[0]) == 4:
        #Req 3:
        minDate = input("Ingrese la hora inferior en formato HH:MM : ")
        maxDate = input("Ingrese la hora superior en formato HH:MM : ")
        minDate += ":00"
        maxDate += ":00"
        eventHM = controller.getEventsByRangeDate(analyzer, minDate, maxDate)
        lista = eventHM[1]

        print('There are ' + str(eventHM[0]) + ' sightings in the maximum date: ' + str(eventHM[3]))
        print('There are ' + str(lt.size(lista)) + ' sightings between: ' + str(minDate) + ' and ' + str(maxDate) + ' duration')
        print("--------------------------------------------------------------------------")
        print("First three")
        primeros=lt.subList(lista,1,3)
        for avistamiento in lt.iterator(primeros):
            print("| Datetime: " + avistamiento["datetime"] + " | City / Country: "  + avistamiento['city'] + " / " + avistamiento['country'] + "\t| Duration(in seconds): " + avistamiento['duration (seconds)']+"\t| Shape: " + avistamiento['shape'])
        print("--------------------------------------------------------------------------")
        print('Last three: ')
        ultimos=lt.subList(lista,lt.size(lista)-2,3)
        for avistamiento in lt.iterator(ultimos):
            print("| Datetime: " + avistamiento["datetime"] + " | City / Country: "  + avistamiento['city'] + " / " + avistamiento['country'] + "\t| Duration(in seconds): " + avistamiento['duration (seconds)']+"\t| Shape: " + avistamiento['shape'])
        print("--------------------------------------------------------------------------")
        print("Tiempo utilizado en el ordenamiento: " + str(eventHM[2]) + " Milisegundos")

        

    elif int(inputs[0]) == 5:

        datemin = input('Límite inferior en formato AAAA-MM-DD: ')
        datemax = input('Límite superior en formato AAAA-MM-DD: ')
        eventHM = controller.geteventsByDatetime(analyzer, datemin, datemax)
        lista = eventHM[1]

        print('There are ' + str(eventHM[0]) + ' sightings in the oldest date: ' + str(eventHM[3]))
        print('There are ' + str(lt.size(lista)) + ' sightings between: ' + str(datemin) + ' and ' + str(datemax) + ' duration')
        print("--------------------------------------------------------------------------")
        print("First three")
        primeros=lt.subList(lista,1,3)
        for avistamiento in lt.iterator(primeros):
            print("| Datetime: " + avistamiento["datetime"] + " | City / Country: "  + avistamiento['city'] + " / " + avistamiento['country'] + "\t| Duration(in seconds): " + avistamiento['duration (seconds)']+"\t| Shape: " + avistamiento['shape'])
        print("--------------------------------------------------------------------------")
        print('Last three: ')
        ultimos=lt.subList(lista,lt.size(lista)-2,3)
        for avistamiento in lt.iterator(ultimos):
            print("| Datetime: " + avistamiento["datetime"] + " | City / Country: "  + avistamiento['city'] + " / " + avistamiento['country'] + "\t| Duration(in seconds): " + avistamiento['duration (seconds)']+"\t| Shape: " + avistamiento['shape'])
        print("--------------------------------------------------------------------------")
        print("Tiempo utilizado en el ordenamiento: " + str(eventHM[2]) + " Milisegundos")

    elif int(inputs[0]) == 6:
        #Req 5:
        latmin = float(input('Ingrese la latitud minima: '))
        latmax =float(input('Ingrese la latitud máxima: '))
        longmin = float(input('Ingrese la longitud minima: '))
        longmax = float(input('Ingrese la longitud máxima: '))
        eventLL = controller.eventLongLat(analyzer, latmin, latmax, longmin, longmax)

        lst = eventLL[0]
        print('The total of sightings in the area are: ' + str(eventLL[2]))
        if eventLL[2] >= 10:
            print("First five")
            print(lst['elements'][0:5])
            print("--------------------------------------------------------------------------")
            print('Last five: ')
            print(lst['elements'][-5:]) 
            print("--------------------------------------------------------------------------")
            print("Tiempo utilizado en el ordenamiento: " + str(eventLL[1]) + " Milisegundos")
        elif eventLL[2] < 10:
            print("First three")
            print(lst['elements'][0:3])
            print("--------------------------------------------------------------------------")
            print('Last three: ')
            print(lst['elements'][-3:]) 
            print("--------------------------------------------------------------------------")
            print("Tiempo utilizado en el ordenamiento: " + str(eventLL[1]) + " Milisegundos")

    elif int(inputs[0]) == 7:

        controller.vicualizarEventoZonaG(eventLL, latmin, latmax, longmin, longmax)

    else:
        sys.exit(0)
sys.exit(0)

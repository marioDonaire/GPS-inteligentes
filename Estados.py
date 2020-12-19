#!/usr/bin/python3
import hashlib as hl
import os
import math
class Estado():
    '''
    estado de un nodo
    '''
    def __init__(self, id_nodo, lista_objetivo):
        '''
        contructor de la clase EspacioEstados
        '''
        self.id_nodo = id_nodo
        self.lista_objetivo = lista_objetivo
        lista_ordenada = self.lista_objetivo.copy()
        aux = []
        aux.append(int(self.id_nodo))
        for i in lista_ordenada:
            aux.append(int(i))
            aux.sort()
        lista_ordenada.clear()
        for i in aux:
            lista_ordenada.append(str(i))
        cod = hl.md5()
        for i in lista_ordenada:
            cod.update(i.encode('UTF-8'))
        self.id_md5 = cod.hexdigest()

class EspacioEstados():
    '''
    espacio donde guardamos los estados
    '''
    def __init__(self, grafo, estado):
        '''
        contructor de la clase EspacioEstados
        '''
        self.__grafo = grafo
        self.__estado = estado

    def esta(self, estado):
        '''
        comprueba si el estado esta en el espacio de estados
        '''
        return self.__grafo.pertenece_nodo(estado.id_nodo)

    def sucesores(self, nodo):
        '''
        busca los sucesores del estado y los devuelve
        '''
        ln = []
        self.__estado = nodo.estado
        id_nodo = self.__estado.id_nodo
        if self.__grafo.pertenece_nodo(id_nodo):
            for i in dict(self.__grafo.grafo[nodo.estado.id_nodo]).items():
                id_nodo = i[0]
                lista = nodo.estado.lista_objetivo.copy()
                if id_nodo in nodo.estado.lista_objetivo:
                    lista.remove(id_nodo)
                ln.append([i[1][0].get('name'),[id_nodo,lista],i[1][0].get('length')])
            return ln

        print(f"el id  {id_nodo} no se encuentra en el nodo")
        os._exit(1)
    
    def distance(self, idNode1, idNode2):

        (lng1,lat1) = self.__grafo.posicion_nodo(idNode1)
        (lng2,lat2) = self.__grafo.posicion_nodo(idNode2)
        earth_radious=6371009

        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        d_phi = phi2 - phi1
        theta1 = math.radians(lng1)
        theta2 = math.radians(lng2)
        d_theta = theta2 - theta1
        h = math.sin(d_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_theta/2)**2
        h=min(1.0,h)
        arc = 2 * math.asin(math.sqrt(h))
        dist = arc * earth_radious
        return dist

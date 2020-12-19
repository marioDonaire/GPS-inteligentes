#!/usr/bin/python3
'''
codigo de la parte 2
'''
import os
import json
from Estados import EspacioEstados
from Estados import Estado
from grafo import Grafo

class Problema():
    '''
    clase problema
    '''
    def __init__(self, ruta_archivo=None):
        '''
        contructor de la clase problema,leemos el json
        y creamos el estado inicial y el espacio de estados
        '''
        if ruta_archivo is None:
            print("No se ha pasado ninguna ruta para el json")
        else:
            with open(ruta_archivo) as file:
                data = json.load(file)
                grafo = Grafo(data['graphlmfile'])
                nodo = data['IntSt']['node']
                lista_nodos = data['IntSt']['listNodes']
            self.estado_inicial = Estado(nodo, lista_nodos)
        self.espacio_estados = EspacioEstados(grafo, self.estado_inicial)

    def es_objetivo(self, lista_objetivo):
        '''
        devuelve true si la lista esta vacia,sino devulve false
        '''
        if lista_objetivo:
            return False
        return True




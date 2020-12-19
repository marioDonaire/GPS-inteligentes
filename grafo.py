#!/usr/bin/python3
'''
tiene la clase grafo de la tarea 1
'''
import networkx as nx
import os

class Grafo():
    '''
    Le pasamos la ruta para leer el grafo y lo crea
    '''
    def __init__(self, Name=None):
        '''
        contructor de la clase grafo
        '''
        if Name is None:
            print("No se ha pasado una ruta para leer el grafo")
        else:
            self.grafo = nx.read_graphml(Name)

    def pertenece_nodo(self, id_nodo=None):
        '''
        devuelve true o false si el nodo esta en el grafo
        '''
        lista_nodos = nx.nodes(self.grafo)
        if id_nodo in lista_nodos:
            return True
        print(f"el nodo {id_nodo} no se encuentra en el grafo")
        os._exit(1)

    def posicion_nodo(self, nodo=None):
        '''
        devuelve la posicion del nodo en el grafo
        '''
        dicattr_x = nx.get_node_attributes(self.grafo, "x")
        dicattr_y = nx.get_node_attributes(self.grafo, "y")
        return float(dicattr_x.get(nodo)), float(dicattr_y.get(nodo))

    def adyacentes_nodo(self, nodo=None):
        '''
        devuelve los nodos vecinos del nodo en el grafo
        '''
        return nx.neighbors(self.grafo, nodo)

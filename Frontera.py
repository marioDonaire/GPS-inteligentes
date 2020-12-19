#!/usr/bin/python3
from abc import ABCMeta, abstractmethod
from sortedcontainers import SortedKeyList
from Nodo_arbol import NodoArbol
class Frontera(metaclass=ABCMeta):
    '''
    clase abstracta frontera
    '''
    @abstractmethod
    def __init__(self):
        '''
        crea la frontera
        '''
        raise NotImplementedError()
    @abstractmethod
    def añadir(self, nodo_arbol):
        '''
        añade un nudo a la frontera
        '''
        raise NotImplementedError()

    @abstractmethod
    def crea_frontera(self):
        '''
        crea una frontera
        '''
        raise NotImplementedError()

    @abstractmethod
    def eliminar(self):
        '''
        devuelve el primer nodo de la frontera
        y lo elimina de la misma
        '''
        raise NotImplementedError()

    @abstractmethod
    def es_vacia(self):
        '''
        devuelve un true si es vacia y false si no es asi
        '''
        raise NotImplementedError()

class FronteraPila(Frontera):
    '''
    clase donde definimos frontera
    '''
    def __init__(self):
        self._frontier = self.crea_frontera()

    def crea_frontera(self):
            frontier = SortedKeyList(key=NodoArbol.get_f)
            return frontier

    def añadir(self, node):
        if isinstance(node, NodoArbol):
            self._frontier.add(node)
        else:
            print("Error. No es un nodo.")

    def eliminar(self):
        return self._frontier.pop(0)

    def es_vacia(self):
        if bool(self._frontier):
            return False
        return True
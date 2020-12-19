#!/usr/bin/python3
class NodoArbol():
    '''
    nodo del arbol de busqueda
    '''
    def __init__(self, padre, estado, coste, accion, p, f):
        '''
        contructor de la clase NodoArbol
        '''
        self.padre = padre
        self.estado = estado
        self.coste = coste
        self.accion = accion
        self.profundidad = p
        self.f = f

    def get_f(self):
        return self.f

#!/usr/bin/python3
'''
codigo de la tarea 3
'''
from io import open
import os
from Nodo_arbol import NodoArbol
from Frontera import FronteraPila
from Estados import Estado


class Stack:
    '''
    crea una pila
    '''
    def __init__(self):
        '''
        inicia la pila
        '''
        self.items = []

    def is_empty(self):
        '''
        comprueba si esta vacia
        '''
        return self.items == []

    def push(self, item):
        '''
        push
        '''
        self.items.append(item)

    def pop(self):
        '''
        pop
        '''
        return self.items.pop()

    def peek(self):
        '''
        peek
        '''
        return self.items[len(self.items)-1]

    def size(self):
        '''
        size
        '''
        return len(self.items)



class Solucionador:
    '''
    clase que crea una solucion al problema
    '''
    def __init__(self, problema, estrategia, prof_max):
        '''
        inicia los valores del problema para solucionarlo
        '''
        self.frontera = FronteraPila()
        self.frontera.crea_frontera()
        nodo_inicial = NodoArbol(None, problema.estado_inicial, 0, str(f"None 0 0 0\nEstoy en {problema.estado_inicial.id_nodo} y quiero visitar {problema.estado_inicial.lista_objetivo}\n\n"), 0, 0)
        self.frontera.añadir(nodo_inicial)
        self.solucion = False
        self.__cnt_nodos = 0
        self.__poda = {}
        solucion = self.solucionar(problema, estrategia, prof_max)
        if solucion is None:
            print("No se ha encontrado solucion")
        else:
            self.imprimir_solucion(estrategia, solucion)


    def solucionar(self, problema, estrategia, prof_max):
        '''
        crea la soluciona, si la hay
        '''
        while not self.solucion and  not self.frontera.es_vacia():
            nodo_actual = self.frontera.eliminar()
            if problema.es_objetivo(nodo_actual.estado.lista_objetivo):
                self.solucion = True
            else:
                if problema.espacio_estados.esta(nodo_actual.estado):
                    ls = problema.espacio_estados.sucesores(nodo_actual)
                    ln = self.crear_lista_nodo_arbol(ls,nodo_actual,prof_max, estrategia, problema)
                    for i in ln: 
                        self.frontera.añadir(i)
        return nodo_actual
    
    def crear_lista_nodo_arbol(self, ls, nodo_actual, prof_max, estrategia, problema):
        '''
        crea la lista de nodos del arbol
        '''
        ln = []
        for i in ls:
            '''
            i[1][0] id nodo hijo
            i[1][1] lista de ids por recorrer
            i[2] coste 
            '''
            self.__cnt_nodos += 1
            inicio = str(f"Estoy en {i[1][0]} y tengo que visitar {i[1][1]}\n\n")
            coste = float(i[2])
            calle = i[0]
            estado = Estado(i[1][0],i[1][1])
            valor = self.calcular_f(estrategia, nodo_actual, coste,problema.espacio_estados, i[1][0])
            accion = str(f"{nodo_actual.estado.id_nodo} --> {i[1][0]} ({calle}) {valor} {nodo_actual.profundidad + 1} {coste + nodo_actual.coste}\n")
            nuevo = NodoArbol(nodo_actual,estado,coste + nodo_actual.coste, accion + inicio, nodo_actual.profundidad + 1, valor)
            if self.poda(estado.id_md5, valor):
                ln.append(nuevo)
        return ln

    def poda(self, id_md5, valor):
        '''
        hace la poda del arbol
        '''
        if not id_md5 in self.__poda:
            self.__poda[id_md5] = valor
            return True
        if self.__poda.get(id_md5) > valor:
            self.__poda.pop(id_md5)
            self.__poda[id_md5] = valor
            return True
        return False

    def calcular_f(self, estrategia, padre, coste, ee, id_hijo):
        '''
        calcula la f de cada nodo
        '''
        g = 0
        h = 0
        if estrategia == "Anchura":
            g = padre.profundidad + 1
            return g 
        if estrategia == "Costo uniforme":
            g = padre.coste + coste
            return g 
        if estrategia == "Profundidad simple":
            g = -(padre.profundidad + 1)
            return g 
        if estrategia == "Profundidad iterativa":
            #falta hacerla iterativa
            g = -(padre.profundidad + 1)
            return g 
        if estrategia == "Profundidad acotada":
            #falta hacer profundidad acotada
            g = -(padre.profundidad + 1)
            return g 
        if estrategia == "Voraz":
            h = ee.distance(padre.estado.id_nodo,id_hijo)
            return  h
        if estrategia == "A*":
            h = ee.distance(padre.estado.id_nodo,id_hijo)
            g = padre.coste + coste
            return g + h
        

    def imprimir_solucion(self, estrategia, nodo):
        '''
        imprime la solucion en un archivo txt llamado solucion
        '''
        fichero = open("solucion.txt", 'w')
        fichero.write(str(f'Estrategia: {estrategia}\nTotal de nodos generados: {self.__cnt_nodos}\nProfundidad: {nodo.profundidad + 1}\ncosto: {nodo.coste}\n\n\n'))
        pila = Stack()

        aux = nodo
        while aux.padre is not None:
            pila.push(aux)
            aux = aux.padre
        pila.push(aux)
        while not pila.is_empty():
            escribir = pila.pop()
            fichero.write(str(escribir.accion))
        fichero.close()

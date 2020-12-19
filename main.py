#!/usr/bin/python3
from Problema import Problema
from Solucionador import Solucionador

def main():
    switch = {0:"Anchura", 1:"Costo uniforme", 2:"Profundidad simple", 3:"Profundidad iterativa", 4:"Profundidad acotada",5:"Voraz",6:"A*"}
    json = input("Inserte el nombre del json: ")
    problema = Problema(str(f"json/{json}.json"))
    num = input("Que estrategia quieres usar?\n0.Anchura\n1.Costo Uniforme\n2.Profundidas simple\n3.Profundidad iterativa\n4.Profundidad recursiva\n5.Voraz\n6.A*\n")
    estrategia =switch.get(int(num))
    num = input("Profundidad maxima:")
    Solucionador(problema, estrategia, int(num))
    print("Solucion creada")




if __name__ =='__main__':
    main()
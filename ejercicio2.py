import sys
from ast import main

def imprimir_elemento_lista(lista, posicion):
    try:    
        return lista[posicion]

    except IndexError:
        print ("La lista tiene {} elementos, no existe el de la posicion {}".format(len(lista),posicion))
        return "Operación no válida"
#En este caso el tipo de error será de índice, por lo que se pondrá IndexError, para indicar por pantalla que es un error de indice y que continue
#ejecutándose el resto del código.

def main():
    lista=[4, 7, 30, 23, 5]
    posicion=10
    elemento=imprimir_elemento_lista(lista, posicion)
    print(elemento)

if __name__=="__main__":
    main()
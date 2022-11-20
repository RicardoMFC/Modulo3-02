import sys
from ast import main

def imprimir_clave_valor(lista, pais):
    try:    
        return lista[pais]

    except KeyError:
        print ("Esa clave no está en el diccionario")
        return "Operación no válida"
#En este otro caso se intenta acceder a un diccionario con una clave que no está definida en el diccionario, por lo que el tipo de error será KeyError

def main():
    paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
    clave="alemania"
    resultado=imprimir_clave_valor(paises, clave)
    print(resultado)

if __name__=="__main__":
    main()



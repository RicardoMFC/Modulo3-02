import sys
from ast import main

def dividir(a,b):
    try:    
        return a/b

    except ZeroDivisionError:
        print ("No se puede dividir entre cero")
        return "Operación no válida"
    
#En la función dividir se van a pasar dos valores a y b, que se van a dividir. En caso de que b=0 se va a ejecutar el except ya que sería un error del 
#tipo ZeroDivisionError en caso de que el error fuera otro, lo que hay dentro del except no se ejecutará, por tanto se dejará de ejecutar todo el código. 
#Lo que conseguimos con el except ZeroDivisionerror, es que no se deje de ejecutar el programa en caso de que b=0. No nos devolverá la división ya que 
#no se puede hacer pero el resto del código se seguirá ejecutando.

def main():
    numerador=7
    denominador=0
    resultado=dividir(numerador,denominador)
    print(resultado)

if __name__=="__main__":
    main()
import sys
from ast import main

def suma(a, b):
    try:    
        return a+b
    except TypeError:
        print ("Hay un elemento de tipo str por lo que no se puede realizar la suma")
        return "Operación no válida"
#Si alguno de los numeros introducidos es de tipo str y queremos realizar la suma de estos, no podremos, para que se siga ejecutando nuestros programa
#utilizaremos el except TypeError (se ejercutará siempre que sea un eror de ese tipo), mediante el cual mostraremos por pantalla que hay algún elemento 
#que es de tipo str y que nos permitirá seguir ejecutando el resto del código. Lo que devolverá la función suma será emtonces Operación no válida.

def transformacion_a_enteros(a, b):
    if type(a)==str:
        a=int(a)
        print("El numero1 era de tipo str")
    else:
        b=int(b)
        print("El numero2 era de tipo str")
    return a,b
    
def main():
    numero1="2"
    numero2=10
    resultado=suma(numero1,numero2)
    print(resultado)

    if resultado=="Operación no válida":
        numero1, numero2 = transformacion_a_enteros(numero1, numero2)
        resultado=suma(numero1,numero2)
        print(resultado)

#Si resultado=Operación no válida, entonces llamaremos a la función transformacion_a_enteros y luego de nuevo a la función suma para que nos devuelva la 
#suma de los números, ya no podría salir error ya que el numero de tipo str se ha transformado a entero.
        
if __name__=="__main__":
    main()


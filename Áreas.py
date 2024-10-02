#importamos la la libreria Math
import math

#Se crean las funciones de las operaciones

def area_cuadrado():
    lado= ("Introdusca lo que mide el lado del cuadrado: ")
    return lado*lado

def area_rectangulo():
    base=("Introdusca la base: ")
    altura=("Introdusca la altura: ")
    return base*altura

def area_triangulo(): 
   base=("Introdusca la base: ")
   altura=("Introdusca la altura: ") 
   return base*altura/2

def area_trapecio():
    basemenor=("Introdusca la base menor: ")
    basemayor=("Introdusca la base mayor: ")
    altura=("Introdusca la altura: ")
    return basemayor+basemenor*altura/2

while True:
    print("Calcular Areas")
    print("Elija una opción")
    print("a) Area del cuadrado")
    print("b) Area del rectangulo")
    print("c) Area del triangulo")
    print("d) Area del trapecio")
    print("e) Salir")
    
    #pedimos la opcion al usuario
    opcion=input("Ingrese la opción(a,b,c,d,e):")

    #Ejecutamos la opcion correspondiente
    if opcion in ["a)","b)","c)","d)"]:

        if opcion=="a)":
            resultado= area_cuadrado
            lado=float (input("Ingresar lado del cuadrado: "))
            resultado= lado*lado
            print("el resultado es: ",resultado)

        elif opcion=="b)":
            resultado= area_rectangulo
            base=float (input("Introdusca la base: "))
            altura=float (input("Introdusca la altura: "))
            resultado= base*altura
            print("el resultado es: ",resultado)

        elif opcion=="c)":
            resultado= area_triangulo
            base=float (input("Introdusca la base: "))
            altura=float (input("Introdusca la altura: "))
            resultado= base*altura/2
            print("el resultado es: ",resultado)

        elif opcion=="d)":
            resultado= area_trapecio
            basemenor=float (input("Introdusca la base menor: "))
            basemayor=float (input("Introdusca la base mayor: "))
            altura=float (input("Introdusca la altura: "))
            resultado= basemayor+basemenor*altura/2
            print("el resultado es: ",resultado)

    elif opcion=="e)":
        print("Saliendo del programa")
        break
    else:
        print("Opción invalida")

    input("presione Enter para continuar...")

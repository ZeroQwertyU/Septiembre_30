#Crear menu con tre opciones:
#1. opcion 1: temperaturas
#2. opcion 2: datos de personas
#3. opcion 3: Salir
import os

def Temperaturas():
    print("***** Temperaturas *****")
    #INgresar n temperaturaas donde n es un numero ingresado por teclado
    #mostrar el promedio de las temperaturas ingresadas
    suma = 0
    veces = int(input("Cuantas temperaturas quiere ingresar?: "))
    for x in range(veces):
        tempe = float(input("Digite una temperatura: "))
        suma = suma + 1

    print("El promedio de las temperaturas ingresadas es: " , round((suma/veces),2))#al agregar un + hay que agregar el str  (cuando es "+" se coloca un str)
    pausa = input("presione una tecla")

def Personas():
    print("***** Datos de personas *****")


    pausa = input("presione una tecla")


seguir = True
while seguir:
    os.system("cls")
    print("1. Temperaturas")
    print("2. Datos de personas")
    print("3. Salir")
    op = int(input("Ingrese opcion 1 - 2 - 3: "))
    if(op==1):
        Temperaturas()
    elif(op==2):
        Personas()
    else:
        print("Finalizado")
        break


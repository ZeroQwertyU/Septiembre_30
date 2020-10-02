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
    #ingresar para n personas donde n es un numero ingresado por teclado: 
    #nombre y edad. Mostrar cuantas personas son mayores de edad y cuantas son menores de edad
    #subir a github la segunda version de lo programado con el siguiente commit:
    #"Se agrego opcion 2 al menu de python"

    mayor = 0
    menor = 0
    veces = int(input("Cuantas personas quiere ingresar?: "))
    for x in range(veces):
        nom = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad de la persona: "))
        if edad >= 18:
            mayor+=1
        elif edad < 18:
            menor+=1
    print("La cantidad de personas mayores de edad es: " + str(mayor))
    print("La cantidad de personas menores de edad es: " + str(menor))
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


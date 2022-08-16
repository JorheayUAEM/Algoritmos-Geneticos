
import random 

from transform import *

def principal():

    poblacion = int(input("Ingrese el numero de poblacion: "))

    ristra = int(input("Ingrese el numero de ristra: "))

    individuo = []

    for i in range(poblacion):
        binario = random.choices([0, 1], k = ristra)
        individuo.append(binario)
    
    decimales = binToDec(individuo) 

    reales = decToReal(decimales, ristra)

    adaptados = realToAdap(reales)

    for i in range(len(individuo)):
        numero = i + 1
        muestra = individuo[i]
        decimal = decimales[i]
        real = reales[i]
        adaptado = adaptados[i]
        print(f"Poblacion[{numero}]: {muestra} Decimal: {decimal} Real: {real} Adaptado: {adaptado}")

    adaptados.sort(reverse=True)
    print(f"Ruleta: {adaptados}")



principal()
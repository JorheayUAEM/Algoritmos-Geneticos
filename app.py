import random

from transform import *
from CruceDeUnPunto import cruceDeUnPunto

def principal():

    poblacion = int(input("Ingrese el numero de poblacion: "))
    ristra = int(input("Ingrese el numero de ristra: "))
    xmin = int(input("Ingresa X minima: "))
    xmax = int(input("Ingresa X maxima: "))

    individuo = []
    for i in range(poblacion):
        binario = random.choices([0, 1], k = ristra)
        individuo.append(binario)
    

    decimales = binToDec(individuo) 
    reales = decToReal(decimales, ristra, xmax, xmin)
    adaptados = realToAdap(reales)

    frame = genFrame(individuo, decimales, reales, adaptados)
    print(frame)

    new_frame = cruceDeUnPunto(frame, poblacion, ristra, xmax, xmin)
    print(new_frame)


principal()
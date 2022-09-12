import math
import random
import pandas as pd 




def genCruce(long):
    num1 = random.randint(0, long-1)
    num2 = random.randint(0, long-1)
    if num1 == num2:
        num2 = random.randint(0, long-1)
    return num1, num2


def genHijos(individuo1, individuo2, corte):
    hijo1 = individuo1[-corte:]
    hijo2 = individuo2[-corte:]
    hijo_uno = []
    hijo_dos = []
    for i in range(len(individuo1) - corte):
        hijo_uno.append(individuo1[i])
        hijo_dos.append(individuo2[i])

    for i in hijo2:
        hijo_uno.append(i)

    for i in hijo1:
        hijo_dos.append(i)

    return hijo_uno, hijo_dos 


def getDecimal(binario):
    decimal = 0
    aux = 0
    binario = binario[::-1]
    for bin in binario:
        pot = 2**aux
        decimal += int(bin) * pot 
        aux += 1
    return decimal


def getReal(decimal, ristra, xmax, xmin):
    real = 0
    aux = (xmax - xmin) / (2**ristra - 1)
    auxdos = xmin + decimal
    real = auxdos * aux
    return real


def getAdap(real):
    aux = 4 * math.cos(real)
    part = 2 * (real**2)
    res = aux + part
    return res


def mutacion(frame, ristra, xmax, xmin):
    indice = int(input("Ingrese el indice a mutar: "))
    indice = indice -1
    bit = int(input("Ingrese el bit a mutar: "))
    individuo = frame.iloc[indice]["INDIVIDUO"]
    temp_list = []
    for i in reversed(individuo):
        temp_list.append(i)
    if temp_list[bit -1] == 1:
        temp_list[bit -1] = 0
    elif temp_list[bit -1] == 0:
        temp_list[bit -1] = 1
    individuo_mutado = []
    for i in reversed(temp_list):
        individuo_mutado.append(i)
    #VALORES DEL INDIVIDUO MUTADO
    dec_uno = getDecimal(individuo_mutado)
    real_uno = getReal(dec_uno, ristra, xmax, xmin)
    adap_uno = getAdap(real_uno)

    frame.at[indice, 'INDIVIDUO'] = individuo_mutado
    frame.loc[indice, 'DECIMAL'] = dec_uno
    frame.loc[indice, 'REAL'] = real_uno
    frame.loc[indice, 'ADAPTADO'] = adap_uno

    return frame


def cruceDeUnPunto(frame, long, ristra, xmax, xmin):
    estabilidad = float(input("Ingrese la estabilidad: "))
    corte = int(input("Ingrese el punto de corte: "))
    cant_cruces = (long * estabilidad) / 100
    cant_cruces = round(cant_cruces)
    print(f"La cantidad de cruces es: {cant_cruces}")
    for i in range(cant_cruces):
        ind1, ind2 = genCruce(long)
        padre_uno = frame.iloc[ind1]["INDIVIDUO"]
        padre_dos = frame.iloc[ind2]["INDIVIDUO"]
        hijo_uno, hijo_dos = genHijos(padre_uno, padre_dos, corte)
        #VALORES DE HIJO UNO
        dec_uno = getDecimal(hijo_uno)
        real_uno = getReal(dec_uno, ristra, xmax, xmin)
        adap_uno = getAdap(real_uno)
        #VALORES DE HIJO DOS
        dec_dos = getDecimal(hijo_dos)
        real_dos = getReal(dec_dos, ristra, xmax, xmin)
        adap_dos = getAdap(real_dos)
        if adap_uno > adap_dos:
            frame.at[ind2, 'INDIVIDUO'] = hijo_uno
            frame.loc[ind2, 'DECIMAL'] = dec_uno
            frame.loc[ind2, 'REAL'] = real_uno
            frame.loc[ind2, 'ADAPTADO'] = adap_uno
        else:
            frame.at[ind1, 'INDIVIDUO'] = hijo_dos
            frame.loc[ind1, 'DECIMAL'] = dec_dos
            frame.loc[ind1, 'REAL'] = real_dos
            frame.loc[ind1, 'ADAPTADO'] = adap_dos
    print(frame)
    frame = mutacion(frame, ristra, xmax, xmin)
    return frame
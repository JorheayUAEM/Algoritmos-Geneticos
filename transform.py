import math

def binToDec(binarios):
    decimales = []
    for binario in binarios:
        decimal = 0
        aux = 0
        binario = binario[::-1]
        for bin in binario:
            pot = 2**aux
            decimal += int(bin) * pot 
            aux += 1
        decimales.append(decimal)

    return decimales


def decToReal(decimales, ristra):
    
    xmin = int(input("Ingresa X minima: "))
    xmax = int(input("Ingresa X maxima: "))
    reales = []
    for decimal in decimales:
        aux = (xmax - xmin) / (2**ristra - 1)
        auxdos = xmin + decimal
        real = auxdos * aux
        reales.append(real)
    return reales


def realToAdap(reales):
    adapt = []
    for real in reales:
        aux = 4 * math.cos(real)
        part = 2 * (real**2)
        res = aux + part
        adapt.append(res)
    return adapt       

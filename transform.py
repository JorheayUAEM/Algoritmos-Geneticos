import math
import pandas as pd 

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


def decToReal(decimales, ristra, xmax, xmin):
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


def genFrame(ind, dec, rea, adap):
    df = pd.DataFrame()
    df["INDIVIDUO"] = ind
    df["DECIMAL"] = dec
    df["REAL"] = rea
    df["ADAPTADO"] = adap
    df = df.sort_values("ADAPTADO", ascending=False)
    df.reset_index(inplace = True, drop = True)
    return df

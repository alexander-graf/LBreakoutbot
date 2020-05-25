#!/usr/bin/env python

#Variable global?
fisting = 100


#Funktion definieren
def summe(*alle):
    print(fisting)
    s = 0
    for p in alle:
        s += p
    return s


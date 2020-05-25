#!/usr/bin/env python



#Funktion definieren
def fak(zahl):
    ergebnis = 1
    if zahl < 0:
        return None
    for i in range(2, zahl+1):
        ergebnis *= i
    return ergebnis



while True:
    eingabe = int(input("Gib Zahl ahlda: "))
    ergebnis = fak(eingabe)
    if ergebnis is None:
        print("Fehler")
    else:
        print(ergebnis)
    
    
    

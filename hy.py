#!/usr/bin/env python

geheimnis = 12
versuch = 0
zaehler = 0

while versuch != geheimnis:
    versuch = int(input("Rate mal: "))

    if versuch < geheimnis:
        print("zu klein")

    if versuch > geheimnis:
        print("zu groß")

    zaehler = zaehler + 1

print("super, du hast es in ", zaehler, " Versuchen geschafft")


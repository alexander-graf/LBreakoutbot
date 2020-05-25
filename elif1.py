geheimnis = 1338
versuch = -1
while versuch != geheimnis:
    versuch = int(input("Gib ne Zahl ein: "))
    if versuch == 0:
        print("Abbruch")
        break
else:
    print("Geschafft")
    

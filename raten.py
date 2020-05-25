geheimnis = 1338
versuch = -1
while versuch != geheimnis:
    versuch = int(input("Gib ne Zahl ein: "))
    if versuch == 0:
        print("Abbruch")
        break
    if versuch == 12:
        print("du hast 12 getippt")
        continue
    
else:
    print("Geschafft")
    

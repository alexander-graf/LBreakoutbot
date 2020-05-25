#!/usr/bin/python3

import os
import time
import sys
import datetime
import stat

a=1
accessTime1 = 1
accessTime2 = 1     #alles auf Start stellen

print("Deine ArgV ist: ", sys.argv[1])
ausfDatei = sys.argv[1]


while a==1:
    fileStatsObj =sys.argv[1]    #hier kommt die argv datei rein
    try:
        accessTime1 = os.path.getmtime (fileStatsObj)
    except:
        pass

    time.sleep(1)  # wartet 1 sekunde

    fileStatsObj = sys.argv[1]    #die Datei neu einlesen. evtl. Zeit anders
    try:
        accessTime2 = os.path.getmtime (fileStatsObj)
    except:
        pass

    if accessTime1 != accessTime2:
        #print ("Deine Datei heißt: ", sys.argv[1])
        os.system("python " + ausfDatei +  " 1")
        accessTime1 = 1
        accessTime2 = 1



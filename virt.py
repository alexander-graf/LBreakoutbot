
import virtkey
import time

keypress=virtkey.virtkey

time.sleep(2)

for i in range (1,100,1):
	print ("loop " + str(i))
	time.sleep(1)
	keypress(" ")     # <-- doesn't work, but doesn't return an error either

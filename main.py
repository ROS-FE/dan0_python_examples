#! /usr/bin/python2
# za izvajanje pozeni 
# chmod +x main.py
# ./main.py
import time #dodam modul za nadzor casa v programu
"""#############################
####Primer dodajanja modulov####
# ##############################"""
#from time import sleep
#from time import *
#import time as t


def main(): #Dodamo funkcijo main za omejitev scope
    print("moje besedilo") #primer print stavka
    print "test" #se en primer
    time.sleep(1.54213) #primer cakanja 1.54213 s
    print("Moje stevilo: %d" % 5) # primer formatiranja stevil v string - guglaj print formats python

if __name__ == "__main__": #preverimo ce je bil program zagnan kot modul ali program
    main() #kličemo funkcijo main
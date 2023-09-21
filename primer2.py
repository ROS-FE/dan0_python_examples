#! /usr/bin/python2
import time
from collections import deque

def main(): 
    #Zanka for kjer i zavzema vrednosti od 1 do 9
    for i in range(1, 10):
        print(str(i))
        
    #Zanka for po spisku (z indeksi) z uporabo funkcije range in len
    spisek = [2, 4, 5, 6, 2, 6]
    for j in range(len(spisek)):
        print(str(spisek[j]))
    
    #Malo bolj pythonska verzija for po spisku, kjer el zavzema vrednosti elementov v spisku
    for el in spisek:
        print(str(el))
        
    #Če potrebujemo indeks in element ju lahko dobimo tako
    for i, el in enumerate(spisek):
        print("ind %d: %d" % (i, el))

    #"List comprehension", ki s pomočjo for zanke izbere le elemente v spisku, ki so večji od 3
    spisek2 = [k for k in spisek if k > 3]
    print(repr(spisek2))
    
    dict1 = {"Peter": "0283213", "Franci": "9283726"} #dict()
    
    #Iteracija po slovarju (dictionary)
    for key, el in dict1.items():
        print(el + " " + key)
        
    #Iteracija po slovarju, kjer vrednost zanemarimo (zanima nas le ključ)
    for key, _ in dict1.items():
        print(key)
        
    #Dodajanje elemnta v slovar
    print(dict1["Peter"])
    dict1["Tilen"] = "ahkidai"
    print(repr(dict1))
    
    #Primer neskončnega while stavka
    try:
        while True:
            print("Beseda")
            time.sleep(1) #Dodamo nek sleep, da imajo tudi drugi procesi čas za izvajanje
    except KeyboardInterrupt: #Exception as e
        #V to kodo pridemo, če uporabnik pritisne ctrl + c
        pass #ne zgodi se nič
    finally:
        #ta koda se izvede na koncu, ne glede na to, ali je koda v try "crknila"
        print("Exiting")
        
    #Primer while s pogojem
    l = 10
    while l > 0:
        print(str(l))
        l -= 1
        
    #primer for s korakom po 2
    for m in range(0, 10, 2):
        print(str(m))
        
    #Primer for v negativno smer
    for n in range(10, 0, -1):
        print(str(n))
        
    #Kako v python2 uporabnik vnese string
    asjb = raw_input("Vpisi svoje ime:") #!python 2 posebnost, input izvede kodo!
    print(asjb)
    
    #Struktura deque se obnaša kot "circular buffer", parameter maxlen pove, kakšno je največje dovoljeno število elementov
    d = deque(maxlen=10)
    d.append("nekej")
    for o in range(1, 35):
        d.append(str(o))
        
    print(repr(d))
    #int()
    #float()
    
if __name__ == "__main__":
    main()
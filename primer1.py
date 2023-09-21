#! /usr/bin/python2
import time
from copy import copy, deepcopy # dodamo funkcije za kopiranje struktur

def main():
    spisek1 = ["Franci", "Peter", "Marusa"] #spisek z imeni (listi v pythonu so "linked lists")
    spisek2 = spisek1 #kompleksnejše strukture v pythonu so predstavljene s kazalci (pointerji)
    
    temp = spisek1.pop(1) # funkcija pop bo vplivala na oba spiska, ker vsebujeta site podatke (kopirali smo le kazalec kazalec)
    
    print(temp)
    print(repr(spisek1)) #repr lepo prikaže kompleskse python strukture
    print(repr(spisek2))
    
    spisek1.append(temp) #na zadnje mesto dodamo vrednost iz spremenljivke temp
    
    print("Spisek 1 po append: " + repr(spisek1))
    
    spisek3 = copy(spisek1) #funkcija copy kopira "prvi nivo" podatkov
    spisek3.pop(0) #pop vpliva samo na spisek3, ker smo te podatke fizično kopirali na drug sopmin
    #deepcopy kopira vse nivoje podatkov !pozor, računsko in spominsko zahtevna operacija!
    print("Spisek1: " + repr(spisek1))
    print("Spisek3: " + repr(spisek3))



if __name__ == "__main__":
    main()
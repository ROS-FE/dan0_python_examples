#! /usr/bin/python2

import time
from threading import Thread
import sys
from multiprocessing import Lock

global thr1running, mx
thr1running = False

def thr1():
    global thr1running, mx
    thr1running = True
    num = 1
    numPrev = 1
    while thr1running:
        mx.acquire()
        temp = num
        num = num + numPrev
        numPrev = temp
        print(num)
        sys.stdout.flush() #Poskrbimo, da se printi iz tega threada res izpišejo pravočasno
        time.sleep(5)
        mx.release()
        time.sleep(5)
        
def thr2():
    while True:
        print("Deamon thread")
        time.sleep(1)

def main():
    global thr1running, mx
    #mutex (Lock) nam pomaga pri sinhronizaciji več threadov. 
    mx = Lock()
    #Thread teče v posebnem procesu target kaže na funkcijo, ki se v threadu izvaja, vanjo lahko podamo argumente v tuplu args
    thr1obj = Thread(target=thr1, args=())
    thr1obj.start()
    
    #Daemon thread je vezan na glavni proces, ugasne se skupaj z njim
    thr2obj = Thread(target=thr2)
    thr2obj.setDaemon(True)
    thr2obj.start()
    
    try:
        while True:
            mx.acquire() #pridobimo dovoljenje za dostop do skupnih spremenljivk
            print("Main thread")
            time.sleep(0.5)
            mx.release() #sprostimo dovoljenje, da lahko do njih dostopa še kdo drug
            time.sleep(0.5)
    except KeyboardInterrupt:
        try:
            mx.release()
        except Exception as e:
            pass
        thr1running = False #threadu 1 sporočimo, naj se ugasne
        print("cakam na thread")
        thr1obj.join() #Počakamo, da se thread 1 zaključi (če se ne bomo čakali za vedno)
        print("izhod")

if __name__ == "__main__":
    main()
#! /usr/bin/python2
import time
from collections import deque

def main(): 
    for i in range(1, 10):
        print(str(i))
        
    spisek = [2, 4, 5, 6, 2, 6]
    for j in range(len(spisek)):
        print(str(spisek[j]))
        
    for el in spisek:
        print(str(el))
    
    for i, el in enumerate(spisek):
        print("ind %d: %d" % (i, el))

    spisek2 = [k for k in spisek if k > 3]
    print(repr(spisek2))
    
    dict1 = {"Peter": "0283213", "Franci": "9283726"} #dict()
    
    for key, el in dict1.items():
        print(el + " " + key)
        
    for key, _ in dict1.items():
        print(key)
        
    print(dict1["Peter"])
    dict1["Tilen"] = "ahkidai"
    print(repr(dict1))
    
    try:
        while True:
            print("Beseda")
            time.sleep(1)
    except KeyboardInterrupt: #Exception as e
        pass
    finally:
        print("Exiting")
        
    l = 10
    while l > 0:
        print(str(l))
        l -= 1
        
    for m in range(0, 10, 2):
        print(str(m))
        
    for n in range(10, 0, -1):
        print(str(n))
        
    asjb = raw_input("Vpisi svoje ime:") #!python 2 posebnost, input izvede kodo!
    print(asjb)
    
    d = deque(maxlen=10)
    d.append("nekej")
    for o in range(1, 35):
        d.append(str(o))
        
    print(repr(d))
    #int()
    #float()
    
if __name__ == "__main__":
    main()
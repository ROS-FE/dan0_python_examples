#! /usr/bin/python2

#Če hočemo, da se class lahko deduje, mora ta dedovati iz "object"
class Kvader(object):
    #atribut vseh objektov "Kvader"
    kajjeto="geometrijski objekt"
    
    #Funkcija ki se izvede ob inicializaciji
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def ploscina(self):
        return self.a * self.b
    
    # * pomeni poljubno št. navadnih argumentov v seznamu ** pa keyword argumente v dictu
    def mojafunkcija(*args, **kwargs):
        print(repr(len(args)))
        print(repr(kwargs))
    
    #def __del__():
    #    pass
    
#Kvadrat deduje iz Kvadra, prepiše se le __init__ -> ta vseeno kliče init svojega starša super()
class Kvadrat(Kvader):
    def __init__(self, a):
        super(Kvadrat, self).__init__(a, a)

    
def main(): 
    kv = Kvader(1.0, 2.0)
    print(repr(kv.ploscina()))
    kvadrat = Kvadrat(2.0)
    print(repr(kvadrat.ploscina()))
    kvadrat.mojafunkcija("fghj", "fghj", "jjjj", arg1="jbb", arg2="zqiowhol")
    
    

if __name__ == "__main__":
    main()
#! /usr/bin/python2

class Kvader(object):
    
    kajjeto="geometrijski objekt"
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def ploscina(self):
        return self.a * self.b
    
    def mojafunkcija(*args, **kwargs):
        print(repr(len(args)))
        print(repr(kwargs))
    
    #def __del__():
    #    pass
    
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
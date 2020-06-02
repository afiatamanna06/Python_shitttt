class Animal:
    def tell(self):
        print("I am animal.")
        

class Tiger(Animal):
    def tell(self):
        super().tell()
        print("I am Tiger.")
        
        
class Panther(Tiger):
    def tell(self):
        super().tell()
        print("I am Panther.")
        
        
animal = Animal()
animal.tell()
tiger = Tiger()
tiger.tell()
panther = Panther()
panther.tell()
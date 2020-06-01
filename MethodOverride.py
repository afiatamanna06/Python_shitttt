class Mobile:
    def __init__(self):
        print("I am mobile")
  
        
class Iphone(Mobile):
    def __init__(self):
        super().__init__()
        print("I am Iphone")
        

s = Iphone()
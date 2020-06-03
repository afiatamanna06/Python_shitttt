class Dumb:
    def tell(self):
        print("I am dumb.")


class Clever:
    def tell(self):
        print("I am clever.")


class Human(Dumb, Clever):
    def tell(self):
        super().tell()
        print("I am Human.")


human = Human()
human.tell()

class Methods:
    def public_method(self):
        print("Public method")
        self.__private_method()

    def __private_method(self):
        print("Private method")



method = Methods()
method.public_method()

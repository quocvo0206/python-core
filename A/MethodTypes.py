class MethodTypes:

    name = "Ragnar"

    def instanceMethod(self):
        # Creates an instance atribute through keyword self
        self.lastname = "Lothbrock"
        self.name = "QuocVV"
        print(self.name)
        print(self.lastname)

    # @classmethod
    # def classMethod(self):
    #     # Access a class atribute through keyword cls
    #     self.name = "Lagertha"
    #     print(self.name)

    @staticmethod
    def staticMethod():
        print("This is a static method")

# Creates an instance of the class
m = MethodTypes()
# Calls instance method
m.instanceMethod()
print(m.name)

#m.classMethod()
MethodTypes.staticMethod()
print(MethodTypes.name)
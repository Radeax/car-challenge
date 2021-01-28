class Car:
    def __int__(self, make=None, model=None, year=None, color=None):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def setMake(self, make):
        self.make = make

    def getMake(self):
        return self.make

    def setModel(self, model):
        self.model = model

    def getModel(self):
        return self.model

    def setYear(self, year):
        self.year = year

    def getYear(self):
        return self.year

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color


# Class Car:
# Object: Audi, Mercedes, Toyota, BMW, Tesla
# Properties: make, model, year, color

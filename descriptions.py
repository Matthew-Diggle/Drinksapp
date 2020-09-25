class Drink:
    def __init__(self, name, temp, carbonated):
        self.name = name
        self.age = 27
        self.temp = temp
        self.carbonated = carbonated
    #def is_carbonated():
        #return self.carbonated == "a soft drink"
    #def is_not_carbonated():
        #return self.is_carbonated == False
    def properties(self):
        soft_drink = "a soft drink"
        if not self.carbonated:
            soft_drink = "not a soft drink"
        print(f'{self.name} is {soft_drink} drink, served {self.temp}.')


class Tea(Drink):
    def __init__(self, name):
        self.temp = "hot"
        self.carbonated = False
        super().__init__(name, self.temp, self.carbonated)
    def properties(self):
        super().properties()
class Mocha(Drink):
    def __init__(self, name):
        self.temp = "hot"
        self.carbonated = False
        super().__init__(name, self.temp, self.carbonated)
    def properties(self):
        super().properties()
class Coffee(Drink):
    def __init__(self, name):
        self.temp = "hot"
        self.carbonated = False
        super().__init__(name, self.temp, self.carbonated)
    def properties(self):
        super().properties()
class Americano(Drink):
    def __init__(self, name):
        self.temp = "hot"
        self.carbonated = False
        super().__init__(name, self.temp, self.carbonated)
    def properties(self):
        super().properties()
class Coke(Drink):
    def __init__(self, name):
        self.temp = "cold"
        self.carbonated = True
        super().__init__(name, self.temp, self.carbonated)
    def properties(self):
        super().properties()
class Fanta(Drink):
    def __init__(self, name):
        self.temp = "cold"
        self.carbonated = True
        super().__init__(name, self.temp, self.carbonated)
    def properties(self):
        super().properties()

    

#Drink descriptions
def tea_properties():
    tea_properties = Tea("Tea")
    tea_properties.properties()
def mocha_properties():
    mocha_properties = Mocha("Mocha")
    mocha_properties.properties()
def coffee_properties():
    coffee_properties = Coffee("Coffee")
    coffee_properties.properties()
def americano_properties():
    americano_properties = Americano("Americano")
    americano_properties.properties()
def coke_properties():
    coke_properties = Coke("Coke")
    coke_properties.properties()
def fanta_properties():
    fanta_properties = Fanta("Fanta")
    fanta_properties.properties()

def all_properties():
    tea_properties()
    coffee_properties()
    mocha_properties()
    americano_properties()
    coke_properties()
    fanta_properties()
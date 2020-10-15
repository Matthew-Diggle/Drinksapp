class Drink:
    def __init__(self, drink_name, temp, blend):
        self.drink_name = drink_name
        self.temp = temp
        self.blend = blend
        if self.temp == "":
            self.temp = "Regular"
        if self.blend == "":
            self.blend = "Regular"
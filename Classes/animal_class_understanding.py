class Animal:
    def __init__(self, name):
        self.name = name
        self.age = 42
    def speak(self):
        print(f'My name is {self.name} and I am {self.age}')
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.type = "dog"
        self.breed = breed
    def speak(self):
        super().speak()
        print(f'I am a {self.type}')
class Labrador(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed)
        self.colour = "golden"
    def speak(self):
        super().speak()
        print(f'My furs is {self.colour}')
fish = Animal("George")
fish.speak()
cat = Animal("Whiskers")
cat.speak()
dog = Dog("Fido", "breed2")
dog.speak()
lab = Labrador("Paws", "breed2")
lab.speak()
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def speak(self):
        return f"{self.name} make a sound"
    
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks !"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows !"
    
    
dog = Dog("Rocky")
cat = Cat("Tom")


print(dog.speak())
print(cat.speak())


class Vehicule:
    def __init__(self, brand: str):
        self.brand = brand
    def info(self) :
        return f"Brand: {self.brand}"
    
class Car(Vehicule) :
    def __init__(self, brand, model : str):
        super().__init__(brand)
        self.model = model
        
    def info(self):
        return f"{super().info()}, Model: {self.model}"


car = Car("Porsche", "911 carrera 4")

print(car.info())


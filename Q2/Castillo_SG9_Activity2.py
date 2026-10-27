# 1. SINGLE INHERITANCE
print("--- 1. Single Inheritance ---")

class Animal:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Bark!"

my_dog = Dog("Bantay")
print(f"Dog Name: {my_dog.get_name()}")
print(f"Sound: {my_dog.make_sound()}\n")


# 2. MULTILEVEL INHERITANCE
print("--- 2. Multilevel Inheritance ---")

class Organism:
    def __init__(self, alive=True):
        self._alive = alive

    def get_alive(self):
        return self._alive

    def set_alive(self, alive):
        self._alive = bool(alive)

class Animal(Organism):
    def eat(self):
        return "Eating food..."

class Mammal(Animal):
    def feed_milk(self):
        return "Feeding milk to young..."

my_cat = Mammal()
print(f"Is alive?: {my_cat.get_alive()}")
print(my_cat.eat())
print(my_cat.feed_milk())
print()


# 3. HIERARCHICAL INHERITANCE
print("--- 3. Hierarchical Inheritance ---")

class Vehicle:
    def __init__(self, brand):
        self._brand = brand

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

class Car(Vehicle):
    def drive(self):
        return "Driving on four wheels"

class Motorcycle(Vehicle):
    def ride(self):
        return "Riding on two wheels"

my_car = Car("Toyota")
my_motor = Motorcycle("Yamaha")

print(f"Car Brand: {my_car.get_brand()} - {my_car.drive()}")
print(f"Motorcycle Brand: {my_motor.get_brand()} - {my_motor.ride()}")
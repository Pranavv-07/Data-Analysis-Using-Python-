# 2.3 Define a base class called Animal with a method make_sound(). Implement derived classes 
# Demonstrate polymorphism by calling the method on objects of different classes.
class AnimalBase:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement this method")


class DogPoly(AnimalBase):
    def make_sound(self):
        return "Woof!"


class CatPoly(AnimalBase):
    def make_sound(self):
        return "Meow!"


class BirdPoly(AnimalBase):
    def make_sound(self):
        return "Chirp!"


animals = [DogPoly(), CatPoly(), BirdPoly()]
for animal in animals:
    print(animal.make_sound())
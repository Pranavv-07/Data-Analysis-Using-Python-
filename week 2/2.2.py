# 2.2 Inheritance using animal class.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " makes a sound.")


class Dog(Animal):
    def speak(self):
        print(self.name + " barks!")


class Cat(Animal):
    def speak(self):
        print(self.name + " meows!")


class Bird(Animal):
    def speak(self):
        print(self.name + " chirps!")


dog = Dog("DOG")
cat = Cat("CAt")
bird = Bird("Bird")

dog.speak()
cat.speak()
bird.speak()
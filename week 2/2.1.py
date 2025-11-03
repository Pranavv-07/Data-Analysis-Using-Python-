class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
        print("The car has started.")

    def stop(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
        print("The car has stopped.")


my_car = Car("Honda", "BRV", 2022)
my_car.start()
my_car.stop()
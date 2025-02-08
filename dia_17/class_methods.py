class Car:
    def __init__(self):
        self.seats = 4

    def enter_race_mode(self):
        self.seats = 2

my_car = Car()

print(my_car.seats)
my_car.enter_race_mode()
print(my_car.seats)
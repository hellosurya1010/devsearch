from hashlib import new


class Car:
    wheels = 4
    doors = 4
    speed = 100
    
    def __init__(self, brand, model, fuel):
        self.fuel = fuel
        self.brand = brand
        self.model = model
    
    def description(self):
        print(self.model + self.brand + self.fuel )
        # print("This car is " + self.model + " model in " + self.brand " with " + self.fuel + "type.")

class SuperCar(Car):
    doors = 2
    speed = 400

bmwM3 = Car('bmw', 'M3','Petrol')

audiRs10 = SuperCar()

print(audiRs10.description)

# print(bmwM3.description())
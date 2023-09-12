class car:
    wheel=4
    def __init__(self):
        self.name="Jaguar"
        self.milage=15
car1=car()
car2=car()
car2.name="Range Rover"
car2.milage=12
car1.wheel=8
print(car2.wheel)
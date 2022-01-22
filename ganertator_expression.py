class Car:
    name = ""
    color = ""

    def __init__(self,name,color):
        self.name = name
        self.color = color

    def start(self):
        print("starting the engine")


my_car = Car()
my_car.name = "Allion"
print(my_car.name)
my_car.start()


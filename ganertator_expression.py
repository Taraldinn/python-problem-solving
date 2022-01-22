class Car:
    def __init__(self, n , c):
        self.name = n
        self.color = c

    def start(self):
        print("name: ", self.name)
        print("color: ",self.color)
        print("Starting the engine")



my_car1 =Car("Corolla", "White")
my_car1.start()
my_car2 = Car("premio","red")
my_car2.start()
my_car3 = Car("BMW", "Blue")
Car.start(my_car3)
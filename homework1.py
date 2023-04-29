class Car():
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0

    def get_speed(self):
        return self.speed


my_car = Car("new_model", "red")

print(my_car.model)
print(my_car.color)
print(my_car.speed)

my_car.accelerate(20)
print(my_car.get_speed())

my_car.brake(10)
print(my_car.get_speed())

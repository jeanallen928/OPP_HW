class Car():
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self, amount):
        return self.speed + amount

    def brake(self, amount):
        return self.speed - amount

    def get_speed(self):
        return self.speed

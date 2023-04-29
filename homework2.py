class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("동물 소리")


class Dog(Animal):
    def speak(self):
        print("왕왕")


class Cat(Animal):
    def speak(self):
        print("야옹")

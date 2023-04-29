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


husky = Dog("숙희", 5)
goldendoodle = Dog("Brodie", 4)
cat = Cat("영희", 9)

husky.speak()
print(goldendoodle.name)
cat.speak()
print(cat.age)

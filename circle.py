class Animal:
    def __init__(self,name):
        self.name = name

    def move(self):
        print("move")

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("멍멍")

class Duck(Animal):
    def speak(self):
        print("꽥꽥")




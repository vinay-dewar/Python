"""Inheritance allows a class (child class) to inherit attributes and methods from
another class (parent class)."""


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("from dog class speak method")

class Cat(Dog):

    def speak(self):
        print(" from cat speck method")

dog =Cat("tom")
dog.speak()

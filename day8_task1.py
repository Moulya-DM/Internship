# Task 1 (Abstraction) – Simple Problem Statement
# Problem: Animal Sound System
# You want to create an Animal system where every animal must make a sound.
# What to do
# Create an abstract class Animal
# Create an abstract method sound()
# Create a normal method sleep() (common for all animals)
# Then create child classes:
# Dog → sound() prints Bark
# Cat → sound() prints Meow
# Cow → sound() prints Moo
# How it works
# Animal class will force all child classes to write their own sound()
# But sleep() is common so it can be used directly.


from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    # Normal (concrete) method
    def sleep(self):
        print("Animal is sleeping.")


# Child class: Dog
class Dog(Animal):
    def sound(self):
        print("Dog says: Bark")


# Child class: Cat
class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")


# Child class: Cow
class Cow(Animal):
    def sound(self):
        print("Cow says: Moo")


# Testing the program

dog = Dog()
cat = Cat()
cow = Cow()

print("---- Animal Sound System ----")
dog.sound()
dog.sleep()

cat.sound()
cat.sleep()

cow.sound()
cow.sleep()

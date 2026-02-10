# Task-2: Abstraction – Vehicle System
# Problem Statement
# Create a program for a Vehicle System using Abstraction.
# Requirements
# Create an abstract class Vehicle
# abstract method: start_engine()
# Create child class Car
# implement start_engine()
# Create child class Bike
# implement start_engine()
# Create child class Bus
# implement start_engine()
# Create objects and call start_engine() method.

from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass


# Child class: Car
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with key or button.")


# Child class: Bike
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started with self-start or kick.")


# Child class: Bus
class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started with heavy-duty ignition.")


# Testing Abstraction

car = Car()
bike = Bike()
bus = Bus()

print("---- Vehicle System ----")
car.start_engine()
bike.start_engine()
bus.start_engine()

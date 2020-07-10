# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle(): #Base Class
        pass

class FlightVehicle(Vehicle):
        pass     

class Starship(FlightVehicle):
        pass     

def GroundVehicle(Vehicle):
        pass     

def Airplane(FlightVehicle):
        pass     

def Car(GroundVehicle):
        pass     

def Motorcycle(GroundVehicle):
        pass     
"""
Calculate the gravitational force between Earth and Venus
"""
#import math


#A basic print command
print ('My name\'s Ashish')


# A calculation showing how you calculate force

G = 6.67e-11  # Gravitational constant
mass_1 = 6e24  # in kg (mass of Earth)
mass_2 = 4.9e24  # in kg (mass of Venus)
distance = 4.1e10  # in m (distance between Earth and Venus)

force = G*mass_1*mass_2/(distance**2)  # <-- Replace with your code
print(force)

# An example of how to take user input
name = input("Who's birthday is it?")
print ("Happy Birthday to you \nHappy Birthday to you \nHappy Birthday dear " + name + "!" + "\nHappy Birthday to you!")

#An example of converting temperature from F to C
temp_f = float(input("Temperature in F: "))
temp_c = (temp_f - 32) * 5/9
temp_c = round(temp_c)

print(f"Temperature in C: {temp_c} ")


#Some more calculations of circumference by creating methods.
from math import pi

def area(r):
    return pi *r**2

def circumference(r):
    return 2* pi * r
    
radius = float(input("Circle radius: "))
    
my_area = area(radius)

print(f'Area: {my_area}')
print(f'Circumference: {circumference(radius)}')



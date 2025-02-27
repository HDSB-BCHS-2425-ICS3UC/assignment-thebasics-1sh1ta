"""
Write a program that calculates the volume of the three-dimensional shapes mentioned to the right.
It should take as input the parameter(s) necessary to calculate the volume (A, r , h ).
You should take in each variable you need in turn. Ie. for the cube, take in the length, for the sphere, take in the radius, etc…
The output should be USER FRIENDLY.
"""

import math

# Set value for name
name  = str(input("What is your name? \n"))

# Print message
print (f"Hi {name}! Welcome to the 3D Shape Volume Calculator!")
shape = str(input("What shape would you like to start with?"))
shape = shape.lower

if shape == "cube":
    A = float(input("What is the length of an edge of the cube?"))
    cube_volume = int(A**3)
    print ("The volume of this cube is:", cube_volume)

elif shape == "sphere":
    r = float(input("What is the radius of this sphere?"))
    sphere_volume = int((4/3)*math.pi*r**3)
    print ("The volume of this sphere is:", sphere_volume)

elif shape ==  "cone":
    r = float(input("What is the radius of this cone?"))
    h = float(input("What is the height of this cone?"))
    cone_volume = int((1/3)*math.pi*r**2*h)
    print ("The volume of the cone is: ", cone_volume)

elif shape == "cylinder":
    r = float(input("What is the radius of this cylinder?"))
    h = float(input("What is the height of this cylinder?"))
    cylinder_volume = int((1/3)*math.pi*r**2*h)
    print ("The volume of the cone is: ", cylinder_volume)
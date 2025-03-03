
#Author: Ishita Malhotra
#Date Modified: March 3, 2025
#Description: Calculating the volume of a cube, sphere, cone, and cylinder using user input

import math

# Set value for name
name  = str(input("What is your name? \n"))

# Print message
print (f"Hi {name}! Welcome to the 3D Shape Volume Calculator!")
shape = input("What shape would you like to start with?\n")
shape = shape.lower()

if shape == "cube":
    A = float(input("What is the length of an edge of the cube?\n"))
    cube_volume = float(A**3)
    print ("The volume of this cube is:", cube_volume)

elif shape == "sphere":
    r = float(input("What is the radius of this sphere?\n"))
    sphere_volume = float((4/3)*math.pi*r**3)
    print ("The volume of this sphere is:", sphere_volume)

elif shape ==  "cone":
    r = float(input("What is the radius of this cone?\n"))
    h = float(input("What is the height of this cone?\n"))
    cone_volume = float((1/3)*math.pi*r**2*h)
    print ("The volume of the cone is: ", cone_volume)

elif shape == "cylinder":
    r = float(input("What is the radius of this cylinder?\n"))
    h = float(input("What is the height of this cylinder?\n"))
    cylinder_volume = float(math.pi*r**2*h)
    print ("The volume of the cone is: ", cylinder_volume)

else:
    print ("Error! It looks like you have inputted an incorrect shape. Please check your spelling and run the code again.")
    print = (shape)
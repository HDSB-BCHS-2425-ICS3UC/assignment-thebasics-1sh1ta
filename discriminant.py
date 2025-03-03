
#Author: Ishita Malhotra
#Date Modified: March 3, 2025
#Description: Calculating the discriminant using user input 


# Requesting user for the "a" input
print("Welcome to the discriminant calculator!\nA discriminant is a tool used in quadratics that identifies how many roots are in an equation.\nA positive value means that there are two roots (or x-intercepts) in that quadratic equation.\nA value of zero means that there is only one root in that equation.\nA negative value means that there are no roots in the equation.\nThe discriminant uses standard form for quadratics, which looks like: ax^2 + bx + c\nPlease enter the 'a' value then press Enter: ")
a = float(input())

# Requesting user for the "b" input
print("Enter b then press Enter: ")
b = float(input())

# Requesting user for the "c" input
print("Enter c then press Enter: ")
c = float(input())

# Equation to calculate the discriminant
discriminant = b**2 - 4*a*c

# Printing the discriminant
print("Your discriminant is:", discriminant,"!")
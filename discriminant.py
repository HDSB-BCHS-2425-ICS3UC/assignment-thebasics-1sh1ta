"""
Write a program that finds the Discriminant
Delta = b^2 – 4ac
The output should be similar to the following (Difficulty Mark 3):

Enter a and then press Enter: 4
Enter b and then press Enter: 2
Enter c and then press Enter: 2
The Discriminant is -28
"""

# Requesting user for the "a" input
print("Welcome to the discriminant calculator!\nA discriminant is a tool used in quadratics that identifies hwo many roots are in an equation.\nA positive value means that there are two roots (or x-intercepts) in that quadratic equation.\nA value of zero means that there is only one root in that equation.\nA negative value means that there are no roots in the equation.\nThe discriminant uses standard form for quadratics, which looks like: ax^2 + bx + c\nPlease enter the 'a' value then press Enter: ")
a = int(input())

# Requesting user for the "b" input
print("Enter b then press Enter: ")
b = int(input())

# Requesting user for the "c" input
print("Enter c then press Enter: ")
c = int(input())

# Equation to calculate the discriminant
discriminant = b**2 - 4*a*c

# Printing the discriminant
print("Your discriminant is:", discriminant,"!")
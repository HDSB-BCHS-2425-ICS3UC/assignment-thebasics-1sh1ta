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
print("Enter a then press Enter: ")
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
print("The Discriminant is:", discriminant)


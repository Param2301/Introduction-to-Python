#Task 1: Variables: Your First Python Intro
Name="Param"
Age=22
Height=5.2

print(f"Hey everybody, my name is {Name}! I'm {Age} years old and {Height} feet tall.")

#Task 2 : Operators: Playing with Numbers

num1 = 30
num2 = 3

print(f"The sum of {num1} and {num2} is {num1+num2}")

print(f"The difference between {num1} and {num2} is {num1-num2}")

print(f"The product of {num1} and {num2} is {num1*num2}")

print(f"The result of dividing {num1} by {num2} is {num1/num2}")

#Task 3 Conditional Statements: The Number Checker

number = float(input("Please enter a number: "))

if number>0:
    print("This number is positive. Awesome!")
elif number<0:
    print("This number is negative. Better luck next time!") 
else:
    print("Zero it is. A perfect balance!")
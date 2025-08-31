print("Hello Python")

# to execute, use code runner or (Shift + enter by selecting perticular code) 

# Single Line Comment

"""
This
is a
multi-line
comment
"""

"""
1. Comments in python are denoted by the # symbol
2. Any text after the # symbol on the same line is ignored by the interpreter
3. Comments are used to explain the code and make it easier to understand
4. Comments can be used to disable a block of code temporarily
5. Comments can be used to document the code and make it easier to understand for other developers
"""

#-------------------------------------------- Session -2 -------------------------------------------------
"""
1. What is Python Programming?

Python is a high-level, interpreted, general-purpose programming language. 
It was designed to be easy to read and write, making it ideal for beginners and 
professionals alike.
Python is popular in web development, data science, automation, AI/ML, game development, 
and much more.

Real-Life Examples:
1. Instagram and YouTube use Python for backend.
2. Python scripts are used to automate Excel reports.
3. You can create chatbots, calculators, games, and apps.

"""

# Using print() Function
print("Hello, World!") 

# print() used for message printing/ to display output 
print("Hello Students ! Welcome to Python Session-2")

# print your name
print("My Name is Rohan")

"""
Python is a case sensitive language.
ex - Name, name, NAME, NamE will be treated as different words
"""

#---------------------------------------------- Variables ------------------------------------------------
""" 
Variables are used to store data in Python that can be used later, it works as a container.
In Python, you don’t need to declare the type.
You can assign a value to a variable using the assignment operator (=).

Rules/Naming Convention :
1. Must start with a letter or underscore (ex- name, _name)
2. Can’t start with a number (ex- 1name)
3. Can include letters, digits, underscores
4. Can’t include spaces or special characters
5. Can’t be a reserved keyword (ex- if, else, for, while)
"""

name = "Shalini"
age = 27
height = 155.5

print("Name:", name)
print("Age:", age)
print("Height:", height)

# add two numbers
a=1
b=1
sum = a+b
print(sum)
print("sum")
print("sum : ",sum)  # This will print the sum of a and b

# multiply two numbers
c=2
d=3
print("product : ",c*d)

# String Concatenation
first_Name = "Shalini"
last_Name = "Verma"
full_Name = first_Name + last_Name
full_Name = first_Name +" "+ last_Name
print(full_Name)

# print information of a Employee
Name = "Riya Agrawal"
Age = 20
Gender = "Female"
Position = "Software Engineer"
Salary = 60000

print("information of a Employee : ")
print("Name : ",Name)
print("Age : ",Age)
print("Gender : ",Gender)
print("Position : ",Position)
print("Salary : ",Salary)

# print information of Yourself


# Print with Multiple Arguments
name = "Shalini"
age = 27
print("Name:", name, "Age:", age)

# Using String Concatenation (+)
first = "Hello"
second = "World"
print(first + " " + second)

# print multiple sentences together (\n escape sequence used for new line)
print("Hello Students, Welcome to python session-2\nThis is my first python program\n")

#String Concatenation
print("Hello Students, Welcome to python session-2" + "This is my first python program")

"""
Keywords -->

Keywords are reserved words that have a special meaning in Python. 
They cannot be used as variable names.

Examples:
False, True, None, if, else, elif, while, 
for, break, continue, def, return, import, 
as, class, try, except

"""

# Using some keywords in a program
is_Married = True
print(is_Married)

"""
Statements & Comments -->

Statements-->
Instructions that Python can execute.

Comments-->
Used to explain the code. They are ignored by the Python interpreter.

Single-line: starts with #

Multi-line: enclosed in ''' or """


# This is a single-line comment

name = "Shalini"  # storing name
print(name)

"""
7. Python Character Set

Character set refers to all the valid characters Python understands, including:

1. Letters – A to Z, a to z
2. Digits – 0 to 9
3. Special Symbols – + - * / = () {} [] etc.
4. Whitespace – space, tab, newline
5. Other Characters – Unicode characters
"""

#  to execute a selected part in python file --> select code --> Shift + Enter

# Using letters, digits, special characters
a = 10        # digit
b = 20
sum = a + b   # using + operator
print("Sum:", sum)

# using whitespace for indentation
if a < b:
    print("a is smaller than b")  # whitespace used before print


# -----------------------------------------------------------------------------------------------------------


#Example 1: Simple Input
name = input("Enter your name: ")
print("Hello,", name)


# Example 2: Input Two Numbers and Add Them
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert to integers
num1 = int(num1)
num2 = int(num2)

print("Sum =", num1 + num2)


#Example 3: Input and Multiply Two Decimal Numbers
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print("Product =", x * y)


#Example 4: Input Age and Print Eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible yet.")


#Example 5: Calculate Area of a Rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of rectangle =", area)








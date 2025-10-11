#------------------------------ Loops Statements -----------------------------------

# Loops are used to execute a block of code repeatedly for a specified number of times.

num1=1
num2=2
num3=3
num4=4
num5=5
# Using for loop to print numbers from 1 to 5
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)

# Using for loop to print numbers from 1 to 5
for i in range(1,6):
    print(i)

""" 
1. while Loop --> The while loop continues executing a block as long as the condition is True.

Syntax :

while condition:
    # block of code

"""

# Examples:

# Example 1: Print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

# Example 2: Print even numbers less than 10
num = 2
while num < 10:
    print(num)
    num += 2

# Example 3: Sum of numbers till 100
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
    print("Total:", total)

# Example 4: Countdown timer
count = 5
while count > 0:
    print(count)
    count -= 1

# Example 5: Validating user input
user_input = ""
while user_input != "yes":
    user_input = input("Type 'yes' to continue: ")


""" 
2. Simulated do-while Loop (Python doesn't have built-in do-while)

A do-while loop executes the block at least once and then checks the condition.
If the condition is False, it stops the loop.

Syntax :  Simulated using while True and break
"""

#Examples:

# Example 1: Print number once, then check
i = 1
while True:
    print(i)
    if i >= 5:
        break
    i += 1

# Example 2: User password input validation
while True:
    password = input("Enter password: ")
    if password == "admin":
        print("Access granted")
        break

# Example 3: Menu simulation
while True:
    print("1. Start\n2. Exit")
    choice = input("Enter choice: ")
    if choice == "2":
        break

# Example 4: Sum input until 0
while True:
    num = int(input("Enter number (0 to stop): "))
    if num == 0:
        break

# Example 5: Print even numbers till 10
i = 0
while True:
    i += 2
    print(i)
    if i >= 10:
        break

"""
3. for Loop --> A for loop is used to iterate over a sequence (like list, tuple, string, range).

Syntax:
for variable in sequence:
    # block
    
"""

#Examples:
# Example 1: Print numbers 1 to 5
for i in range(1, 6):
    print(i)

# Example 2: Print characters in a string
for char in "Python":
    print(char)

# Example 3: Sum of numbers using for loop
total = 0
for i in range(101):
    total += i
    print("Sum:", total)

# Example 4: Print table of 3
for i in range(1, 11):
    print("3 x", i, "=", 3 * i)

# Example 5: Countdown from 5
for i in range(5, 0, -1):
    print(i)


""" 
 4. for Loop when iterating over collections.
"""

# Example 1: List items
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 2: Dictionary keys and values
person = {"name": "John", "age": 25}
for key, value in person.items():
    print(key, ":", value)

# Example 3: Set elements
colors = {"red", "blue", "green"}
for color in colors:
    print(color)

# Example 4: Tuple iteration
nums = (10, 20, 30)
for num in nums:
    print(num)

# Example 5: Iterating over string
for ch in "HELLO":
    print(ch)

""" 
 5. Nested Loops

A loop inside another loop. Useful for grids, patterns, matrices, etc.

"""

# Example 1: Print square pattern
for i in range(3):    #rows
    for j in range(5): #columns
        print("$", end=" ")
    print()  # Empty line for better readability

# Example 2: Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="\t")
    print()

# Example 3: Star pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Example 4: Number grid
for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print()

# Example 5: Nested list processing
matrix = [[1,2], [3,4], [5,6]]
for row in matrix:
    for val in row:
        print(val)

""" 
6. break Statement

break is used to exit the loop prematurely.
"""

# Example 1: Stop loop at 5
for i in range(10):
    if i == 5:
        break
    print(i)

# Example 2: While loop break
i = 1
while True:
    if i > 3:
        break
    print(i)
    i += 1

# Example 3: Loop user input until 'exit'
while True:
    cmd = input("Type 'exit' to stop: ")
    if cmd == "exit":
        break

# Example 4: Stop on negative number
nums = [1, 2, 3, -1, 4]
for n in nums:
    if n < 0:
        break
    print(n)

# Example 5: Break in nested loop
for i in range(3):
    for j in range(3):
        if j == 2:
            break
        print(i, j)

""" 
 7. continue Statement

continue skips the current loop iteration and moves to the next one.
"""

# Example 1: Skip even numbers
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)

# Example 2: Skip specific item
names = ["John", "", "Mike"]
for name in names:
    if name == "":
        continue
    print(name)

# Example 3: Skip on condition
for i in range(1, 6):
    if i == 3:
        continue
    print("Number:", i)

# Example 4: Skip zero division
nums = [1, 0, 2]
for n in nums:
    if n == 0:
        continue
    print(10 / n)

# Example 5: Continue in while loop
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

""" 
8. else with Loops

else in loop runs only if the loop completes normally (no break).
"""

# Example 1: Simple for-else
for i in range(5):
    print(i)
else:
    print("Loop completed")

# Example 2: Break prevents else
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Will not print")

# Example 3: While-else
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("While finished")

# Example 4: Search success check
for item in [1, 2, 3]:
    if item == 4:
        print("Found")
        break
else:
    print("Not Found")

# Example 5: No break, so else runs
for i in [10, 20, 30]:
    print(i)
else:
    print("Loop done")

""" 
 9. Infinite Loop

A loop that never ends unless broken manually.
"""

# Example 1: Basic infinite loop
while True:
    print("Running...")
    break

# Example 2: Menu system
while True:
    print("1. Show\n2. Exit")
    if input("Choice: ") == "2":
        break

# Example 3: Server ping simulation
while True:
    print("Pinging server...")
    break  # Simulate stop

# Example 4: Countdown until stop
while True:
    stop = input("Stop? (yes): ")
    if stop == "yes":
        break

# Example 5: Retry until correct
while True:
    code = input("Enter code: ")
    if code == "1234":
        print("Correct")
        break

""" 
10. List/Dict Comprehensions (Loop Shortcuts)

Comprehensions offer a short syntax for loops inside lists, sets, and dicts.
"""

# Example 1: Squares list
squares = [x**2 for x in range(5)]
print(squares)

# Example 2: Even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Example 3: Dictionary comprehension
sqr_dict = {x: x**2 for x in range(3)}
print(sqr_dict)

# Example 4: String to char list
chars = [ch for ch in "Data"]
print(chars)

# Example 5: Filter names
names = ["Ram", "Raj", "Rani"]
r_names = [name for name in names if name.startswith("R")]
print(r_names)

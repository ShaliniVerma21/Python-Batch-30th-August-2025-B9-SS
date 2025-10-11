#  Using break Statement in Python

# 1. Stop when PIN is correct
for i in range(3):
    pin = input("Enter PIN: ")
    if pin == "1234":
        print("Access granted.")
        break
    else:
        print("Wrong PIN.")

# 2. Find first even number
nums = [1, 3, 5, 8, 9]
for n in nums:
    if n % 2 == 0:
        print("First even:", n)
        break

# 3. Stop countdown when user cancels
for i in range(10, 0, -1):
    cancel = input("Type 'stop' to cancel countdown or press Enter to continue: ")
    if cancel == "stop":
        print("Countdown stopped.")
        break
    print("Time left:", i)

# 4. Break on duplicate name
names = ["Alice", "Bob", "Charlie", "Bob", "Eve"]
seen = set()
for n in names:
    if n in seen:
        print("Duplicate name found:", n)
        break
    seen.add(n)

# 5. ATM pin entry
for _ in range(3):
    pin = input("Enter your PIN: ")
    if pin == "7890":
        print("Transaction allowed.")
        break
    else:
        print("Try again.")

# 6. Stop loop if item is out of stock
items = ["Soap", "Shampoo", "Toothpaste", "OutOfStock", "Lotion"]
for item in items:
    if item == "OutOfStock":
        print("Item out of stock! Stopping...")
        break
    print("Packing:", item)

# 7. Find a student with score above 90
scores = [70, 85, 92, 88]
for s in scores:
    if s > 90:
        print("Topper found:", s)
        break

# 8. Stop searching product after 5 attempts
for i in range(1, 6):
    found = input(f"Search attempt {i}: Did you find the product? (yes/no): ")
    if found.lower() == "yes":
        print("Product found.")
        break

# 9. Exit when first negative value found
nums = [5, 8, 10, -3, 6]
for n in nums:
    if n < 0:
        print("Negative value:", n)
        break

# 10. Stop loop if username already exists
usernames = ["rahul", "kavita", "mahi", "rahul"]
unique = set()
for name in usernames:
    if name in unique:
        print("Username already exists:", name)
        break
    unique.add(name)

# 11. Stop checking files once virus found
files = ["doc1", "doc2", "virus", "doc4"]
for f in files:
    if f == "virus":
        print("Infected file found!")
        break
    print("Safe file:", f)

# 12. Stop login attempts on success
attempts = 0
while attempts < 5:
    user = input("Enter username: ")
    if user == "admin":
        print("Login successful.")
        break
    print("Incorrect username.")
    attempts += 1

# 13. Stop loop on empty string
while True:
    word = input("Enter a word (or press Enter to stop): ")
    if word == "":
        print("Stopped input.")
        break
    print("You entered:", word)

# 14. Stop when battery low
battery_levels = [100, 80, 60, 30, 10, 5]
for level in battery_levels:
    print("Battery:", level, "%")
    if level <= 10:
        print("Battery low! Stopping tasks.")
        break

# 15. Search for a keyword in paragraph
paragraph = ["This is a book.", "This is a pen.", "Keyword found here.", "Another line"]
for line in paragraph:
    if "Keyword" in line:
        print("Found:", line)
        break

# 16. Exit when secret word is guessed
secret = "apple"
while True:
    guess = input("Guess the word: ")
    if guess == secret:
        print("Correct guess!")
        break

# 17. Break on invalid input
inputs = ["10", "25", "abc", "40"]
for i in inputs:
    if not i.isdigit():
        print("Invalid input:", i)
        break
    print("Valid:", i)

# 18. Exit when target reached
targets = [2, 4, 8, 16]
for t in targets:
    print("Checking:", t)
    if t == 8:
        print("Target found!")
        break

# 19. Check if number is prime (use break if divisible)
num = 29
for i in range(2, num):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime")

# 20. Stop processing faulty transaction
transactions = [100, 200, -999, 300]
for t in transactions:
    if t < 0:
        print("Invalid transaction:", t)
        break
    print("Processed:", t)

# 21. End loop if customer cancels
customers = ["Amit", "Neha", "Cancel", "Priya"]
for c in customers:
    if c == "Cancel":
        print("Customer cancelled the order.")
        break
    print("Processing:", c)

# 22. Stop robot if obstacle detected
for step in range(1, 10):
    obstacle = input("Obstacle at step " + str(step) + "? (yes/no): ")
    if obstacle == "yes":
        print("Stopping robot!")
        break

# 23. Stop email sending on error
emails = ["sent", "sent", "error", "sent"]
for status in emails:
    if status == "error":
        print("Email sending failed.")
        break

# 24. Stop OTP verification on success
for _ in range(5):
    otp = input("Enter OTP: ")
    if otp == "123456":
        print("Verified.")
        break
    else:
        print("Incorrect OTP")

# 25. Break on high temperature
temps = [98, 99.5, 101, 97]
for temp in temps:
    if temp > 100:
        print("Fever detected:", temp)
        break

# 26. Break when parking is full
parking = [True, True, False, True]
for slot in parking:
    if not slot:
        print("Parking full.")
        break

# 27. Break when passcode is matched
codes = [4321, 9999, 1234]
for c in codes:
    if c == 1234:
        print("Passcode matched.")
        break

# 28. Stop train simulation on signal
signals = ["green", "green", "red", "green"]
for s in signals:
    print("Signal:", s)
    if s == "red":
        print("Train stopped.")
        break

# 29. Stop machine on critical error
statuses = ["running", "running", "critical", "running"]
for s in statuses:
    if s == "critical":
        print("Error! Stop machine.")
        break

# 30. Stop app install on fail
apps = ["Installed", "Installed", "Failed", "Installed"]
for a in apps:
    if a == "Failed":
        print("Installation failed. Stopping process.")
        break
    print("Installed:", a)


# 7. continue Statement

# 1. Skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"Odd Number: {i}")

# 2. Skip blank names
names = ["John", "", "Alice", " "]
for name in names:
    if name.strip() == "":
        continue
    print(f"Valid Name: {name}")

# 3. Skip out-of-stock items
items = [{"name": "Milk", "stock": 0}, {"name": "Eggs", "stock": 12}]
for item in items:
    if item["stock"] == 0:
        continue
    print(f"{item['name']} is available")

# 4. Skip zero salary employees
salaries = [25000, 0, 40000, 5000]
for salary in salaries:
    if salary == 0:
        continue
    print(f"Salary Processed: ₹{salary}")

# 5. Skip cancelled orders
orders = ["Order1", "Cancelled", "Order2"]
for order in orders:
    if order == "Cancelled":
        continue
    print(f"Processing {order}")

# 6. Skip failed students
marks = {"Ajay": 75, "Sunita": 30, "Ravi": 90}
for name, mark in marks.items():
    if mark < 40:
        continue
    print(f"{name} passed with {mark} marks")

# 7. Skip non-txt files
files = ["report.docx", "summary.txt", "data.csv", "notes.txt"]
for file in files:
    if not file.endswith(".txt"):
        continue
    print(f"Text File: {file}")

# 8. Skip students with 0 assignments
assignments = {"Neha": 3, "Karan": 0, "Isha": 2}
for student, count in assignments.items():
    if count == 0:
        continue
    print(f"{student} submitted {count} assignments")

# 9. Skip negative balances
balances = [1500, -200, 800, -50, 1200]
for balance in balances:
    if balance < 0:
        continue
    print(f"Valid balance: ₹{balance}")

# 10. Skip unverified users
users = [{"name": "Raj", "verified": True}, {"name": "Simran", "verified": False}]
for user in users:
    if not user["verified"]:
        continue
    print(f"Welcome, {user['name']}")

# 11. Skip even-indexed characters
text = "ContinueExample"
for i in range(len(text)):
    if i % 2 == 0:
        continue
    print(text[i], end=" ")

# 12. Skip temperatures below freezing
temps = [25, -3, 14, -10, 30]
for t in temps:
    if t < 0:
        continue
    print(f"Safe Temperature: {t}°C")

# 13. Skip empty lines in a file
lines = ["Data line 1", "", "Data line 2", " "]
for line in lines:
    if line.strip() == "":
        continue
    print(f"Line: {line}")

# 14. Skip weekends
days = ["Mon", "Tue", "Sat", "Sun", "Wed"]
for day in days:
    if day in ["Sat", "Sun"]:
        continue
    print(f"Working day: {day}")

# 15. Skip small expenses
expenses = [1200, 50, 7000, 30, 500]
for amount in expenses:
    if amount < 100:
        continue
    print(f"Recorded expense: ₹{amount}")

# 16. Skip invalid ages
ages = [25, -1, 30, 0, 45]
for age in ages:
    if age <= 0:
        continue
    print(f"Valid Age: {age}")

# 17. Skip duplicate names
names = ["Alice", "Bob", "Alice", "John"]
seen = set()
for name in names:
    if name in seen:
        continue
    seen.add(name)
    print(f"Unique name: {name}")

# 18. Skip uncompleted tasks
tasks = [{"title": "Task1", "done": True}, {"title": "Task2", "done": False}]
for task in tasks:
    if not task["done"]:
        continue
    print(f"Completed: {task['title']}")

# 19. Skip underage voters
ages = [15, 18, 21, 12]
for age in ages:
    if age < 18:
        continue
    print(f"Eligible voter age: {age}")

# 20. Skip invalid email addresses
emails = ["user@example.com", "invalid@", "@domain.com", "valid@mail.com"]
for email in emails:
    if "@" not in email or email.startswith("@"):
        continue
    print(f"Valid email: {email}")

# 21. Skip products with no price
products = [{"name": "Pen", "price": 10}, {"name": "Notebook", "price": 0}]
for p in products:
    if p["price"] <= 0:
        continue
    print(f"Available product: {p['name']}")

# 22. Skip files starting with temp
files = ["temp1.tmp", "main.py", "temp2.log", "script.py"]
for f in files:
    if f.startswith("temp"):
        continue
    print(f"Loaded file: {f}")

# 23. Skip values greater than 100
values = [45, 102, 99, 120]
for v in values:
    if v > 100:
        continue
    print(f"Accepted value: {v}")

# 24. Skip fruits that start with "B"
fruits = ["Apple", "Banana", "Cherry", "Blueberry"]
for fruit in fruits:
    if fruit.startswith("B"):
        continue
    print(f"Eating: {fruit}")

# 25. Skip odd numbers in range
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(f"Even Number: {i}")

# 26. Skip already vaccinated people
people = [{"name": "Kiran", "vaccinated": True}, {"name": "Anu", "vaccinated": False}]
for p in people:
    if p["vaccinated"]:
        continue
    print(f"{p['name']} needs vaccination")

# 27. Skip tasks with no deadline
tasks = [{"name": "Build App", "deadline": None}, {"name": "Deploy App", "deadline": "2025-08-01"}]
for t in tasks:
    if t["deadline"] is None:
        continue
    print(f"Task with deadline: {t['name']}")

# 28. Skip scores below 50
scores = [45, 60, 30, 80]
for score in scores:
    if score < 50:
        continue
    print(f"Passed with score: {score}")

# 29. Skip lower case vowels
word = "DataAnalytics"
for ch in word:
    if ch in "aeiou":
        continue
    print(ch, end=" ")

# 30. Skip sites with no HTTPS
urls = ["http://abc.com", "https://secure.com", "http://xyz.com"]
for url in urls:
    if not url.startswith("https://"):
        continue
    print(f"Secure Site: {url}")


#8. else with Loops

# Example 1: Simple for-else
for i in range(3):
    print("Running loop:", i)
else:
    print("Loop finished successfully\n")

# Example 2: Check if number is prime
num = 7
for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime Number\n")

# Example 3: Search item in list
items = ["pen", "book", "scale"]
for item in items:
    if item == "eraser":
        print("Eraser found")
        break
else:
    print("Eraser not found\n")

# Example 4: While-else loop
i = 0
while i < 3:
    print("i =", i)
    i += 1
else:
    print("While loop completed\n")

# Example 5: Loop with break and else
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed without break\n")

# Example 6: Password attempts
passwords = ["pass1", "pass2", "admin"]
for pwd in passwords:
    if pwd == "admin":
        print("Access Granted")
        break
else:
    print("Access Denied\n")

# Example 7: Check if string has digits
s = "Hello123"
for ch in s:
    if ch.isdigit():
        print("Contains Digit")
        break
else:
    print("No Digits Found\n")

# Example 8: Check if all even
nums = [2, 4, 6, 8]
for n in nums:
    if n % 2 != 0:
        print("Found odd number")
        break
else:
    print("All are even\n")

# Example 9: While-else without break
n = 1
while n <= 3:
    print("Count", n)
    n += 1
else:
    print("No interruption\n")

# Example 10: Check if username is taken
usernames = ["john", "alex", "maya"]
for name in usernames:
    if name == "maya":
        print("Username already taken")
        break
else:
    print("Username available\n")

# Example 11: Find multiple of 5
data = [3, 8, 10, 14]
for val in data:
    if val % 5 == 0:
        print("Found a multiple of 5")
        break
else:
    print("No multiple of 5 found\n")

# Example 12: Empty list check
numbers = []
for n in numbers:
    print(n)
else:
    print("List is empty\n")

# Example 13: All positive check
values = [1, 3, 7]
for v in values:
    if v < 0:
        break
else:
    print("All numbers are positive\n")

# Example 14: For-else with dictionary
info = {"a": 1, "b": 2}
for key in info:
    if key == "c":
        print("Found")
        break
else:
    print("Key not found\n")

# Example 15: Password length check
passwords = ["123", "admin12", "longpass"]
for pwd in passwords:
    if len(pwd) > 6:
        print("Strong password found")
        break
else:
    print("All passwords are weak\n")

# Example 16: While-else with break
x = 1
while x <= 5:
    if x == 3:
        break
    print(x)
    x += 1
else:
    print("Completed\n")

# Example 17: Validate score
scores = [55, 89, 60]
for s in scores:
    if s < 40:
        print("Fail detected")
        break
else:
    print("All passed\n")

# Example 18: Detect vowel in word
word = "sky"
for ch in word:
    if ch in "aeiou":
        print("Vowel found")
        break
else:
    print("No vowels\n")

# Example 19: For-else with input
inputs = ["a", "b", "c"]
for val in inputs:
    if val == "x":
        print("Found x")
        break
else:
    print("x not found\n")

# Example 20: Check for duplicates
ids = [101, 102, 103, 101]
for i in range(len(ids)):
    if ids[i] in ids[i+1:]:
        print("Duplicate found")
        break
else:
    print("No duplicates\n")

# Example 21: Check if student absent
students = ["Ajay", "Neha", "Ravi"]
for s in students:
    if s == "Deepa":
        print("Deepa present")
        break
else:
    print("Deepa absent\n")

# Example 22: Search city in list
cities = ["Delhi", "Mumbai", "Lucknow"]
for c in cities:
    if c == "Pune":
        print("City found")
        break
else:
    print("City not found\n")

# Example 23: All items in stock
inventory = [5, 10, 8, 0]
for item in inventory:
    if item == 0:
        print("Out of stock item found")
        break
else:
    print("All items available\n")

# Example 24: All items below limit
weights = [45, 50, 55]
for w in weights:
    if w > 60:
        print("Overweight item")
        break
else:
    print("All within limit\n")

# Example 25: While-else no break
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Normal exit\n")

# Example 26: All passwords are different
passwords = ["123", "abc", "xyz"]
for p in range(len(passwords)):
    if passwords[p] in passwords[p+1:]:
        print("Duplicate password")
        break
else:
    print("All passwords are unique\n")

# Example 27: Detect uppercase
text = "hello"
for ch in text:
    if ch.isupper():
        print("Uppercase found")
        break
else:
    print("All lowercase\n")

# Example 28: Check if divisible by 7
nums = [5, 14, 21, 10]
for n in nums:
    if n % 7 == 0:
        print("Divisible by 7")
        break
else:
    print("No divisible number\n")

# Example 29: While-else to count down
n = 3
while n > 0:
    print("Counting down:", n)
    n -= 1
else:
    print("Countdown complete\n")

# Example 30: Detect lowercase vowel in sentence
sentence = "WELCOME"
for ch in sentence:
    if ch in "aeiou":
        print("Lowercase vowel found")
        break
else:
    print("No lowercase vowels\n")



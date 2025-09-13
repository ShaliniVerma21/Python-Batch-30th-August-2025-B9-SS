
# 4. Logical Operators (and, or, not)

# 1. Check if person is adult and has voter ID
age = 22
has_voter_id = True
if age >= 18 and has_voter_id:
    print("Eligible to vote")

# 2. Student eligible for scholarship
marks = 85
income = 20000
if marks > 80 and income < 25000:
    print("Scholarship Granted")

# 3. Login check using OR (either email or phone is needed)
has_email = False
has_phone = True
if has_email or has_phone:
    print("Can login")

# 4. Not operator usage
is_logged_in = False
if not is_logged_in:
    print("Please login first")

# 5. Check if it's weekend or holiday
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("Take a rest day!")

# 6. Validate strong password
length = 12
has_special_char = True
if length >= 8 and has_special_char:
    print("Strong Password")

# 7. Check discount eligibility
is_prime = True
cart_value = 1200
if is_prime or cart_value > 1000:
    print("Discount Applied")

# 8. Bank loan eligibility
credit_score = 750
has_collateral = False
if credit_score > 700 and not has_collateral:
    print("Partial Loan Approved")

# 9. Check if mobile is connected
is_wifi = False
is_data = True
if is_wifi or is_data:
    print("Internet available")

# 10. Check exam pass
math = 65
english = 55
if math > 40 and english > 40:
    print("Passed")

# 11. Entry for senior citizen
age = 65
has_pass = False
if age > 60 and (has_pass or age > 70):
    print("Entry granted")

# 12. Check if form is incomplete
has_name = True
has_photo = False
if not has_name or not has_photo:
    print("Form is incomplete")

# 13. Check festival discount
is_festival = True
purchase_amount = 900
if is_festival and purchase_amount > 800:
    print("Festival Discount Applied")

# 14. Multiple login options
login_with_google = False
login_with_facebook = True
if login_with_google or login_with_facebook:
    print("User logged in")

# 15. Health check
is_fever = True
is_cough = False
if is_fever and not is_cough:
    print("Take paracetamol")

# 16. Night driving alert
is_night = True
has_headlights_on = False
if is_night and not has_headlights_on:
    print("Turn on headlights!")

# 17. Shopping site free delivery
total_cart = 1500
is_premium_member = False
if total_cart > 1000 or is_premium_member:
    print("Free delivery available")

# 18. Attendance check
is_present = False
is_on_leave = True
if not is_present and not is_on_leave:
    print("Marked absent")

# 19. Tourist permit
is_indian = True
has_visa = True
if is_indian or has_visa:
    print("Allowed")

# 20. School entry
has_id_card = True
is_in_uniform = False
if has_id_card and is_in_uniform:
    print("Entry allowed")

# 21. Discount offer
has_coupon = False
spent_above_500 = True
if has_coupon or spent_above_500:
    print("Discount available")

# 22. Insurance eligibility
age = 30
is_smoker = False
if age > 25 and not is_smoker:
    print("Eligible for insurance")

# 23. Ride eligibility
is_driver = True
has_license = True
if is_driver and has_license:
    print("Can ride")

# 24. Battery charging check
is_plugged = True
battery_percent = 45
if is_plugged and battery_percent < 100:
    print("Charging...")

# 25. Not operator for validation
logged_in = True
if not logged_in:
    print("Access denied")
else:
    print("Welcome user!")



#  5. Bitwise Operators (&, |, ^, ~, <<, >>)

# 1. Bitwise AND
print(12 & 5)  # 4

# 2. Bitwise OR
print(12 | 5)  # 13

# 3. Bitwise XOR
print(12 ^ 5)  # 9

# 4. Bitwise NOT
print(~5)  # -6

# 5. Left shift
print(5 << 2)  # 20

# 6. Right shift
print(20 >> 2)  # 5

# 7. Check even/odd using AND
num = 7
if num & 1:
    print("Odd")
else:
    print("Even")

# 8. Swap using XOR
a, b = 5, 7
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)

# 9. Set specific bit
n = 4
n = n | (1 << 1)
print(n)

# 10. Clear specific bit
n = 7
n = n & ~(1 << 1)
print(n)

# 11. Toggle specific bit
n = 5
n = n ^ (1 << 1)
print(n)

# 12. Multiply by 2 using <<
print(10 << 1)  # 20

# 13. Divide by 2 using >>
print(10 >> 1)  # 5

# 14. Bit masking
n = 13  # 1101
mask = 1 << 2
if n & mask:
    print("Bit 2 is set")

# 15. Check if power of 2
num = 16
if num & (num - 1) == 0:
    print("Power of 2")

# 16. Convert decimal to binary
print(bin(10))  # 0b1010

# 17. Count number of 1s in binary
print(bin(15).count('1'))  # 4

# 18. Invert all bits
n = 0b1010
print(bin(~n))

# 19. Set all bits to 1 in 8-bit
print(bin((1 << 8) - 1))  # 0b11111111

# 20. Bitwise AND with mask
value = 13
mask = 0b111
print(value & mask)

# 21. Store multiple flags
read = 0b001
write = 0b010
execute = 0b100
perm = read | write
print(perm & execute)  # 0

# 22. Toggle bit in status flag
status = 0b1011
toggle_bit = 0b0100
status = status ^ toggle_bit
print(bin(status))

# 23. Turn off rightmost 1-bit
x = 12
print(x & (x - 1))

# 24. Turn on rightmost 0-bit
x = 10
print(x | (x + 1))

# 25. Get rightmost 1-bit only
x = 10
print(x & -x)



# 6. Membership Operators (in, not in)

# 1. Check if item exists in list
fruits = ['apple', 'banana']
if 'banana' in fruits:
    print("Found banana")

# 2. Check if char in string
word = "Python"
if 'y' in word:
    print("Yes")

# 3. Check if value not in set
roll_numbers = {101, 102, 103}
if 105 not in roll_numbers:
    print("Absent")

# 4. Keyword in sentence
sentence = "Python is awesome"
if "awesome" in sentence:
    print("Compliment found")

# 5. Check file extension
filename = "report.pdf"
if ".pdf" in filename:
    print("PDF File")

# 6. Check domain
email = "user@gmail.com"
if "@gmail.com" in email:
    print("Gmail user")

# 7. Character in password
password = "myp@ss123"
if '@' in password:
    print("Valid special character")

# 8. Membership in dict keys
student = {'name': 'Raj', 'age': 21}
if 'name' in student:
    print("Name exists")

# 9. Membership in values
if 21 in student.values():
    print("Age exists")

# 10. Membership in tuple
colors = ('red', 'green', 'blue')
if 'blue' in colors:
    print("Color matched")

# 11. Check in list of dicts
users = [{'id': 1}, {'id': 2}]
if {'id': 2} in users:
    print("User found")

# 12. Find substring
msg = "Welcome to Python batch"
if "Python" in msg:
    print("Batch verified")

# 13. Word not in paragraph
para = "Learning Python with real examples"
if "Java" not in para:
    print("Java is missing")

# 14. Tag check in HTML
html = "<h1>Hello</h1>"
if "<h1>" in html:
    print("Title tag found")

# 15. Find item in cart
cart = ["pen", "pencil", "eraser"]
if "pencil" in cart:
    print("In cart")

# 16. Role check
roles = ['admin', 'editor']
if 'viewer' not in roles:
    print("Access denied")

# 17. Skill set match
skills = ['Python', 'SQL']
if 'Excel' in skills:
    print("Has Excel skill")
else:
    print("Excel missing")

# 18. Search query in title
title = "Data Science Workshop"
query = "Science"
if query in title:
    print("Match found")

# 19. Ingredient in recipe
ingredients = ["milk", "sugar", "tea"]
if "tea" in ingredients:
    print("Make chai")

# 20. Filter empty strings
words = ["alpha", "", "beta"]
filtered = [w for w in words if w != '']
print(filtered)

# 21. Check file path
path = "C:/Users/Admin/Desktop"
if "Desktop" in path:
    print("Inside desktop")

# 22. URL check
url = "https://youtube.com"
if "youtube" in url:
    print("Video site")

# 23. Membership in range
if 5 in range(1, 10):
    print("Within range")

# 24. Find duplicate
nums = [1, 2, 3, 4, 2]
if nums.count(2) > 1:
    print("Duplicate found")

# 25. Validate token
token = "abc123"
valid_tokens = ['xyz456', 'abc123']
if token in valid_tokens:
    print("Token accepted")



# 7. Identity Operators (is, is not)

# 1. Check same object
x = [1, 2]
y = x
if x is y:
    print("Same object")

# 2. Check different object
a = [3, 4]
b = [3, 4]
if a is not b:
    print("Different object")

# 3. Check None
result = None
if result is None:
    print("Result not available")

# 4. Compare strings
name1 = "Shalini"
name2 = "Shalini"
if name1 is name2:
    print("Same string objects")

# 5. Check boolean identity
status = True
if status is True:
    print("Active")

# 6. Compare memory references
a = 1000
b = 1000
print(a is b)  # False in some cases due to memory

# 7. Tuple identity
t1 = (1, 2)
t2 = (1, 2)
print(t1 is t2)  # True in some versions

# 8. Float identity
f1 = 2.5
f2 = 2.5
print(f1 is f2)

# 9. Integer cache check
x = 10
y = 10
print(x is y)  # True for small integers

# 10. Not identical list
a = [1]
b = [1]
print(a is not b)

# 11. Object None check
obj = None
if obj is None:
    print("Object not created")

# 12. Flag toggle
flag = True
if flag is not False:
    print("Valid flag")

# 13. Check instance id
data = {}
if id(data) is not None:
    print("ID exists")

# 14. Object comparison
class A:
    pass

a = A()
b = A()
print(a is b)  # False

# 15. Check if two sets are same
set1 = {1, 2}
set2 = {1, 2}
print(set1 is set2)

# 16. String intern check
a = "hello"
b = "hello"
print(a is b)  # True due to interning

# 17. Validate None
name = None
if name is None:
    print("No name found")

# 18. Different type object
x = 10
y = '10'
print(x is y)

# 19. Nested object identity
l1 = [1, [2, 3]]
l2 = l1
print(l1[1] is l2[1])  # True

# 20. Check reused variable
x = 100
y = x
print(x is y)

# 21. Dict identity
d1 = {"a": 1}
d2 = d1
print(d1 is d2)

# 22. Temporary object
print([] is [])

# 23. Check is not for deletion
item = None
if item is not None:
    print("Still exists")

# 24. Validate empty string identity
s = ""
if s is not None:
    print("Not null")

# 25. Check same function reference
def fun(): pass
a = fun
print(a is fun)
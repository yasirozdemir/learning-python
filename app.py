age = 21
age = 30  # can reassign
price = age
first_name = "Yasir"
is_online = True
# print(price)

name = input("What is your name? ")
birth_year = input(
    "In what year did you born? "
)  # input function always returns a string -> "2002"

age_from_input = 2023 - int(birth_year)  # 2023 - "2002" won't work because of the types

print(age_from_input)
print(float(age_from_input))

# TYPE CONVERSION
# bool()
# int()
# float()
# str()

# String methods
course = "Python for Beginners"
print(course.capitalize())
print(course.upper())
print(course.lower())

# if exists returns the index number else returns -1
print(course.find("y"))
print(course.find("for"))

# strings are immutable in python
print(course.replace("for", "4"))
print(course)

print("Python" in course)  # if there is "Python" in course it will return true

# division
print(10 / 3)  # answer will be a floating number '3.3333333...'
print(10 // 3)  # answer wil be a whole number '3'

# power operator
print(10 * 3)  # it will multiply '30'
print(10**3)  # it will show the 3rd power of 10 '1000'

# augmented assignment operator
x = 10
x += 3  # 13
x *= 2  # 26
x -= 2  # 24
x /= 6  # 4.0
x **= 4  # 256.0
x %= 3  # 1
x //= 3  # 0
print(x)

# Comparison Operations
x = 3 == 2  # False
x = 3 > 2  # True
x = 3 != 2  # True
# > >= < <= == !=
# Unlike Javascript === does not exist in Python


# Logical expressions
x = 25
print(x > 10 and x < 30)  # True
print(x > 30 or x < 10)  # False
print(not True)  # False

# if statements
temperature = 21
if temperature > 30:
    print("It's a hot day!")
    print("Haha")  # no need to curly braces
elif temperature < 12:
    print("It's cool today!")
else:
    print("Nice!")

weight = input("Weight: ")
unit = input("If it's in Kgs, insert K. If it's in Lbs insert L. ")

if unit.lower() == "k":
    weight_in_lbs = float(weight) / 0.45
    print(
        "Your weight in Lbs: " + str(weight_in_lbs)
    )  # first option to print with concat
elif unit.lower() == "l":
    weight_in_kgs = float(weight) * 0.45
    print("Your weight in Kgs:", weight_in_kgs)  # second option using a comma
else:
    print("Unknown input!")


# while loops
i = 1
# while i <= 1_000:  # 1_000 = 1000 but more readable
#     print(i)
#     i += 1

while i <= 10:
    print(i * "*")
    i += 1


# Lists -> arrays in JS

names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names[-1])  # Mary
print(names[-2])  # Sam
print(names[0])  # John
print(names[2])  # Mosh

names[0] = "John but edited"  # list items are mutable
print(names)

print(
    names[0:3]
)  # returns items of index 0, 1, 2 (NOT INCLUDING 3) -> ['John but edited', 'Bob', 'Mosh']
# it doesn't change the original list

# List Methods

numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # adds 6 at the end -> [1, 2, 3, 4, 5, 6]
numbers.insert(2, 0)  # (index value: int, any) -> [1, 2, 0, 3, 4, 5, 6]
numbers.remove(3)  # removes 3 from the list -> [1, 2, 0, 4, 5, 6]
# numbers.clear()  # empties the list
print(numbers)
print(1 in numbers)  # -> returns a boolean. True if 1 is in the list. True
print(10 in numbers)  # -> False
print(len(numbers))  # returns the number of items in the list -> array.length in JS


# For Loops
print("With for loop:")
for item in numbers:
    print(item)

# For and While
print("With while loop:")
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1


# Range operator
range_of_nums = range(5)
print(
    range_of_nums
)  # range(0, 5) -> generates a sequence of numbers starting from 0 to the given value (not including 5 in this case)

range_of_nums = range(5, 10)  # -> 5, 6, 7, 8, 9

range_of_nums = range(5, 10, 2)  # -> 5, 7, 9 (increases 2 by 2)

range_of_nums = range(5, 10, 3)  # -> 5, 8 (increases 3 by 3)

for number in range_of_nums:
    print(number)

for number in range(
    20, 100, 5
):  # don't need to store the result in a seperate variable using this way
    print(number)


# Tuples -> IMMUTABLE

nums = (1, 2, 3, 3)
# nums[0] = 10  # TypeError: 'tuple' object does not support item assignment
print(
    nums.count(3)
)  # -> 2. returns the number of occurance of the given number in this tuple
# For more look for MAGIC METHODS in PYTHON


# Functions
def calc_sum(a, b):
    return a + b


print(calc_sum(3, 4))

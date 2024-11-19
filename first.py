# Assignment:
# 1. 3 more mathematical functions
# 2. 3 more built-in functions
# 3. function in python to add several numbers
# 4. write the funtions to calculate area of different shapes
# 5. write a function that creates a factorial of a number
# 6. function in python to multiply several numbers
# 7. program to check if a number is in a given range
# 8. program to find the largest among 3 numbers
# 9. simple calc
# 10. given year is a leap year

# 1. 3 more mathematical functions
# first function cbrt = cube root
from math import cbrt

a = 36
cubert_a = cbrt(a)
print(cubert_a)
# second function pi
from math import pi

radius = 12

area = radius * radius * pi
print(area)
# third function fma
from math import fma

x = 23
y = 54
z = 2

equation = fma(x,y,z)
print(equation)

# 2. 3 more built-in functions
# first one split
txt = 'Welcome to the python class'
x = txt.split()

print(x)
# second one tyoe
a = 'string'
print(type(a))
# third one
input_name = input('Enter your name:')
print(input_name)

# 3. function in python to add several numbers
def addNum(x,y,z):
    return x + y + z

print(addNum(32, 44, 72))

# 4. write the funtions to calculate area of different shapes
circle = {
    'radius': 12
}
rectangle = {
    'height': 12,
    'width': 14
}
triangle = {
    'base': 13,
    'height': 10
}

def areacalc(shape):
    if shape is circle:
        return shape['radius'] * shape['radius'] * pi
    elif shape is triangle:
        return shape['base'] * shape['height'] * 0.5
    else:
        return shape['width'] * shape['height']
print(areacalc(circle))

# 5. write a function that creates a factorial of a number
def factorial(n):
    if n == 1 or n == 0:
        return 0
    else:
        result = 1
        for i in range(n, 1, -1):
            result *= i
            return result

# 6. function in python to multiply several numbers
def addNum(x,y,z):
    return x * y * z

print(addNum(32, 44, 72))

# 7. program to check if a number is in a given range
number = int(input('Enter number to check if it is in the range of 50-100: '))
if number >= 50 and number <= 100:
    print('In range')
else:
    print('Not in range')

# 8. program to find the largest among 3 numbers
number1 = int(input('Num 1: '))
number2 = int(input('Num 2: '))
number3 = int(input('Num 3: '))

if number1 > number2 and number1 > number3:
    print('Num 1 is the biggest number')
elif number2 > number1 and number2 > number3:
    print('Num 2 is the biggest number')
elif number1 == number2 == number3:
    print('All are equal')
else:
    print('Num 3 is the biggest number')

# 9. simple calc
param1 = int(input('number 1 to calc: '))
param2 = int(input('number 2 to calc: '))
action = str(input('Enter sign of operation: '))

if action == '*':
    print(param1 * param2)
elif action == '+':
    print(param1 + param2)
elif action == '-':
    print(param1 - param2)
elif action == '/':
    print(param1 / param2)
else:
    print('Not a valid operation')

# 10. given year is a leap year
year = int(input('Enter year to check if it s a leap year: '))

if year%4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print('Leap year')
    else:
        print('Not a leap year')
else:
    print('Not a leap year')


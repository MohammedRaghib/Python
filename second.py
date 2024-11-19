# The mutiplication table of 1 to 10 but both sides of the numbers should be incremented by itself ✔
# using nested loops print a right angle triangle ✔
# Itterates over a list and checks if each number is greater than 3 ✔
# Prints a list in a reversed order using for loop ✔
# Research about break and continue in for loop 📄
# short guessing game program using a while loop, user should be prompted to guess a number between 1 and 100 and the result should tell them if it is too low or too high and it should keep running until the player guesses the number correctly ✔
# write a python program that calculates the sum of numbers from 1 to 500 ✔
# write a python program using while loop that prints a traingle pattern of stars ✔
# Research about break and continue in while loop 📄
# print a pttern where each row has the same number repeated so first row is 1 second is 2 and etc ✔

#  Assigment 1:

print('Assignment 1:')
print('')

for snd in range(1, 11):
    for fst in range(1,11):
        print(f'{fst} x {snd} = {fst * snd}')
print('')

#  Assigment 2:

print('Assignment 2:')
print('')

for star in range(1, 11):
    asterik = '*'
    print(asterik * star)
print('')

#  Assigment 3:

print('Assignment 3:')
print('')

numbers = [3, 45, 6, 78, 77, 56, 1, 2, 0]
for num in numbers:
    if num>3:
        print(num)
print('')

#  Assigment 4:

print('Assignment 4:')
print('')

li_fruits = ['apple', 'banana', 'mango', 'orange']
length = len(li_fruits)

for fruit in li_fruits:
    length = length - 1
    print(li_fruits[length])
print('')

#  Assigment 5 :

print('Assignment 5:')
print('')

def game():
    number_input = int(input('Guess the number, range is from 1-50: '))

    while 22>=number_input>=20 or 26>=number_input>=24:
        print('Very close')
        game()
        break

    while 19>=number_input>=15 or 31>=number_input>=27:
        print('Close')
        game()
        break

    while 14>=number_input>=10 or 46>=number_input>=32:
        print('Not very far off')
        game()
        break        

    while 9>=number_input>=1 or 50>=number_input>=37:
        print('Very far off')
        game()
        break
    while number_input>50:
        print('Not in range')
        game()
        break
    while number_input==23:
        print('Congratulations!! You will now recive a 1000$ dollars')
        break
game()
print('')

#  Assigment 6:

print('Assignment 6:')
print('')

number = 1
result = 0

while number<= 500:
    result += number # result = result + number
    number += 1 # number = number + 1
print(f'The sum of 1 to 500 is: {result}')
print('')

#  Assigment 7:

print('Assignment 7:')
print('')

Rows = 1

while Rows <= 10:
    asterik = '*'
    result = asterik * Rows
    Rows += 1
    print(result)
print('')

#  Assigment 8:

print('Assignment 8:')
print('')

pattern_number = '1'
times = 1
while times <= 5:
    print(pattern_number * times)
    pattern_number = int(pattern_number)
    pattern_number += 1
    pattern_number = str(pattern_number)
    times += 1
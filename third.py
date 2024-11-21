# Examples:

fruits = ['mango', 'pineapple', 'orange', 'apple']
nums = [1, 2, 4,5 ,3904, 5, 3434, 246,4]
nums.sort()
print(nums)
even_nums = [x for x in range(10) if x%2 == 0]
print(even_nums)
fruits1 = ('apple', 'bana', ('protein', 'fructose'))
print(fruits[-1][-1])
tupe1 = list(fruits1)
print(tupe1)

# Write a function to find the largest number in a list. ✔
# Create a list of characters. Write a program to reverse the order of the elements in the list without using built-in functions. Use indexing method. ✔
# Create a list of groceries you need to buy. Add, remove, and modify items as needed. ✔
# Research about Nested Lists and how they are implemented. 📄
# Create a python program to reverse a string. ✔
# Create a python program to check whether a string is palindrome. A word that reads the same both backwards and forward.  Eg. civic, refer, level, madam ✔
# Create a python program to check whether one string is an anagram of the other. Two strings are said to be anagram if we can form one string by arranging the characters of another string ✔
# Research about more files and then try to implement 📄


# Assignment 1:

numbers = [1, 34,3, 423,543,53430,69696969]
largest_num = max(numbers)
print(largest_num)

# Assignment 2:

list_of_char = ['a', 'b', 'c', 'd','e']
reversed = []
length = len(list_of_char) 

for char in list_of_char:
    length -= 1 
    element = list_of_char[length] 
    reversed.append(element)
print(reversed)

# Assignment 3:

groceries = ['Oranges', 'Milk', 'Peanut butter', 'Cabbbages']

groceries.append('Potatoes')

Important = groceries[0:2]

groceries.pop(2)

for item in groceries:
    item.capitalize()

print(f'Groceries needed: {groceries}')
print(f'Dont forget at all costs: {Important}')

# Assignment 4:

string1 = 'hello human being'
word_length = len(string1)
string2 = ''

for letter in string1:
    word_length -= 1
    w_l = string1[word_length]
    string2 = string2 + w_l
print(string2)

# Assignment 5:

word1 = str(input('Enter word to check if it is a palidrome: '))
word_length = len(word1.lower())
backward = ''

for letter in word1:
    word_length -= 1
    w_l = word1[word_length]
    backward = backward + w_l
if backward == word1 and (len(word1) != 1 and len(word1) != 2):
    print("Yay palindrome!")
else:
    print('Ahh man, not a palindrome or word not long enough')

# Assignment 6:

anag1 = str(input('First word: '))
anag2 = str(input('Second word: '))
leng_anag1 = len(anag1)
leng_anag2 = len(anag2)
list_anag1 = [x for x in anag1.lower()]
list_anag2 = [x for x in anag2.lower()]
o_li_anag1 = sorted(list_anag1)
o_li_anag2 = sorted(list_anag2)

if o_li_anag1 is o_li_anag2:
    print('They are anagrams!')
else:
    print('They are not anagrams!')

# Assignment 7:

# pip install OpenPyxsl
# import OpenPyxsl
# from OpenPyxsl import Workbook, load_workbook
# book = load_workbook('file.xlsx')
# (current opening sheet):
# sheet = book.active
# updating:
# sheet['A2'].value = 'Solara'
# saving:
# book.save('file.xlsx')
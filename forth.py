# write program to join dictionary ✔
# RegEx to check for kenyan phone number ✔
# RegEx to extract URLS ✔
# RegEx to extract dates ✔

# Assignment 1

from collections import ChainMap

dict_1 = {
    'name': 'clark',
    'age': 23,
    'gender' : 'male'
}
dict_2 = {
    'name': 'diana',
    'age': 22,
    'gender' : 'female'
}
merged = ChainMap(dict_1, dict_2)
print(merged)

# Assignment 2:

import re

phone_num_val = r'^07\d{8}$|^01\d{8}$|^\+?254[71]\d{8}|^\+?254[- ]?[71]\d{1}[- ]?\d{3}[- ]?\d{3}'

num = str(input('Number: '))

match_num = re.search(phone_num_val, num)

print(bool(match_num))

# Assignment 3:

url_val = r'^(http://|https://|mailto://|ftp://)www\.(.*)\.(com|org)'

link = str(input('Enter to check url: '))

match_url = re.search(url_val, link)

print(bool(match_url))

# Assignment 3:

date_val = r'^(\d{2})[-/]\d{2}[-/]\d{4}$'

date = str(input('Enter date: '))

match_date = re.search(date_val, date)

print(bool(match_date))
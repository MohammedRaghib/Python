# Assignment 1:

info = {
    'draws':200,
    'player1':300,
    'player2':400
}
total = 0
for key in info:
    total = total + info[key]
print(total)

# Assignment 2:

print('Input product details in the order: name, price and quantity. Seperate by space')

item_input = str(input('Input product details: '))

products = item_input.split()

product_dict = {
    'Name': products[0],
    'Price': products[1],
    'Quantity': products[2]
}
print('Do you want to modify? If not enter no, if yes then type in this order: Action, Catergory, Value (modified or to add). Seperate by space')

modify_prompt = str(input('Modify: '))

prompt = modify_prompt.split()

def modify():
    if modify_prompt == 'no':
        print('Product added without modification')
    elif prompt[0] == 'add' or prompt[0] == 'update':
        product_dict[prompt[1]] = prompt[2]
    elif prompt == 'remove':
        pop = product_dict.pop([prompt[1]])
        print(f'Removed: {pop}')
modify()

print(product_dict)

# Assignment 3:

department = {
    'IT': {
        'name': 'Heron',
        'role': 'Technician'
    },
    'MEDICAL': {
        'name': 'Annabeth',
        'role': 'Nurse'
    },
    'HR': {
        'name': 'Reyna',
        'role': 'Therapist'
    },
}

print(department)

# Assignment 4:

set_1 = {1,2,3,4}
set_2 = {4,3,5,6}

ms = set_1 & set_2
print(ms)
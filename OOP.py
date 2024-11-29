# Examples:

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def starteng(self):
        print(self.make, self.model, 'Engine is starting')
    def shiftgear(self):
        print(self.model, 'gear is on parking')
car_1  = Car('Toyota', 'Corolla', 2020)

car_1.starteng()
car_1.shiftgear()

class person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def introduce(self):
        print(f'Hi my name is {self.name}, I live at {self.address}, I am a {self.age}')

person_1 = person('Damon', '100 years old', 'New orleans')

person_1.introduce()

# Trial 1:

class bank_acc:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, depoamt):
        self.balance += depoamt
        print(f'You have deposited KSH {depoamt}, your balance is {self.balance}')

    def withdrawal(self, withamt):
        if self.balance == 0:
            print(f'Insufficeint funds, your balance is {self.balance}')
        elif withamt > self.balance:
            print(f'Insuffecient funds, withdrawal amount is higher than your balance: {self.balance}')
        else:
            self.balance -= withamt
            print(f'You have withdrawn KSH {withamt}, your balance is {self.balance}')
    def checkbal(self):
        print(f'Your balance is KSH {self.balance}')
    

acc_1 = bank_acc('Morpheus', 3000000)

acc_1.checkbal()
acc_1.deposit(3000)
acc_1.withdrawal(2000)

class rectangle:
    def __init__(self, height, width, unit = 'cm'):
        self.height = height
        self.width = width
        self.unit = unit
    def calarea(self):
        area = self.height * self.width
        print(f'The area is {area}{self.unit}²')
    def calcperimeter(self):
        perimeter = (self.height * 2) + (self.width * 2)
        print(f'The area is {perimeter}{self.unit}')

rectangle_1 = rectangle(32, 36, 'cm')
rectangle_1.calcperimeter()
rectangle_1.calarea()
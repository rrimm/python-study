# Object
# 1. adjective = properties
# 2. verbs = methods

# Question 1
class Person:
    pass

p1 = Person()
print(Person)
p1.name = "John"

# Question 2
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def speak(self):
        print(self.name)

p1 = Person("John", "Smith", 18)

print(p1.speak)

# Question 3
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

newRectangle1 = Rectangle(10, 20)
newRectangle2 = Rectangle(20, 35)

print(newRectangle1.perimeter())
print(newRectangle2.perimeter())

# Question 4
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def calculate_average_grade(self):
        return sum(self.grades) / len(self.grades)

new_student = Student('student', [4,3,5,2])
print(new_student.calculate_average_grade())

# Question 5
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

new_bank_account = BankAccount(100)

print(new_bank_account.deposit(10))
print(new_bank_account.withdraw(40))

# Question 6
class Dog:
    created = 0

    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
        Dog.created = Dog.created + 1


dog1 = Dog("Rascal", 2018)
dog2 = Dog("Boi", 2022, "Yip yip yip")
print(f"{Dog.created} dogs have been created so far.")

# Question 7
class Dog:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'hello {self.name}'

d1 = Dog('Julia')
print(d1)

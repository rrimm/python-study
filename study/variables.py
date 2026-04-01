# Variables
import math

# Question 1
var1= "Hi, my name is 'Mirim'"
var2 = '='
var3 = 'I am a student'
print(var1)
print(80*var2)
print(var3)

# Question 2
num1 = 7
print(id(num1))
print(hex(id(num1)))

# Question 3
num = input('number')
print(type(int(2*num)))
name = 'Mirim'
num = math.pi
print(f'Hello, {math.pi:10.2f}')

# Question 4
fahrenheit_str = input('temperature: ')
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit - 32) * 5/9
print(f'celsius: {celsius:.3f}')

# Question 5
print(6 % 3)

# Question 6
radius_str = input('radius: ')
radius = float(radius_str)
area = math.pi * radius * radius

print(f'area: {area:.2f}')

# Question 7
num1 = int(input('first number: '))
num2 = int(input('second number: '))
num3 = int(input('third number: '))

print(f'sum: {num1+num2+num3}')
print(f'product: {num1*num2*num3}')
print(f'average: {(num1+num2+num3)/3:.2f}')

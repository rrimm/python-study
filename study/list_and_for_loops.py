import math

names = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary", "Maru", "Mart"]
print(names[6:4:-1])

numbers = [3, 10, 80, 7, 9, 10, -8, 13]

if 7 in numbers:
    print("7 found")

if 7 not in numbers:
    print("7 not found")

num = 0
arr = []

while num < 3:
    fruit = input("favorite fruit: ")
    arr.append(fruit)
    num += 1

print(arr)

numbers1 = []
for num in range(1,101):
    if num % 2 == 0:
        numbers1.append(num)

print(numbers1)

for num in range(2,100,2):
    print(num)


numbers2 = [3, 9, 20, 11]

arr1 = []

for number in numbers2:
    if type(math.sqrt(number)) == int:
        arr1.append(number)

print(arr1)

arr2 = []
for number in numbers2:
    arr2.append(number ** 2)

print(arr2)
newList = [item**2 for item in numbers2]
print(newList)


numbers4 = [1, 9, 5, 10, 23, 80, -7, 8]
arr3 = []

for number in numbers4:
    if number % 5 == 0:
        arr3.append(number)

newList = [number for number in numbers4 if number % 5 == 0]

print(newList)

numbers5 = [2, 4, 5, 7, 8]
newList = [number**2 for number in numbers5]


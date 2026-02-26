# Conditional structures exercise 3
# Write a program that asks for the biological gender and hemoglobin value (g/l). The program the notifies the user if the hemoglobin value is low, normal or high.
# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.
import sys

male = 'male'
female = 'female'

biologicalGender = input('The biological Gender: ')
if biologicalGender != male and biologicalGender != female:
    print('The biological Gender should be male or female')
    sys.exit()

hemoglobinValue = float(input('The hemoglobin value: '))

if biologicalGender == male:
    if hemoglobinValue < 134:
        print('The hemoglobin is low')
    elif hemoglobinValue > 167:
        print('The hemoglobin is high')
    else:
        print('The hemoglobin is normal')

if biologicalGender == female:
    if hemoglobinValue < 117:
        print('The hemoglobin is low')
    elif hemoglobinValue > 155:
        print('The hemoglobin is high')
    else:
        print('The hemoglobin is normal')


# List structures and iterative loops exercise 1
# Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.
import random

roll = int(input("Enter your roll: "))
numberList = []

for i in range(roll):
    randomNumber = random.randint(1,6)
    numberList.append(randomNumber)

print(f'the sum of the numbers: {sum(numberList)}')

# List structures and iterative loops exercise 2
# Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, the program prints out the five greatest numbers sorted in descending order. Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.

numberList = []
userNumber = input("Enter a number: ")

while True:
    if userNumber == "":
        if len(numberList) < 5:
            print("You must enter at least five numbers")
            break

        numberList.sort(reverse=True)
        print(f"the five greatest numbers: {numberList[:5]}")
        break

    numberList.append(int(userNumber))
    userNumber = input("Enter a number: ")

# List structures and iterative loops exercise 4
# Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names) and stores them into a list structure. Finally, the program prints out the names of the cities one by one, one city per line, in the same order they were read as input. Use a for loop for asking the names and a for/in loop to iterate through the list.
cityList = []

for i in range(5):
    cityName = input("Enter the name of the city: ")
    cityList.append(cityName)

for city in cityList:
    print(city)

# Tuple, set, and dictionary exercise 1
# Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program. We can define each season to last three months, December being the first month of winter.
month = int(input("month: "))
seasons = ("spring", "summer", "autumn", "winter")

index = (month % 12) // 3
print(f"The season is {seasons[index - 1]}.")

# Tuple, set, and dictionary exercise 2
# Write a program that asks the user to enter names until he/she enters an empty string. After each name is read the program either prints out New name or Existing name depending on whether the name was entered for the first time. Finally, the program lists out the input names one by one, one below another in any order. Use the set data structure to store the names.

nameSet = set()
userName = input("Enter a name: ")

while True:
    if userName == "":
        for name in nameSet:
            print(name)
        break

    if userName in nameSet:
        print("Existing name")
    else:
        print("New name")

    nameSet.add(userName)
    userName = input("Enter a name: ")

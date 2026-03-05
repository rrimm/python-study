import math
import random

# 1. Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters. Write a main program that rolls the dice until the result is 6. The main program should print out the result of each roll.
def getRandomDiceRoll():
    while True:
        dice = random.randint(1, 6)
        print(dice)

        if dice == 6:
            break

    return dice

getRandomDiceRoll()

# 2. Modify the function above so that it gets the number of sides on the dice as a parameter. With the modified function you can for example roll a 21-sided role-playing dice. The difference to the last exercise is that the dice rolling in the main program continues until the program gets the maximum number on the dice, which is asked from the user at the beginning.
def getRandomDiceRoll(sideNumber):
    while True:
        dice = random.randint(1, sideNumber)
        print(dice)

        if dice == sideNumber:
            break

    return dice

number = 14
getRandomDiceRoll(number)

# 3. Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres. Write a main program that asks for a volume in gallons from the user and converts the value to liters. The conversion must be done by using the function. Conversions continue until the user inputs a negative value.
def toLiter(volume):
    return int(volume) * 3.785412

while True:
    volume = int(input("Enter volume in gallons: "))
    if volume < 0:
        print("Volume cannot be negative")
        break

    volumeInLiters = toLiter(volume)
    print(f'volume in liters: {volumeInLiters}')

# 4. Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in the list. For testing, write a main program where you create a list, call the function, and print out the value it returned.
def getSum(integerList):
    return sum(integerList)

integerList = [1,3,8,9,14,31,55]
total = getSum(integerList)
print(total)

# 6. Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros. The function calculates and returns the unit price of the pizza per square meter. The main program asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for money (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices.
def calculateUnitPrice(diameterInCentimeters, priceInEuros):
    diameter = diameterInCentimeters / 100
    radius = diameter / 2
    area = math.pi * radius * radius

    return priceInEuros / area

firstPizzaDiameter = float(input("Enter the first pizza diameter in centimeters: "))
firstPizzaPrice = int(input("Enter the first pizza price in euros: "))
secondPizzaDiameter = float(input("Enter the second pizza diameter in centimeters: "))
secondPizzaPrice = int(input("Enter the second pizza price in euros: "))

firstPizzaUnitPrice = calculateUnitPrice(firstPizzaDiameter, firstPizzaPrice)
secondPizzaUnitPrice = calculateUnitPrice(secondPizzaDiameter, secondPizzaPrice)

if firstPizzaUnitPrice < secondPizzaUnitPrice:
    print("The first pizza provides better value for money")
else:
    print("The second pizza provides better value for money")

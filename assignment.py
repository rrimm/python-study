# Assignment 1
# Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
number = 0
arr = []

while number < 1000:
    number += 1
    if number % 3 == 0:
        arr.append(number)

print(arr)

# Assignment 2
# Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
inches = float(input("Enter command: "))
centimeters = inches * 0.393701

while True:
    if inches <= 0:
        print("Inches cannot be a negative value")
        break
    print(f'centimeters: {centimeters}')
    inches = float(input("Enter command: "))

# Assignment 3
# Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.
arr = []
userNumber = input("Enter a number: ")

while True:
    if userNumber == "":
        print(f"max number: {max(arr)}")
        print(f"min number: {min(arr)}")
        break

    arr.append(int(userNumber))
    userNumber = input("Enter a number: ")

# Assignment 4
# Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until they guess the right number. After each guess the program prints out a text: Too high, Too low or Correct. Notice that the computer must not change the number between guesses.
import random
randomNumber = random.randint(1, 10)
userNumber = int(input("Enter command: "))

while True:
    if userNumber == randomNumber:
        print("You are correct!")
        break

    if userNumber > randomNumber:
        print("Your number is too high!")

    if userNumber < randomNumber:
        print("Your number is too low!")

    userNumber = int(input("Enter command: "))

# Assignment 5
# Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the user to enter the username and password again. This continues until the login information is correct or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome. After five failed attempts the program prints out Access denied. The correct username is python and password rules.
username = "rim"
password = "0000"
tryNumber = 0

tryUsername = input("Enter your username: ")
tryPassword = input("Enter your password: ")

while True:
    tryNumber += 1

    if tryNumber > 5:
        print("Access Denied")
        break

    if username == tryUsername and password == tryPassword:
        print("Welcome")
        break

    if username != tryUsername or password != tryPassword:
        print("Wrong Credentials")
        tryUsername = input("Enter your username: ")
        tryPassword = input("Enter your password: ")

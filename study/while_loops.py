import random

number = 1
while number <= 4:
    print(f'Hello for iteration number {number}')
    number = number + 1

print('I am out of the loop!')

number1 = 0

while number1 <= 10:
    number1 = number1 + 1
    print(number1)
    if number1 == 5:
        break


print(random.randint(1,10))
print(random.choice(["a", "b", "c"]))


command = input("Enter command: ")
while True:
    print("Executing command: " + command)
    command = input("Enter command: ")
    if command == "stop":
        break


lucky_number = 17

user_number = int(input("Enter command: "))
while True:
    if user_number == lucky_number:
        print("Congrats!")
        break
    user_number = int(input("Enter command: "))


rolls = 0

while True:
    dice1 = random.randint(1,6)
    rolls += 1
    print(f"the number you got is {dice1}")
    if dice1 == 6:
        print(f"you got a 6 after {rolls} rolls!")
        break


command1 = input("Enter command: ")
while command1!="stop":
    if command1=="MAYDAY":
        break
    print("Executing command: " + command1)
    command1 = input("Enter command: ")
else:
    print("Goodbye.")
print("Execution stopped.")

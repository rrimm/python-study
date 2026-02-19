# Conditional structures

# Question 1
money = int(input("Enter amount of money: "))
print(type(money))

if money >= 5:
    print("You can buy a latte.")

# Question 2
num = 2

print(num == "2")

# Question 3
num = int(input('number: '))

if num > 0:
    print("your number is positive")
else:
    print("your number is not positive")

# Question 4
num = int(input('number: '))

if num % 2 == 0:
    print("your number is even")
else:
    print("your number is odd")

# Question 5
temperature = float(input('temperature: '))

if temperature > 25:
    print('hot')
elif temperature >= 10:
    print('warm')
else:
    print('cold')

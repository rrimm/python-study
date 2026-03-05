# The reason why we use functions
# 1. Modularity
# 2. Repetitive tasks

# Question 1
def f(originalList):
    anotherList = []
    for number in originalList:
        if number % 2 == 0:
            anotherList.append(number)

    return anotherList

originalList = [4,6,7,9,10,99,78]
print(f(originalList))

# Question 2
largestNumber = 0
secondLargestNumber = 1

def f(originalList):
    originalList.sort(reverse=True)

    return {"partA": originalList[largestNumber],
            "partB": originalList[secondLargestNumber],
            }

value = f([3,7,11,14,28])

print(f'partA: {value["partA"]}\npartB: {value["partB"]}')

# Question 3
def change():
    city = "Vantaa"
    print("At the end of the function: " + city)
    return

city = "Helsinki"
print("At the beginning in the main program: " + city)
change()
print("At the end of the main program: " + city)

# Question 4
def f(x):
    return x**2

g = lambda x : x**2
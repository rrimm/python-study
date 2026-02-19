numbers = {"Viivi":"050-12345",
           "Ahmed":"040-11111",
           "Pekka": "010-1112"
           }

name = input("Enter a name: ")
if name in numbers:
    print(f"{name} found!")

for key in numbers:
    print(numbers[key])

names = ['Alice', 'Bob', 'Dave']
nums = [123, 345, 567]

dict = {}

for index in range(len(names)):
    dict[names[index]] = nums[index]

print(dict)

for key in numbers:
    print(f"{key}'s phone number is {numbers[key]}")

for key, value in numbers.items():
    print(f"{key}'s phone number is {value}")

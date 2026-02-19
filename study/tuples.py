days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
day = days_of_the_week[::-1]
print(day)

# Tuple unpacking
# The elements inside a tuple can be unpacked into variables in the following way:
fruits = "Orange", "Banana", "Apple"
(first, second, third) = fruits
print(f"The fruits are: {first}, {second} and {third}.")

orange, banana, apple = fruits
print(type(orange))
print(banana)
print(apple)
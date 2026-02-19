# for loops
# Question 1
for num in range(10, 0, -1):
    print(num)

for num in range(5, 101, 5):
    print(num)

# Question 2
numbers = [2, 4, 5, 7, 8]

newList = [number**2 for number in numbers]
print(newList)


# Tuple
a = (1, 2, 3)
b = (3, 6, 7)
c = []

for num in a:
    c.append(a[num - 1] + b[num - 1])

print(tuple(c))

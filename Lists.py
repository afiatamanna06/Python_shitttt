fruits = ['apple', 'cherry', 'mango']
print(fruits)
print(fruits[1])
print(fruits[-1])
print(fruits[1:])
fruits[0] = 'lemon'
print(fruits)
#exercise
numbers = [1, 5, 2, 9, -1]
bigger = numbers[0]
for items in numbers:
    if items>bigger:
        bigger = items

print(bigger)

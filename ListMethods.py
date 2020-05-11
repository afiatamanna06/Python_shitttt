number = [5, 2, 1, 7, 4, 5]
number.append(13)
print(number)
number.insert(0, 10)
print(number)
number2 = number.copy()
print(number2)
number.remove(13)
print(number)
print(number.index(5))
print(7 in number)
print(number.count(5))
number.sort()
print(number)
number.reverse()
print(number)
number.clear()
print(number)
#exercise
list = [1, 4, 2, 0, -1, 1, 4, 0, 4]
unique = []
for x in list:
    if x not in unique:
        unique.append(x)
print(unique)

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

#exercise
numbers = [5, 2, 5, 2, 2]

for x in numbers:
    for y in range(x):
        print('x', end = '')
    print("")

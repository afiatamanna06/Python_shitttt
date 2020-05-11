for item in 'Python':
    print(item)

for item in ['apple', 'mango', 'cherry', 4]:
    print(item)

for item in range(20):
    print(item)

for item in range(5, 10):
    print(item)

for item in range(5, 10, 3):
    print(item)

#exercise
prices = [10, 20, 30]
sum = 0
for item in prices:
    sum += item
print(f'Total: {sum}')

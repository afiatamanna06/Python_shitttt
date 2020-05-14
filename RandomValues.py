import random

for item in range(10):
    print(random.randint(10, 20))

members = ['Yuki', 'Shigure', 'Ayame', 'Kyo', 'Kagura']
leader = random.choice(members)
print(leader)

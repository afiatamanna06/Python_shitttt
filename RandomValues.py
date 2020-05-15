import random

for item in range(10):
    print(random.randint(10, 20))

members = ['Yuki', 'Shigure', 'Ayame', 'Kyo', 'Kagura']
leader = random.choice(members)
print(leader)
#exercise
class Dice:
    def roll(self):
        thistuple = tuple((random.randint(1,6), random.randint(1,6)))
        return thistuple


dice = Dice()
dice_numbers = dice.roll()
print(dice_numbers)

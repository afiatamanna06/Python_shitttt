import random
number = int(input())
guessed_number = random.randint(1,5)
if number==guessed_number:
    print("won")
else:
    print("lost",guessed_number)
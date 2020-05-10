i = 1
flag = False
while i<=3:
    num = input("Guess: ")
    if int(num) == 9:
        flag = True
        break
    i += 1
if flag == True:
    print("You win!")
else:
    print("Sorry you failed!")

a = 30
if a>20:
    print("Greater than 20")
elif a<20:
    print("Smaller than 20")
else:
    print("Equal to 20")

#exercise

price = 1000000
has_good_credit = True

if has_good_credit:
    payment = price * 0.1
else:
    payment = price * 0.2

print(payment)

try:
    age = int(input("Age: "))
    print(age)
    income = 2000
    risk = income/age
    print(risk)
except ZeroDivisionError:
    print("Age cannot be 0.")
except ValueError:
    print("Invalid Value")

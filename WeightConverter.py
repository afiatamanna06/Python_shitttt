weight = input("Weight: ")
floatweight = float(weight)
option = input("(L)bs or (K)g: ")
if option == 'L' or option == 'l':
    kgweight = floatweight * 0.453592
    print(f'You are {kgweight} kilos')
elif option == 'K' or option == 'k':
    lbsweight = floatweight * 2.20462
    print(f'You are {lbsweight} lbs')

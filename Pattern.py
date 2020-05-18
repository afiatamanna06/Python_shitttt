number = int(input())
print("One pattern:")
for i in range(1, number+1, 1):
    stars = ""
    for j in range(1, i+1, 1):
        stars += '*'
        
    print(stars)
print("Another pattern:")       
for i in range(1, number+1, 1):
    stars = ""
    for j in range(1, i*2, 1):
        stars += '*'
        
    print(stars)
    
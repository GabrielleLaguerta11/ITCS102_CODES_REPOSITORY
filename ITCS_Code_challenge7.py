
size = int(input("Enter size of diamond -->  "))

for x in range(size):
    d = abs(x - size // 2)
    for y in range(size):
        if y >= d and y <= size - 1 - d and (y - d) % 2 == 0:
            print("*", end=" ")
        else: 
            print(" ", end=" ")
    print()            


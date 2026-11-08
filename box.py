r = int(input("Enter row size -->  "))
c = int(input("Enter column size -->  "))

for x in range(r):
    for y in range(c):
        if x == 0 or x == r -1 or y == 0 or y == c - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ") 
    print()           

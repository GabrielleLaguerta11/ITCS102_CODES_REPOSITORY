sum = 0

t = True

while t == True:
    n = int(input("Enter a number -->  "))
    if n == 0:
        print("LOOP TERMINATED.")
        print("The total sum is --> ", sum)
        t == False 
        break

    else:
        print("The current sum is --> ", sum)
        sum += n
        t == True
        continue    
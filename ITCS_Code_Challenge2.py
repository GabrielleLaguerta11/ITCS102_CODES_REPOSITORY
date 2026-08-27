money = 10415

thousand = money//1000
money1 = (money%1000)//500
money2 = (money%500)//200
money3 = (money%200)//100 
money4 = (money%100)//50
money5 = (money%50)//20
money6 = (money%20)//10
money7 = (money%10)//5
money8 = (money%5)//1


print("You have a balance of", money)
print("1000 =", thousand)
print("500 =", money1)
print("200 =", money2)
print("100 =", money3)
print("50 =", money4)
print("20 =", money5)
print("10 =", money6)
print("5 =", money7)
print("1 =", money8)



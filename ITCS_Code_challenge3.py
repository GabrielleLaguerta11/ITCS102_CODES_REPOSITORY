#inputs

name = input("Enter you name: --> ")
item = input("Type of item: --> ")
is_fragile = bool(input("Is the item fragile? (yes/no) --> ") == "yes")
weight = float(input("Weight in kilograms: --> "))
distance = float(input("Distance in kilometers: --> "))
is_express = bool(input("It is rush? (yes/no) --> ") == "yes")
is_international = bool(input("Is it international? (yes/no) --> ") == "yes")

#calculation base cost

base_cost = (weight * 2.50) + (distance * 0.15)

#evaluate pricing tiers

if weight <= 2 and distance <= 100 and not is_express and not is_international:
	total = 0

elif is_express and is_international:
	total = (base_cost * 1.40) + 50

elif weight > 20 and is_express or is_international:
	total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
	total = base_cost + 30

else:
	total = base_cost

shipping_fee = total - base_cost


print("Sender:", name)
print("Item:", item)
print("Fragile:", is_fragile)
print("Weight:", weight)
print("Distance:", distance)
print("Express:", is_express)
print("International:", is_international)
print("Base Cost: PHP", base_cost)
print("Shipping Fee: PHP", shipping_fee)
print("Total/Expected Output: PHP", total)







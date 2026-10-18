import math

driver_name = input("Enter your name -->  ")
license_plate = input("Enter your license plate -->  ")
hours_parked = float(input("How long have you been parked? -->  "))
is_ev = bool(input("Is it electric vehicle? (Press Enter if not) --> "))
is_weekend = bool(input("Is it on a weekend? (Press Enter if not) -->  "))
has_validation = bool(input("Does it have validation? (Press Enter if not) -->  "))
is_member = bool(input("Are you a member? (Press Enter if not) -->  "))

billable_hours = math.ceil(hours_parked)
base_fee = (billable_hours * 5.00) + 5.00

#conditions
if hours_parked <= 5 or has_validation == True and hours_parked <= 2:
    total = 0.00
    print("Free exit. Expected:", total)
elif hours_parked > 12:
        total = 55.0 
        print("Overnight flat rate. Expected:", total)
elif is_member == True and is_weekend:
        total = base_fee * 0.60
        print("Member weekend deal. Expected:", total)
elif is_member == True or is_ev == True:
        total = base_fee * 0.85
        print("Member or EV Discount. Expected:", total)
elif is_weekend: 
        total = base_fee + 8.00
        print("Weekend rate. Expected:", total)
else:
    total = base_fee
    print("Expected:", total)                

print(driver_name, "/", license_plate, "/", total)
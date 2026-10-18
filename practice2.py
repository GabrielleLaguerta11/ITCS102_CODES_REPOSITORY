#inputs 
owner_age = int(input("How old are you? -->  "))
months_revenue = float(input("How much is your monthly revenue? -->  "))
credit_score = int(input("How much is your credit score? -->  "))
years_in_business = float(input("How many years have you been into this business? -->  "))
has_defaults = bool(input("Do you have any defaults? (True/False) -->  "))
collateral_name = input("Name of collateral -->  ")
collateral_value = input("Do you have any collateral? -->  ")

base_rate = 0.00
max_loan = 0.00
monthly_revenue = 0.00


#baseline
if age >= 21:
    if years_in_business >= 2.0:
        if has_defaults == False:
            print("Passed the basseline requirements.")
        else: 
            print("Rejected: high risk application or ineligible owner.")

#tier1
if credit_score >= 720:
    max_loan = 3 * monthly_revenue
    print("Your maximum loan limit is:", max_loan)
    if monthly_revenue >= 5000:
        base_rate = 1.5
    else: 
        base_rate = 2.5  
        print("Your base fee rate is:", base_rate) 

        if collateral_value >= max_loan:
            print("Accepted: Sufficient collateral value for", collateral_name)
        else:
            print("Rejected: Insufficient collateral value for", collateral_name)

            if collateral_value % 5000 != 0:
                base_fee = max_loan * base_rate
                collateral_value = collateral_value + 250.00
                print("Your final processing fee:", collateral_value)
            else:
                collateral_value == collateral_value
                print("Your final processing fee:", collateral_value)    

#tier2
    if credit_score >= 620 and credit_score < 720:
        max_loan = 1.5 * monthly_revenue
        print("Your maximum loan limit is:", max_loan)
        if years_in_business >= 5.0:
            base_rate = 2.0
            print("Your base rate is:", base_rate)
        else:
            base_rate = 3.5
            print("Your base rate is:", base_rate) 

    elif credit_score < 620:
        print("Rejected: Credit score below requirement.")    

else:
    print("Rejected: high risk application or ineligible owner.")


            

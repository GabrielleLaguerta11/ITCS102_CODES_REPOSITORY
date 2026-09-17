age = int(input("Enter you age --> "))
is_employed = bool(input("Are you employed? (True/False) --> "))
credit_score = int(input("What is your current credit score? --> "))
annual_income = float(input("How much is your annual income? --> "))
has_collateral = bool(input("Do you have any collateral? (True/False) --> "))

base_rate = 0.0

if age >= 21 and is_employed ==True:
    print("Application pass baseline requirement.")
    if credit_score >= 750: #tier 1
        base_rate = 5.0
        print("You have a high credit score.")
        if annual_income >= 100000 :
            base_rate = 4.5
            print("Loyalty discount applied. Your final rate is", base_rate)

    elif credit_score >= 600 and credit_score <= 750:
        if has_collateral == True:
            base_rate = 7.0
            print("Your base rate was reduced to", base_rate)

        elif annual_income < 40000:
                base_rate = 9.5 
                print("Your base rate is increased to", base_rate)  

        if credit_score < 600:
            if is_employed == True and has_collateral == True:
                print("Rejected: Credit score too low.")
else:
    print("Rejected: Fails baseline criteria.")     




#input
age = int(input("age -->  "))
rev = float(input("REVENUE -->  "))
cc = int(input("CREDIT SCORE -->  "))
yrs = int(input("YEARS IN BUSINESS -->  "))
has_defaults = bool(input("FILE FOR BANKRUPTCY" -->  ))
collateral = input("COLLATERAL NAME -->  ")
c_value = float(input("COLLATERAL VALUE -->  "))

#baseline
max_loan = 0.00
base_fee = 0.00

if age >= 21 and yrs >= 2.0 and has_defaults == False:
    print("BASELINE PASSED")
    if cc >= 720: #tier1
        max_loan = rev * 3
        print("MAXIMUM LOANABLE AMOUNT IS SET TO", max_loan)
        print("HIGH CREDIT SCORE")
        if rev >= 50000:
            print("REVENUE HIGHER THANK 50K")
            base_fee = max_loan * 0.015
            print("NASE FEE IS SET TO", base_fee)
        else:
            print("REVENUE LOWER THAN 50K")    
            base_fee = max_loan * 0.025
            print("BASEE FEE IS SET TO", base_fee)

        #collateral
        if c_value >= max_loan:
            print("COLLATERAL",collateral, "WITH VALUE OF",c_value, "IS ACCEPTED") 
        else:
            print("REJECTED: INSUFFICIENT COLLATERAL VALUE FOR",collateral)   

        #surcharge
        surcharge_fee = max_loan * base_fee
        print("ADDITIONAL FEE IS ADDED")
        if c_value % 5000 != 0:
            surcharge_fee += 250
            print("SURCHARGE IS SET TO",surcharge_fee)

    elif cc >= 620 and cc <=720: #tier2        
        max_loan = rev * 2
        print("MAXIMUM LOANABLE AMOUNT IS SET TO",max_loan)
        print("MEDIUM CREDIT SCORE")
        if yrs >= 5:
            base_fee = max_loan * 0.02
            print("YEARS IN BUSINESS IS MORE THAN 5 YEARS")
        else:
            base_fee = max_loan * 0.035
            print("BUSINESS IS LESS THEN 5 YEARS")

        #collateral
        if c_value >= max_loan:
            print("COLLATERAL",collateral, "WITH VALUE OF",c_value, "IS ACCEPTED") 
        else:
            print("REJECTED: INSUFFICIENT COLLATERAL VALUE FOR",collateral)   

        #surcharge
        surcharge_fee = max_loan * base_fee
        print("ADDITIONAL FEE IS ADDED")
        if c_value % 5000 != 0:
            surcharge_fee += 250
            print("SURCHARGE IS SET TO",surcharge_fee)

    elif cc < 620: #tier3 
        print("REJECTED: CREDIT SCORE TOO LOW") 

else:
    print("BASELINE NOT PASSED")         





    
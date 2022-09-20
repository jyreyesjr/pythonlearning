#get loan details
money_owed = float(input("How much money do you owe?"))
apr = float(input("What's the APR?"))
payment = float(input("What's your monthly payment?"))
months = int(input("How many months do you want to see the results for?"))

#make it a monthly percentage
monthly_rate = apr/100/12

for i in range(months):
    #add in interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid
    
    if (money_owed - payment < 0):
        print("The last payment is ", money_owed)
        print("You paid off the loan in ", i+1, " months")
        break
    #make a payment
    money_owed = money_owed - payment

    #print results after this month
    print("Paid ", payment, "of which ", interest_paid, "was interest", end=' ')
    print("Now I owe ", money_owed)
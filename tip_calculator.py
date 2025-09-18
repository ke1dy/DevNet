print("\nWelcome to Tip Calculator")

def calculate_tip(bill_amount, tip_percentage):
    tip = bill_amount * tip_percentage
    return tip

def calculate_total(bill_amount, tip):
    total_bill = bill_amount + tip
    return total_bill
    
bill_amount = float(input("Enter yout bill amount: "))
tip_percentage  = float(input("Enter your tip percentage: "))
tip_amount = tip_percentage / 100

tip = calculate_tip(bill_amount, tip_amount)
print("\nYour tip amount is:", tip)
total_bill = calculate_total(bill_amount, tip)
print("Your total bill amount is:", total_bill)

while True:
    total_money = float(input("\nEnter your total money: "))
    if total_money >= total_bill:
        total_money -= total_bill
        print("Your total change is:", total_money)
        break

    else:
        print("You don't have enough money")
        continue
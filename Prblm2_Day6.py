# 2. Function to calculate total expenses
def calculate_expenses(rent, food, electricity, phone, cable_tv):
    return rent + food + electricity + phone + cable_tv

# Function to check savings or borrowing
def check_financial_status(income, expenses):
    remainder = income - expenses
    if remainder > 0:
        print(f"\nYou have savings of Rs.{remainder:.2f} this month.")
    elif remainder < 0:
        print(f"\nYou need to borrow Rs.{-remainder:.2f} this month.")
    else:
        print("\nYour income and expenses are perfectly balanced. No savings or borrowing.")

# User input
income = float(input("Enter your monthly income: "))

print("Enter your monthly expenses:")
rent = float(input("Rent: "))
food = float(input("Food: "))
electricity = float(input("Electricity: "))
phone = float(input("Phone: "))
cable_tv = float(input("Cable TV: "))

# Calculate total expenses and remainder
total_expenses = calculate_expenses(rent, food, electricity, phone, cable_tv)

print(f"\nTotal Monthly Expenses: Rs.{total_expenses:.2f}")
check_financial_status(income, total_expenses)

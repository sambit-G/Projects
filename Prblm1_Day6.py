
##Day 6 Assignment 
# 1. To calculate Gross Pay
def calculate_gross_pay(basic_pay, da_percent, hra_percent):
    da = (da_percent / 100) * basic_pay
    hra = (hra_percent / 100) * basic_pay
    gross_pay = basic_pay + da + hra
    return gross_pay, da, hra

# Input from the user
basic_pay = float(input("Enter Basic Pay: "))
da_percent = float(input("Enter DA percentage: "))
hra_percent = float(input("Enter HRA percentage: "))

# Gross Pay
gross, da, hra = calculate_gross_pay(basic_pay, da_percent, hra_percent)

# Display results
print(f"\nDearness Allowance (DA): {da:.2f}")
print(f"House Rent Allowance (HRA): {hra:.2f}")
print(f"Gross Pay: {gross:.2f}")

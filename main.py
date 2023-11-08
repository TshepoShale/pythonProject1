#math calculation module
import math

welcome_text = """ 
██████╗ ██╗   ██╗ ██████╗     ██████╗  █████╗ ███╗   ██╗██╗  ██╗
██╔══██╗██║   ██║██╔════╝     ██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝
██████╔╝██║   ██║██║  ███╗    ██████╔╝███████║██╔██╗ ██║█████╔╝ 
██╔══██╗██║   ██║██║   ██║    ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗ 
██████╔╝╚██████╔╝╚██████╔╝    ██████╔╝██║  ██║██║ ╚████║██║  ██╗
╚═════╝  ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
"""

def get_float_input(prompt, min_value):
    while True:
        try:
            value = float(input(prompt))
            if value < min_value:
                print(f"Value must be at least {min_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def get_loan_amount(min_amount):
    return get_float_input(f"Enter loan amount in ZAR (minimum {min_amount}): ", min_amount)

def get_loan_duration():
    while True:
        try:
            months = int(input("Enter the number of months for the loan duration (Loan duration must be between 60 and 360 months.): "))
            if 60 <= months <= 360: # time period for loan duration at our bank.
                return months
            else:
                print("Loan duration must be between 60 and 360 months. (5 years until 30 years.)")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_simple_interest(principal, interest_rate, time_period):
    return principal + (principal * (interest_rate / 100) * time_period)

def calculate_compound_interest(principal, interest_rate, time_period):
    amount = principal * (math.pow((1 + interest_rate / 100), time_period))
    return amount
def calculate_simple_interest(principal, annual_interest_rate, loan_duration):
    monthly_interest_rate = annual_interest_rate / (12 * 100)
    total_payments = loan_duration
    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)
    return monthly_payment

while True:
    print(welcome_text)
    print("Options:")
    print("1. Bond Repayment (11.75% interest)")
    print("2. Personal Loan (27.5% interest)")
    print("3. Student Loan (11.75% interest)")
    print("4. Investment Calculator")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        loan_amount = get_loan_amount(500000)
        loan_duration = get_loan_duration()
        monthly_payment = calculate_simple_interest(loan_amount, 11.75, loan_duration)
        print(f"Your monthly payment for the home loan will be: ZAR {monthly_payment:.2f}")
    elif choice == "2":
        loan_amount = get_loan_amount(800000)
        loan_duration = get_loan_duration()
        monthly_payment = calculate_simple_interest(loan_amount, 28.25, loan_duration)
        monthly_payment = calculate_simple_interest(loan_amount, 27.50, loan_duration)
        print(f"Your monthly payment for the personal loan will be: ZAR {monthly_payment:.2f}")
    elif choice == "3":
        loan_amount = get_loan_amount(50000)
        loan_duration = get_loan_duration()
        monthly_payment = calculate_simple_interest(loan_amount, 11.75, loan_duration)
        print(f"Your monthly payment for the student loan will be: ZAR {monthly_payment:.2f}")
    elif choice == "4":
        while True:
            option = input("Which option would you like to choose? 'Simple' or 'Compound': ").lower()
            if option == "simple":
                try:
                    principal = float(input("Enter the principal amount: ZAR "))
                    interest_rate = float(input("Enter the annual interest rate: "))
                    time_period = float(input("Enter the time period (in years): "))
                    simple_interest = calculate_simple_interest(principal, interest_rate, time_period)
                    print(f"The simple interest amount will be: ZAR {simple_interest:.2f}")
                    break
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
            elif option == "compound":
                try:
                    principal = float(input("Enter the principal amount: ZAR "))
                    interest_rate = float(input("Enter the annual interest rate: "))
                    time_period = float(input("Enter the time period (in years): "))
                    total_amount = calculate_compound_interest(principal, interest_rate, time_period)
                    print(f"The total amount after compound interest will be: ZAR {total_amount:.2f}")
                    break
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
            else:
                print("Invalid option. Please choose 'Simple' or 'Compound'.")
        # (Same as before, no changes in this part of the code)
        pass
    elif choice == "5":
        print("Thanks for using BugBank Investment Calculator. Keep well.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

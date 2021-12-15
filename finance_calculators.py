import math

# Print out for user to select options
print("Choose either 'Investment or 'Bond' from the menu below to proceed:")

# Used to give a space break
print()

print("Investment     - to calculate the amount of interest you'll earn on interest")

print("Bond           - to calculate the amount you'll have to pay on a home loan")

# variable created and input requested
user_selection = input("Your option: ")

# variabled casted to be all lower case
user_selection = user_selection.lower()

# list created to have restrictions when user types in options
list = ("investment" , "bond")

# if the option typed in is not in the list; error message appears
# I got this method on google (source: https://stackabuse.com/python-check-if-array-or-list-contains-element-or-value/)
if user_selection.lower() not in list :
    print("Error Message: Please only type in investment or bond")

#if statement used, if investment is typed in the following will be asked to be inputted and cast to float
if user_selection.lower() == "investment" :
    inv_deposit = float(input("Please provide the amount of money you are depositing. "))
    inv_interest_rate = float(input("Please provide the interest rate. "))
    inv_interest_rate = inv_interest_rate / 100
    num_years = float(input("How many years do you plan on investing for? "))
    interest = input("Would you like simple or compound interest? (simple or compound) ")

#if statement used, if previous input is either simple or compund the following formulae are used  
    if interest == "simple" :
        inv_total = inv_deposit * (1 + inv_interest_rate * num_years)
        print(round(inv_total,2))
    elif interest.lower() == "compound" :
        inv_total = inv_deposit * math.pow((1 + inv_interest_rate),num_years)
        print(round(inv_total,2))

# elif statement used, for previous option in 'user_selection', if input is bond the following will be executed
elif user_selection.lower() == "bond" :
    value_house = float(input("What is the present value of the house? "))
    bond_interest_rate = float(input("What is the annual interest rate? "))
    num_months = float(input("What is the number of months you plan to take to repay the bond? "))
    # interest rate is calculated from an annual rate and made into a monthly rate
    bond_interest_rate = ((bond_interest_rate /100)/ 12)
    # formula used to calculate the monthly payment
    # I found this formula on google as the provided formula is not Python equivalent
    # (source: https://www.quora.com/How-do-I-calculate-the-loan-repayment-in-Python)
    bond_total = value_house * (bond_interest_rate *((1 + bond_interest_rate) ** num_months)) / (((1 + bond_interest_rate) ** num_months) -1)
    print(round(bond_total,2))



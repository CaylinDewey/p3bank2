import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('p3bank2')


print("##########################")
print("#                        #")
print("#  WELCOME TO THE BANK   #")
print("#                        #")
print("##########################")



# Prompt user for account name
def account_name_prompt():
    account_name = input ("Welcome, please enter your account name: ")
    return account_name.lower()

# Retrieve old balance from existing file - part I of II
def retrieve_old_balance(account_name):
    try:
        worksheet = SHEET.worksheet(account_name)
        old_balance_amount = calculate_balance(worksheet)# Function below this function
        print(f"The account has been found, the balance is {old_balance_amount:.2f} Euros.")
        transaction_amount_prompt(worksheet, old_balance_amount)
    except gspread.exceptions.WorksheetNotFound:
        create_account_menu(account_name)

# Calculate retrieve old balance from existing file - part II of II
def calculate_balance(worksheet):
    values = worksheet.get_all_values()

    if len(values) <2:
        return 0.00

    deposits = withdrawals = 0

    for row in values[1:]:
        _, transaction_type, amount_str = row
        amount = float(amount_str)
        if transaction_type.lower().strip() == 'deposit':
            deposits += amount
        elif transaction_type.lower().strip() == 'withdrawal':
            withdrawals += amount    
    return deposits - withdrawals

# Create a new account menu
def create_account_menu(account_name=None):
    print("Your account could not be found.\n")
    print("Would you like to: ")
    print("1. Create a new account")
    print("2. Retry")
    print("3. Exit\n")
    choice = input("Enter your choice:  ")
    
    if choice == '1':
        account_name = account_name_prompt()
        create_new_account(account_name)
    elif choice == '2':
        account_name = account_name_prompt()
        retrieve_old_balance(account_name)
    elif choice == '3':
        exit_program_menu()
    else:
        print("Invalid choice. Please enter the numbers 1,2, or 3.")
        create_account_menu()

# Respond to user choice create a new account
def create_new_account(account_name):
    SHEET.add_worksheet(title=account_name, rows="100", cols="3")
    worksheet = SHEET.worksheet(account_name)
    worksheet.append_row(['Date', 'Description', 'Amount',])
    old_balance_amount = 0.00
    print(f"A new account {account_name} has been created. \n")
    transaction_amount_prompt(worksheet, old_balance_amount, account_name)

# Prompt user for transaction type - part II of II - exit option
def exit_program_menu():
    print("Are you sure you want to exit?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice in numbers:  ")

    if choice == '1':
        exit()
    elif choice == '2':
        account_name_prompt()
    else:
        print("Invalid choice. Please enter the numbers 1 or 2.")
        exit_program_menu()

# Prompt user for transaction amount
def transaction_amount_prompt(worksheet, old_balance, account_name):
    try:
        transaction_amount=float(input("Enter the Euro amount with two decimals e.g. 200.00:  "))
        transaction_menu(worksheet, old_balance, transaction_amount, account_name)
    except ValueError:
        print("Invalid input, Please enter a valid number.")
        return transaction_amount_prompt(worksheet, old_balance, account_name)

# Prompt user for transaction type 
def transaction_menu(worksheet, old_balance, transaction_amount, account_name):
    print("What would you like to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Enter your choice with a number (1,2, or 3):   ")

    if choice == '1':
        return deposit_transaction(worksheet, old_balance, transaction_amount)
    elif choice == '2':
        return withdrawal_transaction(worksheet, old_balance, transaction_amount)
    elif choice == '3':
        exit_program_menu()
    else:
        print("Invalid choice. Please enter 1,2, or 3.")
        return transaction_menu(worksheet, old_balance, transaction_amount, account_name)

# Deposit Transaction
def deposit_transaction(worksheet, old_balance, transaction_amount):
    new_balance = old_balance + transaction_amount
    print(f"Your deposit transaction was successful. Your new balance is {new_balance:.2f} Euros. ")
    append_worksheet(worksheet, "Deposit", transaction_amount)
    return new_balance

# Withdrawal Transaction
def withdrawal_transaction(worksheet, old_balance, transaction_amount):
    if transaction_amount > old_balance:
        print(f"Your withdrawal amount exceeds the balance {old_balance:.2f} Euros. Please enter an amount less than your balance.")
        return transaction_amount_prompt(worksheet, old_balance)
    else:
        new_balance = old_balance - transaction_amount
        print(f"Your withdrawal has been successful. Your new balance is {new_balance:.2f} Euros. ")
        append_worksheet(worksheet, "Withdrawal", transaction_amount)
        return new_balance

# Append transactions to worksheet
def append_worksheet(worksheet, transaction_type, transaction_amount):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    worksheet.append_row([date, transaction_type, transaction_amount])



# Call Functions (not nested)
account_name = account_name_prompt()
retrieve_old_balance(account_name)

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
print("#  WELCOME TO QUICK BANK #")
print("#                        #")
print("##########################")

# Prompt user for account name
def account_name_prompt():
    
    while True:
        account_name = input ("Please enter your account name reference (max. 15 characters): \n").lower()
        if account_name and account_name.isalnum() and len(account_name) <=15:
            try:
                worksheet = SHEET.worksheet(account_name)
                retrieve_old_balance(account_name)
                return account_name
            except gspread.exceptions.WorksheetNotFound:
                print(f"The account reference \033[1m{account_name}\033[0m was not found.")
                create_account_menu(account_name)
        else:             
            print("Account name must be alphanumeric, no spaces and a maximum of 15 characters. Please try again.")

# Retrieve old balance from existing file - part I of II
def retrieve_old_balance(account_name):
    
    print(f"Attempting to retrieve balance for account: \033[1m{account_name}\033[0m...🏃‍♀️")
    try:
        worksheet = SHEET.worksheet(account_name)# here it checks if the account_name exists
        old_balance_amount = calculate_balance(worksheet)# Function below this function
        print(f"The account has been found, the balance is {old_balance_amount:,.2f} Euros.\n")
        transaction_amount_prompt(worksheet, old_balance_amount)
    except gspread.exceptions.WorksheetNotFound:
        print(f"The account {account_name} was not found.")
        create_new_account(account_name)
    except Exception as e:
        print(f"An error occurred: {e}")


# Calculate retrieve old balance from existing file - part II of II
def calculate_balance(worksheet):
    
    values = worksheet.get_all_values()

    if len(values) <2:
        return 0.00

    for row in reversed(values[1:]):
        _, _, _, balance_str = row
        balance = float(balance_str.strip().lower())
        return balance
    
    return 0.00
        
# Create a new account menu
def create_account_menu(account_name):

    print("Would you like to: ")
    print("1. Create a new account")
    print("2. Exit\n")
    choice = input("Enter your choice:  ")

    if choice == '1':
            create_new_account(account_name)
    elif choice == '2':
            exit_program_menu()
    else:
        print("Invalid choice. Please enter the numbers 1 or 2.")
        create_account_menu()

# Respond to user choice create a new account
def create_new_account(account_name):

    SHEET.add_worksheet(title=account_name, rows="100", cols="7")
    worksheet = SHEET.worksheet(account_name)
    worksheet.append_row(['Date', 'Description', 'Amount', 'Balance'])
    old_balance_amount = 0.00
    print(f"A new account {account_name} has been created. \n")
    transaction_amount_prompt(worksheet, old_balance_amount)

# Prompt user for transaction type - part II of II - exit option
def exit_program_menu():
    print("Are you sure you want to exit?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice in numbers:  ")

    if choice == '1':
        print("You selected the exit option. Thank you for using Quick Bank. Return soon! 😀\n")
        exit()
    elif choice == '2':
        account_name_prompt()
    else:
        print("Invalid choice. Please enter the numbers 1 or 2.")
    exit_program_menu()

# Prompt user for transaction amount
def transaction_amount_prompt(worksheet, old_balance):

    try:
        transaction_amount = float(input("Enter the Euro amount with two decimals e.g. 200.00:  "))
        transaction_menu(worksheet, old_balance, transaction_amount)
    except ValueError:
        print("Invalid input, please enter a valid number.")
        return transaction_amount_prompt(worksheet, old_balance)

# Prompt user for transaction type 
def transaction_menu(worksheet, old_balance, transaction_amount):

    print("What would you like to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Enter your choice with a number (1, 2, or 3):   \n")

    if choice == '1':
        deposit_transaction(worksheet, old_balance, transaction_amount)
    elif choice == '2':
        withdrawal_transaction(worksheet, old_balance, transaction_amount)
    elif choice == '3':
        exit_program_menu()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        transaction_menu(worksheet, old_balance, transaction_amount)

# Deposit Transaction  depositTransaction
def deposit_transaction(worksheet, old_balance, transaction_amount):
    
    new_balance = old_balance + transaction_amount
    print(f"Your deposit transaction was successful. Your new balance is {new_balance:,.2f} Euros. \n")
    print("Thank you for using Quick Bank. Return soon! 😀\n")
    append_worksheet(worksheet, "Deposit", transaction_amount, new_balance)
    return new_balance

# Withdrawal Transaction
def withdrawal_transaction(worksheet, old_balance, transaction_amount):
    
    if transaction_amount > old_balance:
        print(f"Your withdrawal amount exceeds the balance {old_balance:,.2f} Euros. Please enter an amount less than your balance.")
        return transaction_amount_prompt(worksheet, old_balance)
    else:
        new_balance = old_balance - transaction_amount
        print(f"Your withdrawal has been successful. Your new balance is {new_balance:,.2f} Euros. ")   
        print("Thank you for using Quick Bank. Return soon! 😀\n")
        append_worksheet(worksheet, "Withdrawal", transaction_amount, new_balance)
        return new_balance

# Append transactions to worksheet
def append_worksheet(worksheet, transaction_type, transaction_amount, new_balance):

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    worksheet.append_row([date, transaction_type, transaction_amount, new_balance])
    exit_program_menu()



# Call Functions (not nested)
account_name_prompt()

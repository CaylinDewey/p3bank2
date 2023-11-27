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

print("##################################")
print("#                                #")
print("#     WELCOME TO QUICK BANK      #")
print("#                                #")
print("##################################")


# Prompt user for account name
def accNamePrompt():
    while True:
        accName = input("Please enter your account name: \n").lower()
        if accName and accName.isalnum() and len(accName) <= 15:
            try:
                worksheet = SHEET.worksheet(accName)
                retOldBal(accName)
                return accName
            except gspread.exceptions.WorksheetNotFound:
                print(f"The account {accName} was not found.")
                createAccMenu(accName)
        else:
            print("Try again, only alphanumeric and max. 15 characters.")


# Retrieve old balance from existing file
def retOldBal(accName):

    print(f"Searching account balance: \033[1m{accName}\033[0m...🏃‍♀️")
    try:
        worksheet = SHEET.worksheet(accName)
        oldBalAmt = calcBal(worksheet)
        print(f"The balance is {oldBalAmt:,.2f} Euros.\n")
        tranAmtPrompt(worksheet, oldBalAmt)
    except gspread.exceptions.WorksheetNotFound:
        print(f"The account {accName} was not found.")
        createNewAcc(accName)
    except Exception as e:
        print(f"An error occurred: {e}")


# Calculate retrieve old balance from existing file
def calcBal(worksheet):

    values = worksheet.get_all_values()

    if len(values) < 2:
        return 0.00

    for row in reversed(values[1:]):
        _, _, _, balance_str = row
        balance = float(balance_str.strip().lower())
        return balance

    return 0.00


# Create a new account menu
def createAccMenu(accName):

    print("Would you like to: ")
    print("1. Create a new account")
    print("2. Exit\n")
    choice = input("Enter your choice:  ")

    if choice == '1':
        createNewAcc(accName)
    elif choice == '2':
        exitProgMenu()
    else:
        print("Invalid choice. Please enter the numbers 1 or 2.")
        createAccMenu()


# Respond to user choice create a new account
def createNewAcc(accName):

    SHEET.add_worksheet(title=accName, rows="100", cols="7")
    worksheet = SHEET.worksheet(accName)
    worksheet.append_row(['Date', 'Description', 'Amount', 'Balance'])
    oldBalAmt = 0.00
    print(f"A new account {accName} has been created. \n")
    tranAmtPrompt(worksheet, oldBalAmt)


# Prompt user for transaction type - part II of II - exit option
def exitProgMenu():
    print("Are you sure you want to exit?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice in numbers:  \n")

    if choice == '1':
        print("Thank you for using Quick Bank. Return soon! 😀\n")
        exit()
    elif choice == '2':
        accNamePrompt()
    else:
        print("Invalid choice. Please enter the numbers 1 or 2.")
        exitProgMenu()


# Prompt user for transaction amount
def tranAmtPrompt(worksheet, oldBal):

    try:
        transAmt = float(input("Enter transaction amount e.g. 2,200.00:  "))
        transMenu(worksheet, oldBal, transAmt)
    except ValueError:
        print("Invalid input, please enter a valid number.")
        return tranAmtPrompt(worksheet, oldBal)


# Prompt user for transaction type
def transMenu(worksheet, oldBal, transAmt):

    print("What would you like to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Enter your choice with a number (1, 2, or 3):   \n")

    if choice == '1':
        depTrans(worksheet, oldBal, transAmt)
    elif choice == '2':
        withTrans(worksheet, oldBal, transAmt)
    elif choice == '3':
        exitProgMenu()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        transMenu(worksheet, oldBal, transAmt)


# Deposit Transaction
def depTrans(worksheet, oldBal, transAmt):

    newBal = oldBal + transAmt
    print(f"Success! Your new balance is {newBal:,.2f} Euros. \n")
    print("Thank you for using Quick Bank. Return soon! 😀\n")
    appendWrksh(worksheet, "Deposit", transAmt, newBal)
    return newBal


# Withdrawal Transaction
def withTrans(worksheet, oldBal, transAmt):

    if transAmt > oldBal:
        print(f"Withdrawal exceeds the balance {oldBal:,.2f} Euros.\n")
        print(f"Please enter a smaller transaction amount:   ")
        return tranAmtPrompt(worksheet, oldBal)
    else:
        newBal = oldBal - transAmt
        print(f"Success! Your new balance is {newBal:,.2f} Euros. \n")
        appendWrksh(worksheet, "Withdrawal",
                    transAmt, newBal)
        return newBal


# Append transactions to worksheet
def appendWrksh(worksheet, transType, transAmt, newBal):

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    worksheet.append_row([date, transType, transAmt, newBal])
    exitProgMenu()


# Call Functions (not nested)
accNamePrompt()
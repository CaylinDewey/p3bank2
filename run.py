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

def ask_account_name():
    account_name = input ("Enter your account name: ")
    return account_name.lower()

def check_balance(account_name):
    try:
        worksheet = SHEET.worksheet(account_name)
        old_balance = calculate_balance(worksheet)# Function below this function
        print(f"Your account has been found, the balance is {old_balance:.2f} Euros.")
    except gspread.exceptions.WorksheetNotFound:
        print(f"No account was found for {account_name}. Would you like to create a new account?")

def calculate_balance(worksheet):# function in ask_account_name
    values = worksheet.get_all_values()

    if len(values) <2:
      return 0.0

    deposits = withdrawals = 0

    for row in values[1:]:# [1]: iterates over second row only, now all rows including header
        _, transaction_type, amount_str, _ = row
        amount = float(amount_str)

        if transaction_type.lower().strip() == 'deposit':
            deposits += amount
        elif transaction_type.lower().strip() == 'withdrawal':
            withdrawals += amount
    return deposits - withdrawals


account_name = ask_account_name()
check_balance(account_name)





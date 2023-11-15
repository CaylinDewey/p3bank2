import gspread
from google.oauth2.service_account import Credentials
import math

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('p3bank2')

""""
Get the sheet names ready for use
"""
balSheet = SHEET.worksheet("balance")
depSheet = SHEET.worksheet("deposit")
bankchrSheet = SHEET.worksheet("bankcharge")
intSheet = SHEET.worksheet("interest")

def add_deposit():
    """"
    Provide opportunity for client to deposit and request correct input if validation fails
    """
    while True:
        print("Please enter the amount you want to deposit - with no cents e.g. Euro: 200")
        dep_str = input("Euro:  ")
        
        if validate_deposit(dep_str):
            break

def validate_deposit(values):
    """
    Converts all string values into integers and raises a ValueError if data is not valid.
    """
    try:
        [int(value) for value in values]
        print(f"You are depositing {values} Euro.\n")
         
    except ValueError as e:
        print(f"Invalid amount, please try again.\n")
        return False
    
    return True

def main():
    """
    Run all program functions
    """
    # print(balSheet.get_all_records())
    add_deposit()
print("The Banking App 2\n")
main()
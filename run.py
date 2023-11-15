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

print(balSheet.get_all_records())


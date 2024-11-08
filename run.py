import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open_by_url('https://docs.google.com/spreadsheets/d/11bQcIw_Sovk4kHKVwDFrbk5aW5-_aY4mDRKjKawBfrc/edit?usp=sharing')


sales = SHEET.worksheet('sales')

data = sales.get_all_values()
print(data)


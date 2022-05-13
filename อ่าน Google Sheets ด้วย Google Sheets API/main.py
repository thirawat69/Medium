'''
pip install --upgrade oauth2client PyOpenSSL gspread
'''

# import package and library
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pandas as pd

# modify scope
scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# authenticate and authorize your application with gspread
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials.json', scope)
gc = gspread.authorize(credentials)

# open sheet by link
sheet = gc.open_by_url("<<sheet link>>")

# read sheet first page
worksheet = sheet.get_worksheet(0)
print(worksheet.get_all_values())

# # show records of sheet into dataframe
# dataframe = pd.DataFrame(worksheet.get_all_records())
# dataframe


import streamlit as st
import gspread
from google.auth import default

# Authenticate and connect to Google Sheets
creds, _ = default()
gc = gspread.authorize(creds)

# Load live data from the Google Sheet
sheet_url = 'https://docs.google.com/spreadsheets/d/1o8tI0GCJ0T3wD7WyyNx3PF99hyUUJdEas8RPIUBVl3I/edit?usp=sharing'
spreadsheet = gc.open_by_url(sheet_url)

form_data = spreadsheet.worksheet('Form Responses').get_all_records()
field_map = spreadsheet.worksheet('FieldMap').get_all_records()

# Corrected expected headers to handle duplicate header issue in Weights
weights = spreadsheet.worksheet('Weights').get_all_records(
    expected_headers=['Weight Name', 'Question Id', 'Response Option', 'Weight %']
)

st.title("KMR OEA Dashboard")

# You can expand here with dropdowns, filtering, charts, etc.

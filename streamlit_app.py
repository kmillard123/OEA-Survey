
import streamlit as st
import gspread
from google.oauth2 import service_account

st.title("KMR OEA Dashboard")

# Authenticate
creds = service_account.Credentials.from_service_account_info(st.secrets["gcp"])
gc = gspread.authorize(creds)

# Load from Google Sheet
spreadsheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/1o8tI0GCJ0T3wD7WyyNx3PF99hyUUJdEas8RPIUBVl3I/edit?usp=sharing")
form_data = spreadsheet.worksheet("Form Responses").get_all_records()
field_map = spreadsheet.worksheet("FieldMap").get_all_records()
weights = spreadsheet.worksheet("Weights").get_all_records(
    expected_headers=["Weight Name", "Question Id", "Response Option", "Weight %"]
)

st.success("Sheets loaded successfully!")

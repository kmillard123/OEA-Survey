import streamlit as st
import pandas as pd

st.set_page_config(page_title="OEA Dashboard", layout="wide")
st.title("OEA Survey Dashboard")
st.markdown("This is a working prototype connected to Google Sheets.")

# Placeholder for data loading
@st.cache_data
def load_data():
    sheet_url = st.secrets["google_sheets_url"]
    df = pd.read_csv(sheet_url)
    return df

df = load_data()
st.write("Preview of live data:")
st.dataframe(df)

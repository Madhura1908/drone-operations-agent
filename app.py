import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import os

st.set_page_config(page_title="Drone Agent")
st.title("🚁 Drone Operations Coordinator")

credentials = json.loads(os.environ["GOOGLE_CREDENTIALS"])

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials, scope)
client = gspread.authorize(creds)

pilot_sheet = client.open("PilotRoster").sheet1
drone_sheet = client.open("DroneFleet").sheet1
mission_sheet = client.open("Missions").sheet1

pilots = pd.DataFrame(pilot_sheet.get_all_records())
drones = pd.DataFrame(drone_sheet.get_all_records())
missions = pd.DataFrame(mission_sheet.get_all_records())

st.subheader("Pilots")
st.dataframe(pilots)

st.subheader("Drones")
st.dataframe(drones)

st.subheader("Missions")
st.dataframe(missions)

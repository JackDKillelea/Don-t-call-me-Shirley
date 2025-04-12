import streamlit as st
from helpers.DataHelper import GetData
from Tables import KeystoneTable, WorldRankingsTable, RegionRankingsTable, RealmRankingsTable

players = ["Baldimonk", "Gigdh", "Seutoxze", "WhiteDane", "Winmea", "Ñhs"]
player_data = []

st.set_page_config(layout="wide")

st.title("Don't Call Me Shirley")
st.subheader("Let me know if you want anything adding")

# Fetch data for each player
for player in players:
    data = GetData(player)
    if data:
        player_data.append(data)

KeystoneTable.InitKeystoneTable(player_data)

WorldRankingsTable.InitWorldRankingsTable(player_data)

RegionRankingsTable.InitRegionRankingsTable(player_data)

RealmRankingsTable.InitRealmRankingsTable(player_data)

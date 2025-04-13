import streamlit as st
from helpers.DataHelper import GetData
from Tables import KeystoneTable, WorldRankingsTable, RegionRankingsTable, RealmRankingsTable, PlayerTable

players = {
    "Baldimonk":"Draenor",
    "Gigdh":"Draenor",
    "Seutoxze":"Draenor",
    "WhiteDane":"Draenor",
    "Winmea":"Draenor",
    "Ñhs":"Draenor",
    "Iínk":"Kazzak"
}

player_data = []

st.set_page_config(layout="wide", page_title="Don't call me Shirley")

st.title("Don't Call Me Shirley")
st.subheader("Let me know if you want anything adding")

# Fetch data for each player
for player, realm in players.items():
    data = GetData(player, realm)
    if data:
        player_data.append(data)

PlayerTable.InitPlayerTable(player_data)

KeystoneTable.InitKeystoneTable(player_data)

WorldRankingsTable.InitWorldRankingsTable(player_data)

RegionRankingsTable.InitRegionRankingsTable(player_data)

RealmRankingsTable.InitRealmRankingsTable(player_data)

# TODO: Add Graphs? :o 
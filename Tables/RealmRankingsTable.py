import streamlit as st
from helpers.DataHelper import CreateDF, GetRanks
from helpers.StyleHelper import Highlight_Max_Min_Inverted

def InitRealmRankingsTable(player_data):
    st.header("Rankings Table Realm")
    if player_data:
        player_info_list = []
        
        for data in player_data:
            # Create a dictionary for the player info
            player_info = {
                "Player Name": data['name'],
                "Overall": None,
                "Class": None,
                "Tank": None,
                "Class Tank": None,
                "Healer": None,
                "Class Healer": None,
                "DPS": None,
                "Class DPS": None
            }

            # Extract Realm Ranks
            ranks = data.get('mythic_plus_ranks', {})
            player_info["Overall"] = ranks.get('overall', {}).get('realm', None)
            player_info["Class"] = ranks.get('class', {}).get('realm', None)
            GetRanks(ranks, player_info, "tank", "Tank", "realm")
            GetRanks(ranks, player_info, "class_tank", "Class Tank", "realm")
            GetRanks(ranks, player_info, "healer", "Healer", "realm")
            GetRanks(ranks, player_info, "class_healer", "Class Healer", "realm")
            GetRanks(ranks, player_info, "dps", "DPS", "realm")
            GetRanks(ranks, player_info, "class_dps", "Class DPS", "realm")

            # Append player info to the list
            player_info_list.append(player_info)

        st.dataframe(CreateDF(player_info_list, "Player Name", Highlight_Max_Min_Inverted, "Overall"), use_container_width=True)
    else:
        st.write("No data available.")

import streamlit as st
from helpers.DataHelper import CreateDF, GetRanks
from helpers.MathHelper import Highlight_Max_Min_Inverted

def InitWorldRankingsTable(player_data):
    st.header("Rankings Table World")
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

            # Extract World Ranks
            ranks = data.get('mythic_plus_ranks', {})
            player_info["Overall"] = ranks.get('overall', {}).get('world', None)
            player_info["Class"] = ranks.get('class', {}).get('world', None)
            GetRanks(ranks, player_info, "tank", "Tank", "world")
            GetRanks(ranks, player_info, "class_tank", "Class Tank", "world")
            GetRanks(ranks, player_info, "healer", "Healer", "world")
            GetRanks(ranks, player_info, "class_healer", "Class Healer", "world")
            GetRanks(ranks, player_info, "dps", "DPS", "world")
            GetRanks(ranks, player_info, "class_dps", "Class DPS", "world")

            # Append player info to the list
            player_info_list.append(player_info)

        st.dataframe(CreateDF(player_info_list, "Player Name", Highlight_Max_Min_Inverted, "Overall"), use_container_width=True)
    else:
        st.write("No data available.")

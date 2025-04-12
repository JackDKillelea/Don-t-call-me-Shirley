import streamlit as st
from helpers.DataHelper import CreateKeystoneDF, GetRanks, GetKeystoneLevel
from helpers.MathHelper import Highlight_Max_Min

def InitKeystoneTable(player_data):
    st.header("Keystone Table")
    # Check if player_data is not empty
    if player_data:
        player_info_list = []
        
        for data in player_data:
            # Create a dictionary for the player info
            player_info = {
                "Player Name": data['name'],
                "Score": None,
                "iLevel": None,
                "DFC": None,
                "ROOK": None,
                "ML": None,
                "WORK": None,
                "TOP": None,
                "BREW": None,
                "PSF": None,
                "FLOOD": None,
                "URL": data['profile_url']
            }

            # Extract ilvl
            gear = data.get('gear', {})
            player_info['iLevel'] = gear.get('item_level_equipped', {})

            # Extract mythic plus scores
            for season in data.get('mythic_plus_scores_by_season', []):
                GetRanks(season, player_info, "scores", "Score", "all")

            # Extract best runs for each key
            GetKeystoneLevel(data, player_info)

            # Append player info to the list
            player_info_list.append(player_info)

        st.dataframe(CreateKeystoneDF(player_info_list, "Player Name", Highlight_Max_Min), use_container_width=True)
    else:
        st.write("No data available.")

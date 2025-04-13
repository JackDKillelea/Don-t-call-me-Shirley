import streamlit as st
from helpers.DataHelper import CreateDF, GetRanks
from helpers.StyleHelper import ScoreColours

def InitPlayerTable(player_data):
    st.header("Player Table")
    # Check if player_data is not empty
    if player_data:
        player_info_list = []
        
        for data in player_data:
            # Create a dictionary for the player info
            player_info = {
                "Player Name": data['name'],
                "Score": None,
                "iLevel": None,
                "URL": data['profile_url']
            }

            # Extract ilvl
            gear = data.get('gear', {})
            player_info['iLevel'] = gear.get('item_level_equipped', {})

            # Extract mythic plus scores
            for season in data.get('mythic_plus_scores_by_season', []):
                GetRanks(season, player_info, "scores", "Score", "all")

            # Append player info to the list
            player_info_list.append(player_info)

        st.dataframe(CreateDF(player_info_list, "Player Name", ScoreColours, "Score"), use_container_width=True)
    else:
        st.write("No data available.")

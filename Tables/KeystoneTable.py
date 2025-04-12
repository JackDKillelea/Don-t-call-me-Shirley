import streamlit as st
import pandas as pd
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
                "iLevel": None,
                "DFC": None,
                "ROOK": None,
                "ML": None,
                "WORK": None,
                "TOP": None,
                "BREW": None,
                "PSF": None,
                "FLOOD": None,
                "Score": None,
                "URL": data['profile_url']
            }

            # Extract ilvl
            gear = data.get('gear', {})
            player_info['iLevel'] = gear.get('item_level_equipped', {})

            # Extract mythic plus scores
            for season in data.get('mythic_plus_scores_by_season', []):
                score = season['scores'].get('all', None)
                player_info["Score"] = f"{score:.1f}" if score is not None else None

            # Extract best runs
            for run in data.get('mythic_plus_best_runs', []):
                dungeon = run['short_name']
                if dungeon == "DFC":
                    player_info["DFC"] = run['mythic_level']
                elif dungeon == "ROOK":
                    player_info["ROOK"] = run['mythic_level']
                elif dungeon == "ML":
                    player_info["ML"] = run['mythic_level']
                elif dungeon == "WORK":
                    player_info["WORK"] = run['mythic_level']
                elif dungeon == "TOP":
                    player_info["TOP"] = run['mythic_level']
                elif dungeon == "BREW":
                    player_info["BREW"] = run['mythic_level']
                elif dungeon == "PSF":
                    player_info["PSF"] = run['mythic_level']
                elif dungeon == "FLOOD":
                    player_info["FLOOD"] = run['mythic_level']

            # Append player info to the list
            player_info_list.append(player_info)

        player_info_list.sort(key=lambda x: x["Player Name"])
        # Convert to DataFrame
        df = pd.DataFrame(player_info_list)

        # Convert 0 indexing to 1 indexing
        df.index = range(1, len(df) + 1)

        # Highlight the max and min
        styled_df = df.style.apply(Highlight_Max_Min, subset=['Score', 'iLevel', 'DFC', 'ROOK', 'ML', 'WORK', 'TOP', 'BREW', 'PSF', 'FLOOD'])

        # Display the DataFrame as a table
        st.dataframe(styled_df, use_container_width=True)
    else:
        st.write("No data available.")
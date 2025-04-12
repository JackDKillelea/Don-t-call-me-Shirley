import streamlit as st
import pandas as pd
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

            tank_rank = ranks.get('tank', {}).get('world', None)
            player_info["Tank"] = f"{tank_rank:.0f}" if tank_rank is not None else None

            class_tank_rank = ranks.get('class_tank', {}).get('world', None)
            player_info["Class Tank"] = f"{class_tank_rank:.0f}" if class_tank_rank is not None else None

            healer_rank = ranks.get('healer', {}).get('world', None)
            player_info["Healer"] = f"{healer_rank:.0f}" if healer_rank is not None else None

            class_healer_rank = ranks.get('class_healer', {}).get('world', None)
            player_info["Class Healer"] = f"{class_healer_rank:.0f}" if class_healer_rank is not None else None

            dps_rank = ranks.get('dps', {}).get('world', None)
            player_info["DPS"] = f"{dps_rank:.0f}" if dps_rank is not None else None

            class_dps_rank = ranks.get('class_dps', {}).get('world', None)
            player_info["Class DPS"] = f"{class_dps_rank:.0f}" if class_dps_rank is not None else None

            # Append player info to the list
            player_info_list.append(player_info)

        player_info_list.sort(key=lambda x: x["Player Name"])

        # Convert to DataFrame
        df = pd.DataFrame(player_info_list)  # Pass the list directly
        
        # Convert 0 indexing to 1 indexing
        df.index = range(1, len(df) + 1)

        # Highlight the max and min
        styled_df = df.style.apply(Highlight_Max_Min_Inverted, subset=['Overall'])
        
        # Display the DataFrame as a table
        st.dataframe(styled_df, use_container_width=True)
    else:
        st.write("No data available.")
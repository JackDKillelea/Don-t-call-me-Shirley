import streamlit as st
import requests
import pandas as pd

APIKEY = "RIOA7C3rY8vWSajjvjroDXRka"

players = ["Baldimonk", "Gigdh", "Seutoxze", "WhiteDane", "Winmea", "Ñhs"]
player_data = []

def GetData(charName):
    # Possibly need to add ability to search for characters on different realms as well? 
    url = f"https://raider.io/api/v1/characters/profile?access_key=RIOA7C3rY8vWSajjvjroDXRka&region=eu&realm=Draenor&name={charName}&fields=gear%2Cmythic_plus_scores_by_season%3Acurrent%2Cmythic_plus_ranks%2Cmythic_plus_best_runs%2C"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.write(f'Error: {response.status_code}')
        return None

st.set_page_config(layout="wide")

st.title("Don't Call Me Shirley")
st.subheader("Let me know if you want anything adding")

# Fetch data for each player
for player in players:
    data = GetData(player)
    if data:  # Check if data is not None
        player_data.append(data)

st.header("Keystone Table")
# Check if player_data is not empty
if player_data:
    player_info_list = []
    
    for data in player_data:
        # Create a dictionary for the player info
        player_info = {
            "Player Name": data['name'],
            "Role": data['active_spec_role'],
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

    # Display the DataFrame as a table
    st.dataframe(df, use_container_width=True)
else:
    st.write("No data available.")


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
    
    # Display the DataFrame as a table
    st.dataframe(df, use_container_width=True)
else:
    st.write("No data available.")


st.header("Rankings Table Region")
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

        # Extract Region Ranks
        ranks = data.get('mythic_plus_ranks', {})
        player_info["Overall"] = ranks.get('overall', {}).get('region', None)
        player_info["Class"] = ranks.get('class', {}).get('region', None)

        tank_rank = ranks.get('tank', {}).get('region', None)
        player_info["Tank"] = f"{tank_rank:.0f}" if tank_rank is not None else None

        class_tank_rank = ranks.get('class_tank', {}).get('region', None)
        player_info["Class Tank"] = f"{class_tank_rank:.0f}" if class_tank_rank is not None else None

        healer_rank = ranks.get('healer', {}).get('region', None)
        player_info["Healer"] = f"{healer_rank:.0f}" if healer_rank is not None else None

        class_healer_rank = ranks.get('class_healer', {}).get('region', None)
        player_info["Class Healer"] = f"{class_healer_rank:.0f}" if class_healer_rank is not None else None

        dps_rank = ranks.get('dps', {}).get('region', None)
        player_info["DPS"] = f"{dps_rank:.0f}" if dps_rank is not None else None

        class_dps_rank = ranks.get('class_dps', {}).get('region', None)
        player_info["Class DPS"] = f"{class_dps_rank:.0f}" if class_dps_rank is not None else None


        # Append player info to the list
        player_info_list.append(player_info)

    player_info_list.sort(key=lambda x: x["Player Name"])
    # Convert to DataFrame
    df = pd.DataFrame(player_info_list)  # Pass the list directly

    # Convert 0 indexing to 1 indexing
    df.index = range(1, len(df) + 1)

    # Display the DataFrame as a table
    st.dataframe(df, use_container_width=True)
else:
    st.write("No data available.")


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
        
        tank_rank = ranks.get('tank', {}).get('realm', None)
        player_info["Tank"] = f"{tank_rank:.0f}" if tank_rank is not None else None

        class_tank_rank = ranks.get('class_tank', {}).get('realm', None)
        player_info["Class Tank"] = f"{class_tank_rank:.0f}" if class_tank_rank is not None else None

        healer_rank = ranks.get('healer', {}).get('realm', None)
        player_info["Healer"] = f"{healer_rank:.0f}" if healer_rank is not None else None

        class_healer_rank = ranks.get('class_healer', {}).get('realm', None)
        player_info["Class Healer"] = f"{class_healer_rank:.0f}" if class_healer_rank is not None else None

        dps_rank = ranks.get('dps', {}).get('realm', None)
        player_info["DPS"] = f"{dps_rank:.0f}" if dps_rank is not None else None

        class_dps_rank = ranks.get('class_dps', {}).get('realm', None)
        player_info["Class DPS"] = f"{class_dps_rank:.0f}" if class_dps_rank is not None else None


        # Append player info to the list
        player_info_list.append(player_info)

    player_info_list.sort(key=lambda x: x["Player Name"])
    # Convert to DataFrame
    df = pd.DataFrame(player_info_list)  # Pass the list directly

    # Convert 0 indexing to 1 indexing
    df.index = range(1, len(df) + 1)

    # Display the DataFrame as a table
    st.dataframe(df, use_container_width=True)
else:
    st.write("No data available.")

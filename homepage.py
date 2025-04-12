import streamlit as st
import requests
import pandas as pd

APIKEY = "RIOA7C3rY8vWSajjvjroDXRka"

players = ["Baldimonk", "Gigdh", "Seutoxze", "WhiteDane", "Winmea"]
player_data = []

def GetData(charName):
    url = f"https://raider.io/api/v1/characters/profile?access_key=RIOA7C3rY8vWSajjvjroDXRka&region=eu&realm=Draenor&name={charName}&fields=gear%2Cmythic_plus_scores_by_season%2Cmythic_plus_ranks%2Cmythic_plus_best_runs%2C"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.write(f'Error: {response.status_code}')
        return None

st.set_page_config(layout="wide")

st.title("Don't Call Me Shirley")
st.subheader("Lets see who is the shittest on the team!")
st.write("Please feel free to shit talk the lowest RIO player.")

# Fetch data for each player
for player in players:
    data = GetData(player)
    if data:  # Check if data is not None
        player_data.append(data)

# Check if player_data is not empty
if player_data:
    player_info_list = []
    
    for data in player_data:
        # Create a dictionary for the player info
        player_info = {
            "Player Name": data['name'],
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
    df = pd.DataFrame(player_info_list)  # Pass the list directly

    # Display the DataFrame as a table
    st.table(df)
else:
    st.write("No data available.")

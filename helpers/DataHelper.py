import requests
import pandas as pd
import streamlit as st

APIKEY = "RIOA7C3rY8vWSajjvjroDXRka"

def GetData(player, realm):
    # Possibly need to add ability to search for characters on different realms as well? 
    url = f"https://raider.io/api/v1/characters/profile?access_key=RIOA7C3rY8vWSajjvjroDXRka&region=eu&realm={realm}&name={player}&fields=gear%2Cmythic_plus_scores_by_season%3Acurrent%2Cmythic_plus_ranks%2Cmythic_plus_best_runs%2C"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.write(f'Error: {response.status_code}')
        return None
    
def GetScoreData():
    url = "https://raider.io/api/v1/mythic-plus/score-tiers?access_key=RIOA7C3rY8vWSajjvjroDXRka"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else: 
        st.write(f'Error: {response.status_code}')
        return None
    
def GetRanks(ranks, player_info, search, table_title, competition):
    search_term = ranks.get(search, {}).get(competition, None)
    player_info[table_title] = f"{search_term:.0f}" if search_term is not None else None

def CreateGenericDF(player_info_list, sort_field):
    # Sort by selected field
    player_info_list.sort(key=lambda x: x[sort_field])
    # Convert to DataFrame
    df = pd.DataFrame(player_info_list)
    # Convert 0 indexing to 1 indexing
    df.index = range(1, len(df) + 1)
    return df

def CreateDF(player_info_list, sort_field, highlight_type, subset):
    # Highlight the max and min
    styled_df = CreateGenericDF(player_info_list, sort_field).style.apply(highlight_type, subset=[subset])
    return styled_df

def CreateKeystoneDF(player_info_list, sort_field, highlight_type, keystoneColours):
    # Highlight the max and min
    styled_df = CreateGenericDF(player_info_list, sort_field).style
    
    styled_df.apply(highlight_type, subset=['iLevel', 'DFC', 'ROOK', 'ML', 'WORK', 'TOP', 'BREW', 'PSF', 'FLOOD'])
    styled_df.apply(keystoneColours, subset=['Score'])

    return styled_df

def GetKeystoneLevel(data, player_info):
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
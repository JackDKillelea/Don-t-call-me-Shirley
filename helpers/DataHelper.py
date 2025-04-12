import requests
import streamlit as st

APIKEY = "RIOA7C3rY8vWSajjvjroDXRka"

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
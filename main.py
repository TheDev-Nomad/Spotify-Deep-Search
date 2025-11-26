from dotenv import load_dotenv
from api_functions import get_token, search_for_album
import os
import streamlit as st


load_dotenv()

# Setting secret key variables up
client_id = os.environ.get("CLIENTID")
client_secret = os.environ.get("CLIENTSECRET")
token = get_token()

# Requesting a album
data = search_for_album("The Black Parade", token)

# Displaying the information of the album
for key, value in data['albums']['items'][0].items():
    print(f"{key} has the value of {value}")


from dotenv import load_dotenv
from api_functions import get_token, search_for_album
import streamlit as st
import os

if __name__ == "__main__":

    load_dotenv()

    # Setting secret key variables up
    client_id = os.environ.get("CLIENTID")
    client_secret = os.environ.get("CLIENTSECRET")
    token = get_token(client_id=client_id, client_secret=client_secret)



    st.title("Spotify API Testing Playground 👋")
    query = st.text_input("Enter an album to search for:")
    data = search_for_album(query, token)
    url = data['albums']['items'][0]['images'][1]['url']
    print(url)

    st.write("Album cover")
    st.image(url, width=300)

    # Displaying the information of the album
    # for key, value in data['albums']['items'][0].items():
    #     # print(f"{key} has the value of {value}")
    #     print(data['albums']['items'][0]['images'][1]['url'])

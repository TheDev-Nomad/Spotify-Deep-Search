from dotenv import load_dotenv
from api_functions import get_token, search_for_album, get_album_details, ms_to_min_sec
import streamlit as st
import pandas as pd
import os
import json

if __name__ == "__main__":

    load_dotenv()

    # Setting secret key variables up
    client_id = os.environ.get("CLIENTID")
    client_secret = os.environ.get("CLIENTSECRET")
    token = get_token(client_id=client_id, client_secret=client_secret)

    st.title("Spotify Deep Search")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        album = st.text_input("Enter an album to search for:")
    
    with col2:
        artist = st.text_input("Artist name")

    if st.button("Search"):

        try:
            # Fetching data from the entered album and artist
            data = search_for_album(album, token, artist)['albums']['items'][0]
            
            Artist_Name = data['artists'][0]['name']
            url = data['images'][1]['url']
            Album_link = data['external_urls']['spotify']
            Album_id = data['id']
            Album_name = data["name"]

            data = get_album_details(album_id=Album_id, token=token)
            tracks = data['tracks']['items']

            df = pd.DataFrame({
                "Name": [t["name"] for t in tracks],
                "Duration (ms)": [ms_to_min_sec(t['duration_ms']) for t in tracks]
            })

        except Exception as e:
            st.warning(e)
            
        with col3:
            st.header(Artist_Name)
            st.subheader(Album_name)
            st.image(url, width=300)
            st.markdown(f"[View the album]({Album_link})")

        with col4:
            st.dataframe(df)

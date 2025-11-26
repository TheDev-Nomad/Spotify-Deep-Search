import requests
import base64

# Fetches the token based off of client_id and client_secret
def get_token(client_id, client_secret):

    # Encode client_id:client_secret in Base64
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers=headers,
        data=data
    )

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print("Error:", response.status_code, response.text)

# Searches for a specified album
def search_for_album(query, token):
    
    url = "https://api.spotify.com/v1/search"

    headers = {"Authorization": f"Bearer {token}"}

    params = {
        "q": query,
        "type": "album",
        "limit": 1
    }
    
    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status()

    return r.json()
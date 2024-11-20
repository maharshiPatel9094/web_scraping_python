import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint  # For better visualization of results

# Load environment variables
load_dotenv()  # This will load CLIENT_ID and CLIENT_SECRET from your .env file
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Prompt the user for a year
date = input("What year would you like to travel to? Write the date in this format (YYYY-MM-DD): ")

# Prepare the URL and headers for scraping Billboard's Hot 100 chart
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = f"https://www.billboard.com/charts/hot-100/{date}"

# Send the GET request to fetch the webpage
response = requests.get(url=url, headers=header)
website_html = response.text  # Convert to HTML

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(website_html, "html.parser")

# Extract song names from the HTML structure
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# Set up the Spotipy client with OAuth
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private user-library-read",
        redirect_uri="http://example.com",  # Use a proper redirect URI
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username = "maharshi patel"# Optionally store the token to avoid reauthentication
    )
)

# Get the user's Spotify ID
user_id = sp.current_user()["id"]

# Initialize the list to store song URIs
song_uris = []

# Extract the year from the input date
year = date.split("-")[0]

# Iterate through the song names and search for them on Spotify
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    pprint(result)  # Print the result to help with debugging if needed

    try:
        # Extract the URI of the first track found (if any)
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        # Handle the case where no matching track was found
        print(f"'{song}' doesn't exist in Spotify. Skipped.")

# Display the song URIs found
print(f"\nFound {len(song_uris)} songs on Spotify for the year {year}:")
for uri in song_uris:
    print(uri)

from dotenv import load_dotenv
load_dotenv()

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

df = pd.read_csv('resources/bubbleflexe-rv.csv', usecols=[1, 2], names=['bsides', 'tt'])

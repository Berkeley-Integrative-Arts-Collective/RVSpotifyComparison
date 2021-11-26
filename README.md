# RVSpotifyComparison
This is a network analysis of songs made by [Red Velvet](https://en.wikipedia.org/wiki/Red_Velvet_(group)) using a user survey (N=5,702) that describes a listener's favorite B-sides and Title Tracks out of Red Velvet's music. This is contrasted against Spotify's audio features, recommendations, and song popularity. A summary of findings will be completed soon.

## Developers
Create a Python 3.9+ virtual environment with all dependencies outlined in `py-requirements.txt`. Create a `.env` file at the root and populate as follows:
```py
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
```
Most of the code is contained within `py/explore.ipynb`.

## Data
The raw data (available at `resources/bubbleflexe-rv.csv`) was collected from January 17th, 2021 to February 1st, 2021. Respondents were found via YouTube community posts, Twitter posts, YouTube comments, and other social media methods. Demographics of respondents were not collected, but it can be reasonably assumed that most respondents are casual-significant consumers of Red Velvet content.

Thank you to [bubbleflexe](https://www.youtube.com/channel/UCZYfSS5j4nnUrWQQPuKLVnA) for collecting and providing this data.

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='997344d05ad141a6aa856a94a51edf6f',
                                               client_secret='4090920671a24d01be0215d538fb1018',
                                               redirect_uri='http://localhost:8888/callback',
                                               scope='user-modify-playback-state user-read-playback-state'))

# Get a list of available devices
devices = sp.devices()

# Select a device (for example, the first device in the list)
device_id = devices['devices'][0]['id']

# Start playback on the selected device
sp.start_playback(device_id=device_id, context_uri='spotify:playlist:7hgfPxcMNli5SGFEvMYvxw')

print(f"Playing on device: {device_id}")

import serial
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='997344d05ad141a6aa856a94a51edf6f',
                                               client_secret='4090920671a24d01be0215d538fb1018',
                                               redirect_uri='http://localhost:8888/callback',
                                               scope='user-modify-playback-state'))

devices = sp.devices()
device_id = devices['devices'][0]['id']

# Set up serial communication with Arduino
arduino = serial.Serial('COM5', 9600)
time.sleep(2)  # Wait for the connection to establish

# Playlist URIs mapped to temperature ranges
playlist_map = {
    'cold': ('spotify:playlist:2tORvrsO040BhX78MpOoU4', 'Cold Songs'),
    'warm': ('spotify:playlist:2LvqTvgzJSdepDoMe1AYV2', 'Warm Songs'),
    'hot': ('spotify:playlist:7hgfPxcMNli5SGFEvMYvxw', 'Hot Songs')
}

def get_playlist(temp_value):
    if temp_value < 25:
        return 'cold'
    elif 25 <= temp_value < 30:
        return 'warm'
    else:
        return 'hot'

def play_playlist(playlist_key, device_id):
    uri, _ = playlist_map[playlist_key]
    sp.start_playback(device_id=device_id, context_uri=uri)

print("Reading temperature data from Arduino...")
playing = "nothing here"

try:
    while True:
        if arduino.in_waiting > 0:  # Check if there is incoming data
            temperature = arduino.readline().decode('utf-8').strip()
            print(f"Temperature: {temperature}°C")  # Display the temperature
            
            temp_value = float(temperature)
            playlist_key = get_playlist(temp_value)
            
            if playing != playlist_map[playlist_key][0]:
                play_playlist(playlist_key, device_id)
                playing = playlist_map[playlist_key][0]
                print(f"Playing {playlist_map[playlist_key][1]} on device: {device_id}")

except KeyboardInterrupt:
    print("Program interrupted.")
finally:
    arduino.close()
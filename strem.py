
import streamlit as st
import serial
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='YOUR_CLIENT_ID',
                                               client_secret='YOUR_CLIENT_SECRET',
                                               redirect_uri='http://localhost:8888/callback',
                                               scope='user-modify-playback-state'))

# Function to initialize serial connection
def init_serial_connection(port='COM5', baudrate=9600):
    try:
        arduino = serial.Serial(port, baudrate)
        time.sleep(2)  # Wait for the connection to establish
        return arduino
    except Exception as e:
        st.error(f"Error opening serial port: {e}")
        return None

# Function to play a playlist on Spotify
def play_playlist(playlist_uri, device_id):
    sp.start_playback(context_uri=playlist_uri, device_id=device_id)

# Main Streamlit app
st.title("Temperature-Based Spotify Controller")

# Initialize serial connection
arduino = init_serial_connection()

# Get available devices and select the first one
devices = sp.devices()
if devices['devices']:
    device_id = devices['devices'][0]['id']  # Get the first available device ID
else:
    st.error("No active devices found.")
    st.stop()  # Stop execution if no devices are available

# State variable to track currently playing playlist
if 'playing' not in st.session_state:
    st.session_state.playing = "nothing here"

# Button to start reading temperature data
if st.button("Start Reading Temperature"):
    if arduino is not None:
        while True:
            if arduino.in_waiting > 0:  # Check if there is incoming data
                # Read and decode the line from Arduino
                temperature = arduino.readline().decode('utf-8').strip()
                st.write(f"Temperature: {temperature}°C")  # Display the temperature
                
                # Convert to float for comparison
                temp_value = float(temperature)

                # Determine which playlist to play based on temperature
                if temp_value < 25:
                    current_playlist = 'spotify:playlist:2tORvrsO040BhX78MpOoU4'  # Cold songs playlist
                elif 25 <= temp_value < 26:
                    current_playlist = 'spotify:playlist:2LvqTvgzJSdepDoMe1AYV2'
                elif 26 <= temp_value < 30:
                    current_playlist = 'spotify:playlist:7ItUriE20ViFx6SGfOk6ws'
                elif 30 <= temp_value < 35:
                    current_playlist = 'spotify:playlist:7hgfPxcMNli5SGFEvMYvxw'
                elif 35 <= temp_value < 36:
                    current_playlist = 'spotify:playlist:3FWufqDOdUJ0HpyBb3ftuc'
                else:
                    current_playlist = 'spotify:playlist:3isO1HYQnMyceoe7OLeqaY'

                # Play the playlist only if it has changed
                if current_playlist != st.session_state.playing:
                    st.write(f"Playing on device: {device_id}")
                    play_playlist(current_playlist, device_id)
                    st.session_state.playing = current_playlist  # Update last played playlist

            time.sleep(1)  # Add a small delay to prevent overwhelming the Arduino

# Close the Arduino connection when the app stops running
if arduino is not None:
    arduino.close()
import serial
import time
import spotipy
import pyttsx3
from spotipy.oauth2 import SpotifyOAuth

engine = pyttsx3.init()
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='997344d05ad141a6aa856a94a51edf6f',
                                               client_secret='4090920671a24d01be0215d538fb1018',
                                               redirect_uri='http://localhost:8888/callback',
                                               scope='user-modify-playback-state'))

devices= sp.devices()
device_id=devices['devices'][0]['id']

arduino = serial.Serial('COM5', 9600)  
time.sleep(2)  

def play_text(text):
    engine.say(text)
    engine.runAndWait()
def play_playlist(playlist_uri, device_id=None):
    sp.start_playback(context_uri=playlist_uri, device_id=device_id)

print("Reading temperature data from Arduino...")
playing="nothing here"
try:
    while True:
        if arduino.in_waiting > 0:  
            temperature = arduino.readline().decode('utf-8').strip()
            print(f"Temperature: {temperature}°C")  
    
            temp_value = float(temperature)
            # Determine if hot or cold and play appropriate playlist
            if temp_value < 25:
                if playing!='spotify:playlist:2tORvrsO040BhX78MpOoU4':
                    print("Playing very cold songs...")
                    play_text("Too cold , here comes cold music")
                    sp.start_playback(device_id=device_id, context_uri='spotify:playlist:2tORvrsO040BhX78MpOoU4')
                    playing = 'spotify:playlist:2tORvrsO040BhX78MpOoU4'
            elif 25<=temp_value < 26:
                if playing!='spotify:playlist:2LvqTvgzJSdepDoMe1AYV2':
                    print("Playing cold songs...")
                    play_text("surprise ,enjoy the easter egg")
                    sp.start_playback(device_id=device_id, context_uri='spotify:playlist:2LvqTvgzJSdepDoMe1AYV2')
                    playing = 'spotify:playlist:2LvqTvgzJSdepDoMe1AYV2'
            elif 26<= temp_value < 30:
                if playing!='spotify:playlist:7ItUriE20ViFx6SGfOk6ws':
                    print("Playing solace cold songs...")
                    play_text("sleep time")
                    sp.start_playback(device_id=device_id, context_uri='spotify:playlist:7ItUriE20ViFx6SGfOk6ws')
                    playing = 'spotify:playlist:7ItUriE20ViFx6SGfOk6ws'
            elif 30<= temp_value < 35:
                if playing!='spotify:playlist:7hgfPxcMNli5SGFEvMYvxw':
                    print("Playing hot songs...")
                    play_text("feeling warm , lets here something hot")
                    sp.start_playback(device_id=device_id, context_uri='spotify:playlist:7hgfPxcMNli5SGFEvMYvxw')
                    playing = 'spotify:playlist:7hgfPxcMNli5SGFEvMYvxw'
            elif 35<= temp_value < 36:
                if playing!='spotify:playlist:3FWufqDOdUJ0HpyBb3ftuc':
                    print("Playing edge hot songs...")
                    play_text("hot surprise")
                    sp.start_playback(device_id=device_id, context_uri='spotify:playlist:3FWufqDOdUJ0HpyBb3ftuc')
                    playing = 'spotify:playlist:3FWufqDOdUJ0HpyBb3ftuc'
            elif temp_value>36:
                if playing!='spotify:playlist:3isO1HYQnMyceoe7OLeqaY':
                    print("Playing very hot songs...")
                    play_text("freezing to death with music")
                    sp.start_playback(device_id=device_id, context_uri='spotify:playlist:3isO1HYQnMyceoe7OLeqaY')
                    playing = 'spotify:playlist:3isO1HYQnMyceoe7OLeqaY'
                
    print(f"Playing on device: {device_id}")
except KeyboardInterrupt:
    print("Program interrupted.")

finally:
    arduino.close()
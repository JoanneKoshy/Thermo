<img width="1280" alt="readme-banner" src="https://github.com/user-attachments/assets/35332e92-44cb-425b-9dff-27bcf1023c6c">

# [Thermo-tunes] 🎯


## Basic Details
### Team Name: [Optimus]


### Team Members
- Team Lead: [Joanne Alice Thomas] - [MITS]
- Member 2: [Basil Mathews Biju] - [MITS]
- Member 3: [Vasudev Reji] - [MITS]

### Project Description
This project brings together temperature sensing and music to create the ultimate vibe control! Using an Arduino and Spotify, it reads the room temperature and plays matching playlists—from chilly tunes when it's cold to fiery beats when it’s hot. Just sit back, let the temperature decide the music, and enjoy the perfect soundtrack for every room climate!

### The Problem (that doesn't exist)
Ever find yourself freezing cold but listening to the hottest summer hits? Or sweating through an intense heatwave with smooth, icy jazz playing in the background? That’s just chaos! Our project solves this nonexistent yet totally essential problem: matching the room's vibe with the right music temperature. Because why shouldn't your playlist be as chill or as spicy as your surroundings?

### The Solution (that nobody asked for)
Enter our over-engineered, totally unnecessary, but super fun solution: a temperature-sensitive DJ! We’ve rigged up an Arduino to read the room’s temperature, then paired it with Spotify to play the “right” tunes—chill songs for cool temps, fire tracks for the heat, and even a few surprise playlists when it’s just right. It’s like having a personal DJ that’s way too invested in the thermostat!

## Technical Details
### Technologies/Components Used
For Software:
- Python (for Spotify API interaction and serial communication)
- Arduino/C++ (for microcontroller programming and sensor data processing)
- N/A (Standalone Python and Arduino applications)
- pyttsx3: Provides text-to-speech capabilities for vocal notifications upon temperature changes.
- spotipy: Interfaces with Spotify’s Web API, enabling playlist control based on temperature.
- serial: Manages serial communication between the Arduino and the computer.
  - *Arduino:*
    - DHT: Enables temperature and humidity data acquisition from the DHT11 sensor.
    - Wire and LiquidCrystal_I2C: Facilitates I2C communication with the LCD, displaying live temperature readings.

- *Tools Used:*  
  - Arduino IDE: For programming and uploading code to the Arduino board.
  - Spotify Developer Console: Used to set up API credentials for Spotify integration.



For Hardware:
- *Main Components:*
  - *Arduino UNO*: Acts as the main controller, handling sensor readings and communicating with the connected computer.
  - *DHT11 Temperature and Humidity Sensor*: Measures ambient temperature, providing the data that determines music selection.
  - *16x2 I2C LCD Display*: Displays real-time temperature readings directly on the setup, giving a visual temperature indicator.

- *Specifications:*
  - *DHT11 Sensor*: Provides temperature readings in the range of 0-50°C and humidity as supplementary data.
  - *LCD Display*: 16x2 character display with I2C interface, simplifying wiring and control.

- *Additional Tools Required:*
  - USB Cable: For Arduino-to-computer connection.
  - Breadboard and Jumper Wires: For quick prototyping and wiring.
  - Soldering Tools (optional): For creating a more permanent setup if desired.

---




### Project Documentation
For Software:
![Screenshot1]
https://github.com/JoanneKoshy/Thermo/blob/main/Screenshot%20(53).png

This is the output pic shown in the vsc while the code is running and the music is playing

![Screenshot2]
https://github.com/JoanneKoshy/Thermo/blob/main/Screenshot%20(55).png

This is another pic of the vsc code running

![Screenshot3]

https://github.com/JoanneKoshy/Thermo/blob/main/Screenshot%202024-10-30%20222750.png
This pic is the running of the code in Arduino ide



For Hardware:

# Schematic & Circuit
![Circuit]
https://github.com/JoanneKoshy/Thermo/blob/main/archi.jpg

This shows the whole architerctural flow of the circuit built and its code working

# Build Photos
![Components]
https://github.com/JoanneKoshy/Thermo/blob/main/compo.jpg
The components used are Arduino uno board, Jumper Wires, Dht11 temperature sensor, LCD for display

![Build]
https://github.com/JoanneKoshy/Thermo/blob/main/mid.jpg
Here the temperature which has been read from the arduino is processed by the python script and the spotify playlist plays the desired song according to the temperture inputs.

![Final]
https://github.com/JoanneKoshy/Thermo/blob/main/final.jpg
The temperature is read and then the spotify plays the song according to the input. 
The playlist which plays are different for each temperature range, it is possible because we passed the spotify playlist Uri.

### Project Demo
# Video
https://github.com/JoanneKoshy/Thermo/blob/main/video.mp4
https://github.com/JoanneKoshy/Thermo/blob/main/video2.mp4

The hardware and the software integration is running and the temperature is being succesfully displayed in the lcd, and according to the change in the temperature range changes, the playlist feeded in through spotify is being played according to that. 
The desired connection is done succesfully and we have integrated music and programming together.

## Team Contributions
- [Joanne Alice Thomas]: [Software configuration]
- [Basil Mathews Biju]: [Arduino configuration]
- [Vasudev Reji]: [Hardware configuration]

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProject--24-24?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)



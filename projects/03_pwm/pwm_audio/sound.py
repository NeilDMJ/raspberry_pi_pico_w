melody = [] # this list will hold the melodies (see melodies.py)

notes = ['Minuet in G - Petzold', 140, 'NOTE_D5', '4', 'NOTE_G4', '8', 'NOTE_A4', '8', 'NOTE_B4', '8', 'NOTE_C5', '8', 'NOTE_D5', '4', 'NOTE_G4', '4', 'NOTE_G4', '4', 'NOTE_E5', '4', 'NOTE_C5', '8', 'NOTE_D5', '8', 'NOTE_E5', '8', 'NOTE_FS5', '8', 'NOTE_G5', '4', 'NOTE_G4', '4', 'NOTE_G4', '4', 'NOTE_C5', '4', 'NOTE_D5', '8', 'NOTE_C5', '8', 'NOTE_B4', '8', 'NOTE_A4', '8', 'NOTE_B4', '4', 'NOTE_C5', '8', 'NOTE_B4', '8', 'NOTE_A4', '8', 'NOTE_G4', '8', 'NOTE_FS4', '4', 'NOTE_G4', '8', 'NOTE_A4', '8', 'NOTE_B4', '8', 'NOTE_G4', '8', 'NOTE_A4', '-2', 'NOTE_D5', '4', 'NOTE_G4', '8', 'NOTE_A4', '8', 'NOTE_B4', '8', 'NOTE_C5', '8', 'NOTE_D5', '4', 'NOTE_G4', '4', 'NOTE_G4', '4', 'NOTE_E5', '4', 'NOTE_C5', '8', 'NOTE_D5', '8', 'NOTE_E5', '8', 'NOTE_FS5', '8', 'NOTE_G5', '4', 'NOTE_G4', '4', 'NOTE_G4', '4', 'NOTE_C5', '4', 'NOTE_D5', '8', 'NOTE_C5', '8', 'NOTE_B4', '8', 'NOTE_A4', '8', 'NOTE_B4', '4', 'NOTE_C5', '8', 'NOTE_B4', '8', 'NOTE_A4', '8', 'NOTE_G4', '8', 'NOTE_A4', '4', 'NOTE_B4', '8', 'NOTE_A4', '8', 'NOTE_G4', '8', 'NOTE_FS4', '8', 'NOTE_G4', '-2', 'NOTE_D5', '4', 'NOTE_G4', '8', 'NOTE_A4', '8', 'NOTE_B4', '8', 'NOTE_C5', '8', 'NOTE_D5', '4', 'NOTE_G4', '4', 'NOTE_G4', '4', 'NOTE_E5', '4', 'NOTE_C5', '8', 'NOTE_D5', '8', 'NOTE_E5', '8', 'NOTE_FS5', '8', 'NOTE_G5', '4', 'NOTE_G4', '4', 'NOTE_G4', '4', 'NOTE_C5', '4', 'NOTE_D5', '8', 'NOTE_C5', '8', 'NOTE_B4', '8', 'NOTE_A4', '8', 'NOTE_B4', '4', 'NOTE_C5', '8', 'NOTE_B4', '8', 'NOTE_A4', '8', 'NOTE_G4', '8', 'NOTE_FS4', '4', 'NOTE_G4', '8', 'NOTE_A4', '8', 'NOTE_B4', '8', 'NOTE_G4', '8', 'NOTE_A4', '-2', 'NOTE_D5', '4', 'NOTE_G4', '8', 'NOTE_A4', '8', 'NOTE_B4', '8', 'NOTE_C5', '8', 'NOTE_D5', '4', 'NOTE_G4', '4', 'NOTE_G4', '4', 'NOTE_E5', '4', 'NOTE_C5', '8', 'NOTE_D5', '8', 'NOTE_E5', '8', 'NOTE_FS5', '8', 'NOTE_G5', '4', 'NOTE_G4', '4', 'NOTE_G4', '4', 'NOTE_C5', '4', 'NOTE_D5', '8', 'NOTE_C5', '8', 'NOTE_B4', '8', 'NOTE_A4', '8', 'NOTE_B4', '4', 'NOTE_C5', '8', 'NOTE_B4', '8', 'NOTE_A4', '8', 'NOTE_G4', '8', 'NOTE_A4', '4', 'NOTE_B4', '8', 'NOTE_A4', '8', 'NOTE_G4', '8', 'NOTE_FS4', '8', 'NOTE_G4', '-2', 'NOTE_B5', '4', 'NOTE_G5', '8', 'NOTE_A5', '8', 'NOTE_B5', '8', 'NOTE_G5', '8', 'NOTE_A5', '4', 'NOTE_D5', '8', 'NOTE_E5', '8', 'NOTE_FS5', '8', 'NOTE_D5', '8', 'NOTE_G5', '4', 'NOTE_E5', '8', 'NOTE_FS5', '8', 'NOTE_G5', '8', 'NOTE_D5', '8', 'NOTE_CS5', '4', 'NOTE_B4', '8', 'NOTE_CS5', '8', 'NOTE_A4', '4', 'NOTE_A4', '8', 'NOTE_B4', '8', 'NOTE_CS5', '8', 'NOTE_D5', '8', 'NOTE_E5', '8', 'NOTE_FS5', '8', 'NOTE_G5', '4', 'NOTE_FS5', '4', 'NOTE_E5', '4', 'NOTE_FS5', '4', 'NOTE_A4', '4', 'NOTE_CS5', '4', 'NOTE_D5', '-2', 'NOTE_D5', '4', 'NOTE_G4', '8', 'NOTE_FS5', '8', 'NOTE_G4', '4', 'NOTE_E5', '4', 'NOTE_G4', '8', 'NOTE_FS4', '8', 'NOTE_G4', '4', 'NOTE_D5', '4', 'NOTE_C5', '4', 'NOTE_B4', '4', 'NOTE_A4', '8', 'NOTE_G4', '8', 'NOTE_FS4', '8', 'NOTE_G4', '8', 'NOTE_A4', '4', 'NOTE_D4', '8', 'NOTE_E4', '8', 'NOTE_FS4', '8', 'NOTE_G4', '8', 'NOTE_A4', '8', 'NOTE_B4', '8', 'NOTE_C5', '4', 'NOTE_B4', '4', 'NOTE_A4', '4', 'NOTE_B4', '8', 'NOTE_D5', '8', 'NOTE_G4', '4', 'NOTE_FS4', '4', 'NOTE_G4', '-2']
melody.append(notes)

notes = {
"NOTE_B0": 31,
"NOTE_C1": 33,
"NOTE_CS1": 35,
"NOTE_D1": 37,
"NOTE_DS1": 39,
"NOTE_E1": 41,
"NOTE_F1": 44,
"NOTE_FS1": 46,
"NOTE_G1": 49,
"NOTE_GS1": 52,
"NOTE_A1": 55,
"NOTE_AS1": 58,
"NOTE_B1": 62,
"NOTE_C2": 65,
"NOTE_CS2": 69,
"NOTE_D2": 73,
"NOTE_DS2": 78,
"NOTE_E2": 82,
"NOTE_F2": 87,
"NOTE_FS2": 93,
"NOTE_G2": 98,
"NOTE_GS2": 104,
"NOTE_A2": 110,
"NOTE_AS2": 117,
"NOTE_B2": 123,
"NOTE_C3": 131,
"NOTE_CS3": 139,
"NOTE_D3": 147,
"NOTE_DS3": 156,
"NOTE_E3": 165,
"NOTE_F3": 175,
"NOTE_FS3": 185,
"NOTE_G3": 196,
"NOTE_GS3": 208,
"NOTE_A3": 220,
"NOTE_AS3": 233,
"NOTE_B3": 247,
"NOTE_C4": 262,
"NOTE_CS4": 277,
"NOTE_D4": 294,
"NOTE_DS4": 311,
"NOTE_E4": 330,
"NOTE_F4": 349,
"NOTE_FS4": 370,
"NOTE_G4": 392,
"NOTE_GS4": 415,
"NOTE_A4": 440,
"NOTE_AS4": 466,
"NOTE_B4": 494,
"NOTE_C5": 523,
"NOTE_CS5": 554,
"NOTE_D5": 587,
"NOTE_DS5": 622,
"NOTE_E5": 659,
"NOTE_F5": 698,
"NOTE_FS5": 740,
"NOTE_G5": 784,
"NOTE_GS5": 831,
"NOTE_A5": 880,
"NOTE_AS5": 932,
"NOTE_B5": 988,
"NOTE_C6": 1047,
"NOTE_CS6": 1109,
"NOTE_D6": 1175,
"NOTE_DS6": 1245,
"NOTE_E6": 1319,
"NOTE_F6": 1397,
"NOTE_FS6": 1480,
"NOTE_G6": 1568,
"NOTE_GS6": 1661,
"NOTE_A6": 1760,
"NOTE_AS6": 1865,
"NOTE_B6": 1976,
"NOTE_C7": 2093,
"NOTE_CS7": 2217,
"NOTE_D7": 2349,
"NOTE_DS7": 2489,
"NOTE_E7": 2637,
"NOTE_F7": 2794,
"NOTE_FS7": 2960,
"NOTE_G7": 3136,
"NOTE_GS7": 3322,
"NOTE_A7": 3520,
"NOTE_AS7": 3729,
"NOTE_B7": 3951,
"NOTE_C8": 4186,
"NOTE_CS8": 4435,
"NOTE_D8": 4699,
"NOTE_DS8": 4978
}

from machine import Pin, PWM
from utime import sleep # import notes.py

buzzer = PWM(Pin(20))   # pin where buzzer is connected
button = Pin(15, Pin.IN, Pin.PULL_UP)  # pin where you may connect a button

track = 0      # choose track here (see the list in melodies.py)
volume = 600   # set volume to a value between 0 and 1000


# functions to play the melodies

def playtone(frequency):
    buzzer.duty_u16(volume)
    buzzer.freq(frequency)

def be_quiet():
    buzzer.duty_u16(0)  # turns sound off

def duration(tempo, t):
    
    # calculate the duration of a whole note in milliseconds (60s/tempo)*4 beats
    wholenote = (60000 / tempo) * 4
    
    # calculate the duration of the current note
    # (we need an integer without decimals, hence the // instead of /)
    if t > 0:
      noteDuration = wholenote // t
    elif (t < 0):
      # dotted notes are represented with negative durations
      noteDuration = wholenote // abs(t)
      noteDuration *= 1.5 # increase their duration by a half
    
    return noteDuration

def playsong(mysong):

    try:
        
        print(mysong[0]) # print title of the song to the shell 
        tempo = mysong[1] # get the tempo for this song from the melodies list 

        # iterate over the notes of the melody. 
        # The array is twice the number of notes (notes + durations)
        for thisNote in range(2, len(mysong), 2):
            
            noteduration = duration(tempo, int(mysong[thisNote+1]))
            
            if (mysong[thisNote] == "REST"):
                be_quiet()
            else:
                playtone(notes[mysong[thisNote]])
            
            sleep(noteduration*0.9/1000) # we only play the note for 90% of the duration...
            be_quiet()
            sleep(noteduration*0.1/1000) # ... and leave 10% as a pause between notes
        
            if button.value()==0: # stop playing this track if button is pushed
                return
            
    except: # make sure the buzzer stops making noise when something goes wrong or when the script is stopped
        be_quiet()
        

playsong(melody[track])  # actually start playing the melody


# the next part allows you to add a button to switch melodies

while True: # constantly keep checking if the button is being pressed
    if button.value()==0: # if it is...
        while button.value()==0: # ...first wait for the button to be unpressed
            sleep(0.1)
        track+=1 # ... and then play the next track
        if track > len(melody):
            track = 0
        print(track)
        playsong(melody[track])  # start playing the melody
    sleep(0.1)
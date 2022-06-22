from microbit import *  # load the microbit library 

## beating heart / any other icon 
small_icon = Image.HEART_SMALL
icon = Image.HEART

def beating_icon():
    """
    display the small icon, delay for a bit, display the larger icon
    """
    for i in range(10):  # repeat 10 times
        display.show(small_icon)
        sleep(500)
        display.show(icon)
        sleep(300)
    
    display.clear()  # clear the display
    return 
#######

## speech and song demo
import music  # for playing notes
import speech # for text to speech   
    
# play a list of notes - star wars theme 

def play_tune():
    """
    play a tune given as a list of tunes in the format NOTE{SCALE}:DURATION
    https://microbit-micropython.readthedocs.io/en/latest/tutorials/music.html 
    """
    sw_tune = ['G4:4', 'R:1', 'G4:4', 'R:1', 'G4:4', 'R:1', 
               'C4:5', 'C4:5', 'G4:5', 'G4:5', 'F4:2', 'R:1',
               'E4:2', 'R:1', 'D4:4', 'C6:5', 'C6:5', 'G4:5', 'F4:4', 'R:1'
               'E4:4', 'R:1', 'D4:4', 'C6:5', 'C6:5', 'G4:5']

    music.play(sw_tune)
    music.play(sw_tune)
    
    return 


def say_words():
    """
    say words 
    https://microbit-micropython.readthedocs.io/en/latest/tutorials/speech.html 
    """    
    vader_words = 'No, I am your father'
    han_words = 'that is no moon, it is a space station'

    speech.say(vader_words, pitch=200, speed=125, mouth=150, throat=125)
    sleep(500)
    speech.say(han_words, speed=125)
    
    return 
##### 

### roll dice on shake
import random 

def roll_dice():
    roll = random.randint(1, 6)  # pick a random number between 1 and 6
    display.show(roll)
    sleep(2000)  # sleep for 2 seconds
    display.clear()
    
    return 
##### 

while True:
    # display.scroll('Hello, World!')
    if button_a.is_pressed():
        # play_tune()
        say_words()
    if button_b.is_pressed():
        beating_icon()

    if accelerometer.was_gesture('shake'):
        roll_dice()
    

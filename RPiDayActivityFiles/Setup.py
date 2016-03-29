import RPi.GPIO as GPIO
import time
import os

# Using the BCM layout instead of the physical pin layout
GPIO.setmode (GPIO.BCM)
GPIO.setwarnings(False)

# Pin number of the PIR Sensor
sensor = 23
# We want the start start of the pin to be down. 
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

# Select the headphone jack for audio
os.system('sudo amixer cset numid=3 1')

def CheckForMotion():
    return GPIO.input(sensor)

def CheckForMotion(pin):
    return GPIO.input(pin)

def SoundTheAlarm():
    os.system('mpg123 -q alarm.mp3 &')

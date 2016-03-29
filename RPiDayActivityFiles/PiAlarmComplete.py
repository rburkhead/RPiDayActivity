from Setup import *

print ("Starting the readings")

while (True):
    if CheckForMotion(23)== False:
        print ("No Motion")
    else:
        print ("Motion Detected")
        SoundTheAlarm()
        time.sleep(4)
    time.sleep(1)
    






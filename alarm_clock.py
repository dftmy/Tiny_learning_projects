from datetime import datetime
from playsound import playsound
alarm_hour = int(input("Hour of alarm: "))
alarm_min = int(input("Minute of alarm: "))


while True:
    if alarm_hour == datetime.now().hour and alarm_min == datetime.now().minute:
        print("wake the fuck up samurai!")
        playsound("sound.wav")
        break
        


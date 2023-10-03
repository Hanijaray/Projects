import random
import winsound
frequency = 1000
duration = 2000
temp = random.randint(25,50)
print("Temperature is:",temp)
hum = random.randint(30,70)
print("Humidity is :",hum)
if(temp >= 40):
    winsound.Beep(frequency,duration)
    print("High Temperature")
else:
    print("Normal temperature")
if(hum >= 60):
    winsound.Beep(frequency,duration)
    print("High Humidity")
else:
    print("Normal Humidity")



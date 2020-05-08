import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

# Welcome message
print("looking for cards")
print("Press ctrl-c to stop")

try:
     id, text = reader.read()
     print(id)
     print(text)

finally :
        GPIO.cleanup()

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        text = raw_input('Enter item')
        print("place the card")
        reader.write(text)
        print("success")
finally:
        GPIO.cleanup()

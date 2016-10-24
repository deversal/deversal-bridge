import deversal
import RPi.GPIO as GPIO
import time

#deversal init
device = deversal.Device("0xE8eb35AFBA98fdE9071308b4F7cfB844EE5bf666", "localhost", "1337")

#setup the raspberry pi settings
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)

def refresh():    
    status = device.getValue()
    action_state = status["action_state"]
    return action_state

while True:
    action_state = refresh()
    if action_state == "true":
        print "on"
        GPIO.output(11, GPIO.HIGH)
    else:
        print "off"
        GPIO.output(11, GPIO.LOW)
    time.sleep(5)
#GPIO.cleanup()

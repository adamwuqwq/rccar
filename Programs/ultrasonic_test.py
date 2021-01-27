#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.IN)
GPIO.output(17, GPIO.LOW)
time.sleep(0.3)

def reading():
    GPIO.output(17, True)
    time.sleep(0.00001)
    GPIO.output(17, False)
    while GPIO.input(27) == 0:
        signaloff = time.time()
    while GPIO.input(27) == 1:
        signalon = time.time()
    timepassed = signalon - signaloff
    distance = timepassed * 17000
    if distance < 500:
        return distance
    else:
        return 500
    GPIO.cleanup()

while True:
    dist=reading()
    print(dist)
    time.sleep(1)
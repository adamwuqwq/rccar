import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

def led(mode):
	if(mode==1):
		GPIO.output(2, GPIO.HIGH)
	else:
		GPIO.output(2,GPIO.LOW)

while True:
	led(1)
	time.sleep(0.5)
	led(0)
	time.sleep(0.5)


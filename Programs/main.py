# coding: utf-8
import webiopi
import time
import RPi.GPIO as GPIO

webiopi.setDebug()
GPIO.setwarnings(False)

#initial setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(15,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(18,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(24,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(17,GPIO.OUT,initial=GPIO.LOW) #ultrasonic
GPIO.setup(27,GPIO.IN) #ultrasonic
GPIO.setup(2,GPIO.OUT,initial=GPIO.LOW) #led
GPIO.output(14,0)
GPIO.output(15,0)
pwmS=GPIO.PWM(24,50) #submotorpwm
pwmD=GPIO.PWM(18,50) #dcmotorpwm
pwmD.start(0)
pwmS.start(0)
pwmS.ChangeDutyCycle(8.4)

@webiopi.macro
def servo_freq(freq):
    global pwmS
    pwmS.ChangeFrequency(int(freq))

@webiopi.macro
def servo_duty(duty):
    global pwmS
    pwmS.ChangeDutyCycle(float(duty))

@webiopi.macro
def dc_freq(freq):
    global pwmD
    pwmD.ChangeFrequency(int(freq))

@webiopi.macro
def dc_duty(duty):
    global pwmD
    pwmD.ChangeDutyCycle(float(duty))

@webiopi.macro
def pwm_stop():
    global pwmS,pwmD
    pwmD.stop()
    pwmS.stop()

@webiopi.macro
def output_control(io,value):
    GPIO.output(int(io),int(value))

@webiopi.macro
def sleep():
    webiopi.sleep(5)
    
@webiopi.macro
def distance():
    GPIO.output(17, True)
    time.sleep(0.00001)
    GPIO.output(17, False)
    while GPIO.input(27) == 0:
        signaloff = time.time()
    while GPIO.input(27) == 1:
        signalon = time.time()
    timepassed = signalon - signaloff
    distance = timepassed * 17000
    if(distance<150):
        return distance
    else:
        return 150

    
#output_control(14,0)
#output_control(15,1)
#dc_duty(20)
#time.sleep(5)


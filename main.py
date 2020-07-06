import RPi.GPIO
import time
import argparse
import math
import serial
#### ARDUINO SETUP
## open the serial port that your ardiono
## is connected to.


def setup():
	ser = serial.Serial("/dev/cu.usbmodem1421", 9600)
	GPIO.setmode(GPIO.BOARD)
	TRIG = 23
	ECHO = 24
	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)
	GPIO.output(TRIG, False)

def distancedetct():
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	while GPIO.input(ECHO)==0:
		pulse_start = time.time()
	while GPIO.input(ECHO)==1:
		pulse_end = time.time()
	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration x 17150
	distance = round(distance, 2)
	return distance
	
	
	
	
	
def move(stepper, dir, time):
	'''Moves the specified stepper to the supplied angle.    
	Arguments:
    stepper no 
	the stepper direction, 1 or 0
	the time or steps done
	'''
    



#Very simply returns the user's input
def readInput(prompt):
	usrInput = input(prompt)
	return usrInput


    
   


                              
                              


import RPi.GPIO
import time
import argparse
import math
import serial
import random

Error = 5

maxLeftDistance = 0
maxRightDistance = 0

#### ARDUINO SETUP
## open the serial port that your ardiono
## is connected to.
def setup():
	GPIO.setmode(GPIO.BOARD)
	#Set up Left Ultrasonic sensor
	TRIGLeft = 23
	ECHOLeft = 24
	GPIO.setup(TRIGLeft,GPIO.OUT)
	GPIO.setup(ECHOLeft,GPIO.IN)
	GPIO.output(TRIGLeft, False)
	#Set up right Ultrasonic sensor 
	TRIGRight = 25
	ECHORight = 26
	GPIO.setup(TRIGRight,GPIO.OUT)
	GPIO.setup(ECHORight,GPIO.IN)
	GPIO.output(TRIGRight, False)
	#Set up error pin
	GPIO.setup(Error,GPIO.OUT)
	GPIO.output(Error, False)
	
def serialSetup():
	ser = serial.Serial("/dev/cu.usbmodem1421", 9600)
	while True:
		try:
			ser.write("Pi ON")
		except:
			print("Error Serial not connected")
			GPIO.output(Error, True)
		if ser.read == "Connected"
			break
	
			
def distancedetectLeft():
	GPIO.output(TRIGLeft, True)
	time.sleep(0.00001)
	GPIO.output(TRIGLeft, False)
	while GPIO.input(ECHOLeft)==0:
		pulse_start = time.time()
	while GPIO.input(ECHOLeft)==1:
		pulse_end = time.time()
	pulse_duration = pulse_end - pulse_start
	distanceLeft = pulse_duration x 17150
	distanceLeft = round(distanceLeft, 2)
	return distanceLeft
	
def distancedetectRight():
	GPIO.output(TRIGRight, True)
	time.sleep(0.00001)
	GPIO.output(TRIGRight, False)
	while GPIO.input(ECHORight)==0:
		pulse_start = time.time()
	while GPIO.input(ECHORight)==1:
		pulse_end = time.time()
	pulse_duration = pulse_end - pulse_start
	distanceRight = pulse_duration x 17150
	distanceRight = round(distanceRight, 2)
	return distanceRight


def distancechecks():
	distancedetectLeft()
	distancedetectRight()
	if (distanceLeft < maxLeftDistance or distanceLeft > maxLeftDistance):
		print("Left OBJECT")
		distancedetectLeft()
		distancedetectRight()
		
		if (distanceLeft > distanceRight)
		  move('Forward')
		elif (distanceLeft < distanceRight) {
		  move('Right')
	elif (distanceRight < maxRightDistance or distanceRight > maxRightDistance):
		print("Left OBJECT")
		distancedetectLeft()
		distancedetectRight()
		
		if (distanceLeft < distanceRight)
			move('Forward', 1)
		elif (distanceLeft > distanceRight) {
			move('Left', 1)
	elif (distanceRight > maxRightDistance and distanceLeft > maxLeftDistance):
		move("Backward", 1)
	
	
	
	
	
def serialSend(message, int, float):
	ser.write(startmarker)
	ser.write(message,int,float)
	ser.write(endmarker)
	
def move(Dir, rot):
	'''Moves the specified stepper to the amount of steps.    
	'''
    if Dir == 'Forward':
		serialSend(Dir, rot)
		print(Dir)
	elif Dir == 'Left'
		serialSend(Dir, rot)
		print(Dir)
	elif Dir == 'Right'
		serialSend(Dir, rot)
		print(Dir)
#Very simply returns the user's input
def readInput(prompt):
	usrInput = input(prompt)
	return usrInput

def switchcase(argument):
		switcher = { 
		0: "Forward", 
		1: "Left", 
		2: "Right", 
		3: "Aroundleft",
		4: "Aroundright",
	} 
  
	# get() method of dictionary data type returns  
	# value of passed argument if it is present  
	# in dictionary otherwise second argument will 
	# be assigned as default value of passed argument 
	return switcher.get(argument, "nothing") 
	
def autonomous
	serialSend('Led',0)
	while True:
		distancechecks()
		no = randrange(5) 
		chosen = switchcase(no)
		print(chosen)
		move(chosen, 1)
if __name__ == '__main__':
	setup()
	serialSetup()
                              
                              

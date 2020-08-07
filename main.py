
import RPi.GPIO as GPIO
import time
import argparse
import math
import serial
import random



Error = 5
maxLeftDistance = 0
maxRightDistance = 0
line = ""
startmarker = "<"
endmarker = ">"
TRIGLeft = 17
ECHOLeft = 27
TRIGRight = 22
ECHORight = 23



def setup():
	GPIO.setmode(GPIO.BOARD)
	#Set up Left Ultrasonic sensor
	GPIO.setup(TRIGLeft,GPIO.OUT)
	GPIO.setup(ECHOLeft,GPIO.IN)
	GPIO.output(TRIGLeft, False)
	#Set up right Ultrasonic sensor 
	GPIO.setup(TRIGRight,GPIO.OUT)
	GPIO.setup(ECHORight,GPIO.IN)
	GPIO.output(TRIGRight, False)
	#Set up error pin
	GPIO.setup(Error,GPIO.OUT)
	GPIO.output(Error, False)
	
#### ARDUINO SETUP
## open the serial port that your ardiono
## is connected to.
def serialSetup():
	global ser
	ser = serial.Serial("/dev/ttyUSB0", 9600)
	ser.flush()
	serialtest()
	
	
def serialSend(message, int, float):
	sdata = startmarker + message + "," + str(int) + "," + str(float) + endmarker
	ser.write(sdata.encode('utf-8'))
	
	
def serialreceive():
	global line
	if ser.in_waiting > 0:
		line = ser.readline().decode('utf-8').rstrip()
		ser.flush()
		return line		
		
def serialtest():
	while True:
		serialSend("Pi ON" , 0 ,1.1)
		time.sleep(1)
		serialreceive()
		print(line)
		if line == "Connected":
			serialSend("confirm", 1 ,1.1)
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
	distanceLeft = pulse_duration * 17150
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
	distanceRight = pulse_duration * 17150
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
	
	

	
def move(Dir, rot):
	'''Moves the specified stepper to the amount of steps.    
	'''
    if Dir == 'Forward':
		serialSend(Dir, rot)
		print(Dir)
	elif Dir == 'Left':
		serialSend(Dir, rot)
		print(Dir)
	elif Dir == 'Right':
		serialSend(Dir, rot)
		print(Dir)
	elif Dir == 'Aroundright':
		serialSend(Dir, rot)
		print(Dir)	
	elif Dir == 'Aroundleft':
		serialSend(Dir, rot)
		print(Dir)	
	else:
		GPIO.output(Error, True)
		print("Error, Unknown movement called")
		time.sleep(5)
		GPIO.output(Error, False)
		
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
 

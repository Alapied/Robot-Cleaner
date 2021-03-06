
import RPi.GPIO as GPIO
import time
import argparse
import math
import serial

GPIO.setwarnings(False)
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
	GPIO.setmode(GPIO.BCM)
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
			
#######################################
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
	print(distanceLeft)
	
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
	print(distanceRight)


def ledchange(mode):
	if mode == 'Red':
		serialSend('led', 1, 1.1)
	if mode == 'Green':
		serialSend('led', 0, 1.2)
	if mode == 'Blue':
		serialSend('led', 2, 1.3)
	if mode == 'Boot':
		serialSend('led', 3, 1.4)
	

			
def move(Dir, rot):
	'''Moves the specified stepper to the amount of steps.    
	'''
	if Dir == 'Forward':
		serialSend(Dir, rot,1.1)
		print(Dir)
	elif Dir == 'Left':
		serialSend(Dir, rot, 1.2)
		print(Dir)
	elif Dir == 'Right':
		serialSend(Dir, rot, 1.3)
		print(Dir)
	elif Dir == 'Backward':
		serialSend(Dir, rot, 1.4)
		print(Dir)
	
#Very simply returns the user's input
def readInput(prompt):
	usrInput = input(prompt)
	return usrInput

def LEDtests():
	print("Beginning LED Serial Tests")
	time.sleep(1)
	
	ledchange('Red')
	time.sleep(1)
	
	ledchange('Green')
	time.sleep(1)
	
	ledchange('Blue')
	time.sleep(1)
	
	
	
def steppertest():
	
	print("Beginning Stepper Serial Tests")
	time.sleep(1)
	
	move("Forward", 1)
	time.sleep(1)
	
	move("Backward", 1)
	time.sleep(1)
	
	move("Left", 1)
	time.sleep(1)
	
	move("Right", 1)
	time.sleep(1)
	
def distancetests():
	print("Starting distance test")
	time.sleep(1)
	distancedetectRight()
	distancedetectLeft()
	print ('Distance Tests Done')
	
if __name__ == '__main__':
	setup()
	serialSetup()				  
	time.sleep(5)
	distancetests()
	time.sleep(5)
	LEDtests()
	
	time.sleep(5)
	steppertest()
import RPi.GPIO
import time
import argparse
import math
import serial


Error = 5



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
			ser.write("Connected?")
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

def serialSend(message, int, float):
	ser.write(startmarker)
	ser.write(message,int,float)
	ser.write(endmarker)
	
def move(Dir, rot):
	'''Moves the specified stepper to the amount of steps.    
	'''
    if Dir == Forward:
		serialSend("Forward", rot)
	elif Dir == Left
		serialSend("Left", rot)

#Very simply returns the user's input
def readInput(prompt):
	usrInput = input(prompt)
	return usrInput


    
if __name__ == '__main__':
	setup()


                              
                              

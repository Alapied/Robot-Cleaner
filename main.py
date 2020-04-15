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
    '''Moves the specified servo to the supplied angle.
        
        Arguments:
        servo
        the servo number to command, an integer from 1-4
        angle
        the desired servo angle, an integer from 0 to 180
        
        (e.g.) >>> servo.move(2, 90)
        ... # "move servo #2 to 90 degrees"'''
    
    if (0 <= angle <= 180):
        ser.write(chr(255))
        ser.write(chr(servo))
        ser.write(chr(angle))
    else:
        print "Servo angle must be an integer between 0 and 180.\n"



#Very simply returns the user's input
def readInput(prompt):
    usrInput = input(prompt)
    return usrInput


    
   
    
    move(2, servoFB)
    '''if servoFB > 120:
        servoFB = 160
    elif servoFB < 30:
        servoFB = 20
    else:
        servoFB = servoFB'''
    move(3, servoTB)
   


                              
                              

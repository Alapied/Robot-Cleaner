#! /usr/bin/python

#Import Libraries
import RPi.GPIO as GPIO
import time
import os
import datetime
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
from multiprocessing import Pool
import subprocess

main = "main.py"
robotarm = "robotArm.py"

DebugInfo = ' [Info] '
DebugWarn = ' [Warning] '
DebugErr = ' [Error] '


def run_process(process):                                                             
    os.system('python {}'.format(process))
	

if __name__ == '__main__':
	print(str(datetime.datetime.now()) + DebugInfo +'Beginning Startup process')
	#Creates two seperate processes for both python scripts
	processes = (main, robotarm)
	pool = Pool(processes=2)
	pool.map(run_process, processes)  
	

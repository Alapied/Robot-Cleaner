# Robot-cleaner
This is The Systems Enginnering Project to make an autonmous roomba that will pick small items up that would normally jam a standard Robot Vacumn.

Note: I have no idea what i'm doing so don't expect this to be the cleanest code or the most efficent way of performing a task, it just intends to work as a concept.


## What even is this

This is a OpenCV and Python based autonomus script, it uses multiprocessing in order to run both a computer vision script and autonmous movement contolling steppers and etc 
startThreads.py is the starting script which pools the scripts to be run by one command and then split into two processes (for ease of fuctioning and code complexity i keep telling myself) This will run main.py and robotArm.py, main contains the random and control scripts for the steppers and other functions while robotArm.py initalises an opencv process for object detection and control of the servos in the arm. The ino files are ment to be uploaded to different arduinos and connected via usb.


## Credits
### Opencv-arm control:
https://github.com/ashishtilakarora/Robot-Arm-OpenCV (cloned and modified for purpose)

### Installations and gathering Libaries:
 Adrian Rosebrock and his blog PyImageSearch

### Argument Parsing from serial:
Robin2 and his post on Serial Basics on the Arduino Forums (example was used)

### Driver and stepper control:
https://lastminuteengineers.com/a4988-stepper-motor-driver-arduino-tutorial/

### Colision Avoidence:
Jorge Rance and his HC-SR04 robot

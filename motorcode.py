import time
import math
import RPi.GPIO as GPIO

EN = 7
MS1 = 11
MS2 = 13
MS3 = 15
stp = 16
dir = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(EN, GPIO.OUT)
GPIO.setup(MS1, GPIO.OUT)
GPIO.setup(MS2, GPIO.OUT)
GPIO.setup(MS3, GPIO.OUT)
GPIO.setup(stp, GPIO.OUT)
GPIO.setup(dir, GPIO.OUT)



#Variables
count = 0
rpm				#Revolutions per minute
TPI	= 16		#Threads per inch
DISTANCE = 10	#Between hinge and drive bolt


def resetBEDPins():
	GPIO.output(stp, GPIO.LOW)
	GPIO.output(dir, GPIO.LOW)
	GPIO.output(MS1, GPIO.LOW)
	GPIO.output(MS2, GPIO.LOW)
	GPIO.output(MS3, GPIO.LOW)
	GPIO.output(EN, GPIO.HIGH)

def smallStepMode():
	GPIO.output(dir, GPIO.LOW)
	GPIO.output(MS1, GPIO.HIGH)
	GPIO.output(MS2, GPIO.HIGH)
	GPIO.output(MS3, GPIO.HIGH)
	for i in range(0, 3200):
		GPIO.output(stp, GPIO.HIGH)
		time.sleep(.01)
		GPIO.output(stp, GPIO.LOW)
		time.sleep(.01)

def steps():

	rpm = DISTANCE * (((2 * Math.pi) / 1436) * TPI)
	steps = RPM / 3200
	return steps

while (True):
	if count < 1:
		GPIO.output(EN, GPIO.LOW)
		smallStepMode()
		resetBEDPins()
		count += 1

GPIO.cleanup()
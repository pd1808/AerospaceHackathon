import time
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

count = 0

def resetBEDPins():
	GPIO.output(stp, GPIO.LOW)
	GPIO.output(dir, GPIO.LOW)
	GPIO.output(MS1, GPIO.LOW)
	GPIO.output(MS2, GPIO.LOW)
	GPIO.output(MS3, GPIO.LOW)
	GPIO.output(EN, GPIO.HIGH)

def smallStepMode():
	GPIO.output(dir, GPIO.HIGH)
	GPIO.output(MS1, GPIO.HIGH)
	GPIO.output(MS2, GPIO.HIGH)
	GPIO.output(MS3, GPIO.HIGH)
	for i in range(0, 3200*5):
		GPIO.output(stp, GPIO.HIGH)
		time.sleep(0.000)
		GPIO.output(stp, GPIO.LOW)
		time.sleep(0.001)

GPIO.output(EN, GPIO.LOW)
smallStepMode()
resetBEDPins()

GPIO.cleanup()

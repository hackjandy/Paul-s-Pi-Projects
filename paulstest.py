from time import  sleep
import RPi.GPIO as GPIO


DIR = 20
STEP = 21
DIRR = 19
STEPP = 26
DIRRR = 14
STEPPP = 15
K1 = 22
K2 = 27
K3 = 17

CW = 1
CCW = 0
SPR = 1600


GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(DIRR, GPIO.OUT)
GPIO.setup(STEPP, GPIO.OUT)
GPIO.setup(STEPPP, GPIO.OUT)
GPIO.setup(DIRRR, GPIO.OUT)
GPIO.setup(K1, GPIO.OUT)
GPIO.setup(K2, GPIO.OUT)
GPIO.setup(K3, GPIO.OUT)
step_count = SPR - 1200
delay = .0009

GPIO.output(DIRR, CW)
GPIO. output(K1, GPIO.LOW)
GPIO.output(K2, GPIO.HIGH)
GPIO.output(K3,GPIO.HIGH)


for x in range(step_count):
	GPIO.output(STEPP, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEPP, GPIO.LOW)
	sleep(delay)


sleep(.5)
print "CW"
GPIO.output(DIRR, CCW)


for x in range(step_count):
	GPIO.output(STEPP, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEPP, GPIO.LOW)
	sleep(delay)

sleep(.5)
print "CCW"
GPIO.output(DIR, CW)
GPIO.output(K1, GPIO.HIGH)
GPIO.output(K2,GPIO.LOW)

for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

sleep(.5)
print "CW2"
GPIO.output(DIR, CCW)

for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

sleep(.5)
print "cCW2"
GPIO.output(DIRRR, CW)
GPIO.output(K2, GPIO.HIGH)
GPIO.output(K3, GPIO.LOW)

for x in range(step_count):
        GPIO.output(STEPPP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEPPP, GPIO.LOW)
        sleep(delay)

sleep(.5)
print "CW3"
GPIO.output(DIRRR, CCW)

for x in range(step_count):
        GPIO.output(STEPPP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEPPP, GPIO.LOW)
        sleep(delay)

GPIO.output(K3, GPIO.HIGH)
print "CCW3"
GPIO.cleanup()


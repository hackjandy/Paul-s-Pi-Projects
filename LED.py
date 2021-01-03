import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_UP)	# Start button 
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)


print "Ready"
print "Green LED 18 on"
print  "Please press start" 
GPIO.output(18,GPIO.HIGH)

while GPIO.input(21):
	time.sleep(0.01)

print "button pushed"
GPIO.output(18,GPIO.LOW)

print "LED 18 off"
print "LED 17 on"
GPIO.output(17,GPIO.HIGH)
time.sleep(2)
GPIO.output(17,GPIO.LOW)
print "LED 17 off"
print "LED 16 on"

GPIO.output(16,GPIO.HIGH)
time.sleep(2)
GPIO.output(16,GPIO.LOW)
print "LED 16 off"
print "LED 15 on"
GPIO.output(15,GPIO.HIGH)
time.sleep(2)
GPIO.output(15,GPIO.LOW)
print "LED 15 off"
print "LED 14 on"
GPIO.output(14,GPIO.HIGH)
time.sleep(2)
GPIO.output(14,GPIO.LOW)
print "LED 14 off"
print "LED 13 on"
GPIO.output(13,GPIO.HIGH)
time.sleep(2)
GPIO.output(13,GPIO.LOW)
print "LED 13 off"
time.sleep(2)
print "cycle complete"



GPIO.setup(21,GPIO.IN)        # Some sort of reset attempt 
GPIO.setup(18,GPIO.IN)
GPIO.cleanup()


from time import sleep
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
START = 16
CW = 1
CCW = 0
SPR = 1600
step_count = SPR - 1200
delay = .0009


def initialize():
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
    GPIO.output(K1, GPIO.HIGH)
    GPIO.output(K2, GPIO.HIGH)
    GPIO.output(K3, GPIO.HIGH)
    GPIO.setup(START, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def cleanup():
    GPIO.output(K3, GPIO.HIGH)
    GPIO.cleanup()


def rotate_motor(gpio_pin, ccw=False):
    if ccw:
        GPIO.output(DIRR, CCW)
        print("CCW")
    else:
        GPIO.output(DIRR, CW)
        print("CW")

    for x in range(step_count):
        GPIO.output(gpio_pin, GPIO.HIGH)
        sleep(delay)
        GPIO.output(gpio_pin, GPIO.LOW)
        sleep(delay)


if __name__ == "__main__":
    initialize()

    print("Waiting")
    print("Green LED 18 on")
    print("Please press start")

    while GPIO.input(START):  # wait for start button
        sleep(.01)

    GPIO.output(K1, GPIO.LOW)
    rotate_motor(STEPP)
    sleep(.5)
    rotate_motor(STEPP, ccw=True)

    sleep(.5)
    GPIO.output(K1, GPIO.HIGH)
    GPIO.output(K2, GPIO.LOW)

    rotate_motor(STEP)
    sleep(.5)
    rotate_motor(STEP, ccw=True)

    sleep(.5)
    GPIO.output(K2, GPIO.HIGH)
    GPIO.output(K3, GPIO.LOW)

    rotate_motor(STEPPP)
    sleep(.5)
    rotate_motor(STEPPP, ccw=True)

    print("Cycle Complete")
    cleanup()

from time import sleep
import RPi.GPIO as GPIO

DIRY = 20
STEPY = 21
DIRX = 19
STEPX = 26
DIRZ = 14
STEPZ = 15
K1 = 22
K2 = 27
K3 = 17
START = 16
CW = 1
CCW = 0
SPR = 1600
step_count = SPR - 1200
delay = .0009

motor_to_direction_map = {
    STEPY: DIRY,
    STEPX: DIRX,
    STEPZ: DIRZ
}


def initialize():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIRY, GPIO.OUT)
    GPIO.setup(STEPY, GPIO.OUT)
    GPIO.setup(DIRX, GPIO.OUT)
    GPIO.setup(STEPX, GPIO.OUT)
    GPIO.setup(STEPZ, GPIO.OUT)
    GPIO.setup(DIRZ, GPIO.OUT)
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
        GPIO.output(motor_to_direction_map[gpio_pin], CCW)
        print("CCW")
    else:
        GPIO.output(motor_to_direction_map[gpio_pin], CW)
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
    rotate_motor(STEPX)
    sleep(.5)
    rotate_motor(STEPX, ccw=True)

    sleep(.5)
    GPIO.output(K1, GPIO.HIGH)
    GPIO.output(K2, GPIO.LOW)

    rotate_motor(STEPY)
    sleep(.5)
    rotate_motor(STEPY, ccw=True)

    sleep(.5)
    GPIO.output(K2, GPIO.HIGH)
    GPIO.output(K3, GPIO.LOW)

    rotate_motor(STEPZ)
    sleep(.5)
    rotate_motor(STEPZ, ccw=True)

    print("Cycle Complete")
    cleanup()

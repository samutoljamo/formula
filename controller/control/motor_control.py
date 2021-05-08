import os
if os.getenv("DEBUG") != "1":
    import RPi.GPIO as GPIO
from .constants import LEFT, RIGHT, STRAIGHT

class DCMotor:
    def __init__(self, pwm_pin, in_pin, in2_pin, pwm_freq=100):
        self.pwm_pin = pwm_pin
        self.in_pin = in_pin
        self.in2_pin = in2_pin
        GPIO.setup((self.pwm_pin, self.in_pin, self.in2_pin), GPIO.OUT, initial=GPIO.LOW)
        self.pwm = GPIO.PWM(self.pwm_pin, pwm_freq)

    def start(self, power=100, forward=True):
        self.pwm.start(power)
        if forward:
            GPIO.output(self.in_pin, GPIO.HIGH)
            GPIO.output(self.in2_pin, GPIO.LOW)
        else:
            GPIO.output(self.in_pin, GPIO.LOW)
            GPIO.output(self.in2_pin, GPIO.HIGH)
    def control(self, power=100, forward=True):
        self.pwm.ChangeDutyCycle(power)
        if forward:
            GPIO.output(self.in_pin, GPIO.HIGH)
            GPIO.output(self.in2_pin, GPIO.LOW)
        else:
            GPIO.output(self.in_pin, GPIO.LOW)
            GPIO.output(self.in2_pin, GPIO.HIGH)
    def stop(self):
        GPIO.output((self.in_pin, self.in2_pin), GPIO.LOW)
        self.pwm.stop()

class SteeringMotor(DCMotor):
    def start(self):
        super().start(power=0)
    def turn(self, dir):
        if dir==STRAIGHT:
            self.straight()
        elif dir==LEFT:
            self.left()
        elif dir==RIGHT:
            self.right()
    def straight(self):
        self.control(power=0)
    def left(self):
        self.control(forward=True)
    def right(self):
        self.control(forward=False)


    

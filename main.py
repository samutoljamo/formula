import RPi.GPIO as GPIO
from controller.control import DCMotor, SteeringMotor
import time

GPIO.setmode(GPIO.BOARD)

EN_PWM_PIN = 32
EN_IN1_PIN = 11
EN_IN2_PIN = 12

ST_PWM_PIN = 33
ST_IN1_PIN = 15
ST_IN2_PIN = 16

engine = DCMotor(EN_PWM_PIN, EN_IN1_PIN, EN_IN2_PIN)
steering = SteeringMotor(ST_PWM_PIN, ST_IN1_PIN, ST_IN2_PIN)

engine.start(power=50)
steering.start()
time.sleep(2)
engine.control(power=0)
steering.right()
time.sleep(5)
steering.left()
engine.control(power=10, forward=False)
time.sleep(3)
steering.straight()
engine.control(power=0)
GPIO.cleanup()


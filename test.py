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

engine.start(0)
steering.start()
time.sleep(2)
inp = ""
while inp != "q":
    power = int(input("power: "))
    t = int(input("time: "))
    engine.control(power=power)
    time.sleep(t)
    engine.control(power=0)
GPIO.cleanup()

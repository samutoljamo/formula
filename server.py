import os
import RPi.GPIO as GPIO
import threading, time
from controller.control import DCMotor, SteeringMotor
from controller.network import Server, parse

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

_id = 0
def check(last_id):
    time.sleep(1)
    if _id == last_id:
        steering.straight()
        engine.control(0)
    

def handle(integer):
    global _id
    _id += 1
    if _id > 1000:
        _id = 0
    direction, forward, power = parse(integer)
    steering.turn(direction)
    engine.control(power, forward)
    t = threading.Thread(target=check, args=(_id,))
    t.start()

def on_connect(addr):
    print(f"connection from {addr}")

s = Server(handle_msg=handle, on_connect=on_connect)
try:
    s.run()
except KeyboardInterrupt:
    pass
GPIO.setmode(GPIO.BOARD)
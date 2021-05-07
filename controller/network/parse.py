from ..control import LEFT, RIGHT, STRAIGHT
def parse(integer):
    direction = 0
    forward = True
    if integer & 0b01000000 != 0:
        direction = STRAIGHT
    else:
        if integer & 0b10000000 != 0:
            direction = LEFT
        else:
            direction = RIGHT
    if integer & 0b00100000 == 0:
        forward = False
    power = (integer&0b00011111) * (100/31)
    return direction, forward, power


    

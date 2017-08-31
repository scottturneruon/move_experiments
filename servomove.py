from microbit import *

pin1.set_analog_period(20)
pin2.set_analog_period(20)

def forward(N):
    pin1.write_analog(180)
    pin2.write_analog(1)
    sleep(N)
    
def backward(N):
    pin1.write_analog(1)
    pin2.write_analog(180)
    sleep(N)

def turnLeft(N):
    pin1.write_analog(1)
    pin2.write_analog(1)
    sleep(N)

def turnRight(N):
    pin1.write_analog(180)
    pin2.write_analog(180)
    sleep(N)

while True:
    forward(1500)
    backward(1500)
    turnLeft(1500)
    turnRight(1500) 
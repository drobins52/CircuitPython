
import time
from adafruit_motor import servo
import board
import touchio
import pulseio

touch1 = touchio.TouchIn(board.A1)
touch2 = touchio.TouchIn(board.A2)
pwm = pulseio.PWMOut(board.A3, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)
my_servo.angle = 90
while True:
    if touch1.value and not touch2.value:
        if my_servo.angle<179:
            my_servo.angle += 1
            print("Right!")
    if touch2.value and not touch1.value:
        if my_servo.angle>1:
            my_servo.angle -= 1
            print("Left!")
    if touch2.value and touch1.value:
        my_servo.angle +=1
        time.sleep(0.01)
        my_servo.angle -=1
        print("SwipSwap!")





    time.sleep(0.01)
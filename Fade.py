import time #pylint: disable=import-error
import board #pylint: disable=import-error
import pulseio #pylint: disable=import-error

led = pulseio.PWMOut(board.D13, frequency=5000, duty_cycle=0)

while True:
    for i in range(100):
        # PWM LED up and down
        if i < 50:
            led.duty_cycle = int(i * 2 * 65535 / 100)  # Up
            time.sleep(0.3) # Adjusts the amount of time the LED stays at it's brightest
        else:
            led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
        time.sleep(10) # Adjusts the amount of time it takes the LED to get brighter
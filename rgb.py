import pulseion #this code uses pwm so you need the pulseio library
import time

class RGB:
    def __init__(self, r, g, b):
        self.pwm_r = pulseio.PWMOut(r, frequency=1000, duty_cycle=0)
        self.pwm_g = pulseio.PWMOut(g, frequency=1000, duty_cycle=0)
        self.pwm_b = pulseio.PWMOut(b, frequency=1000, duty_cycle=0)
    def red(self):
        self.pwm_r.duty_cycle = 0      #you set a pin to zero if you want it to turn on
        self.pwm_g.duty_cycle = 2**16-1#2**16-1 is how you make sure a pin is all the way off
        self.pwm_b.duty_cycle = 2**16-1
    def cyan(self): #we need a function for each of the colors
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 0
    def magenta(self):
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 0
    def green(self):
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 2**16-1
    def yellow(self):
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 2**16-1
    def blue(self):
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 0

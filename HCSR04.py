import time
import board
import neopixel
import adafruit_hcsr04 # We have to import adafruit_hcsr04 from our lib folder, so this does that everytime the code runs 

pixel_pin = board.NEOPIXEL 
num_pixels = 1
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D2, echo_pin=board.D3)


RED = (255, 0, 0)     # The 3 numbers are used to determine colors in the neopixel
PURPLE = (180, 0, 255)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
ROUGE = (255, 0, 127)
PINK = (255, 0, 255)
WHITE_WARM = (120, 100, 80)
WHITE_COOL = (80, 100, 120)

while True:
    try:
        distance = sonar.distance
        print((distance)) # This prints how far away the object is from the HCSR04 Sensor

        if distance > 0 and distance <= 5: # Sets up distance and what colors they should match/correspond with
            pixels.fill(ROUGE)
            pixels.show()
        elif distance >= 5 and distance<=10:
            pixels.fill(PURPLE) 
            pixels.show()
        elif distance > 10 and distance <= 20:
            pixels.fill(PINK)
            pixels.show()
        elif distance >= 20 and distance <=25:
            pixels.fill(WHITE_COOL)
            pixels.show()
        elif distance > 25 and distance <= 35:
            pixels.fill(WHITE_WARM)
            pixels.show()
    except RuntimeError:
        print("Retrying!")
        pass
        time.sleep(.2) # Off 

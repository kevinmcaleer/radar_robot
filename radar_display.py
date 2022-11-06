from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER
import gc
from math import sin, radians
gc.collect()
from time import sleep
from range_finder import RangeFinder
from machine import Pin
from servo import Servo
from motor import Motor

m1 = Motor((4, 5))
m1.enable()

# run the motor full speed in one direction for 2 seconds
m1.to_percent(100)

trigger_pin = 2
echo_pin = 3

s = Servo(0)
r = RangeFinder(trigger_pin=trigger_pin, echo_pin=echo_pin)

display = PicoGraphics(DISPLAY_PICO_EXPLORER, rotate=0)
WIDTH, HEIGHT = display.get_bounds()

REALLY_DARK_GREEN = {'red':0, 'green':64, 'blue':0}
DARK_GREEN = {'red':0, 'green':128, 'blue':0}
GREEN = {'red':0, 'green':255, 'blue':0}
LIGHT_GREEN = {'red':255, 'green':255, 'blue':255}
BLACK = {'red':0, 'green':0, 'blue':0}

def create_pen(display, color):
    return display.create_pen(color['red'], color['green'], color['blue'])

black = create_pen(display, BLACK)
green = create_pen(display, GREEN)
dark_green = create_pen(display, DARK_GREEN)
really_dark_green = create_pen(display, REALLY_DARK_GREEN)
light_green = create_pen(display, LIGHT_GREEN)

length = HEIGHT //2
middle = WIDTH // 2

angle = 0

def calc_vectors(angle, length):
    # Solve and AAS triangle
    # angle of c is
    #
    #  B        x1, y1
    #  |\        \ 
    #  | \        \
    # a|_ \c       \
    #  |_|_\        \
    # C  b  A       x2,y2
    
    A = angle
    C = 90
    B = (180 - C) - angle
    c = length
    a = int((c * sin(radians(A))) / sin(radians(C))) # a/sin A = c/sin C
    b = int((c * sin(radians(B))) / sin(radians(C)))  # b/sin B = c/sin C
    x1 = middle - b
    y1 = (HEIGHT -1) - a
    x2 = middle
    y2 = HEIGHT -1
    
#     print(f'a:{a}, b:{b}, c:{c}, A:{A}, B:{B}, C:{C}, angle: {angle}, length {length}, x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}')
    return x1, y1, x2, y2
    
a = 1
while True:
    
#     print(f'x1:{x1}, y1:{y1}, x2:{x2}, y2:{y2}')
    s.value(a)
    distance = r.distance
    if a > 1:
        x1, y1, x2, y2 = calc_vectors(a-1, 100)
        display.set_pen(really_dark_green)
        
        display.line(x1, y1, x2, y2)
    
    if a > 2:
        x1, y1, x2, y2 = calc_vectors(a-2, 100)
        display.set_pen(dark_green)
        display.line(x1, y1, x2, y2)
    
#     if a > 3:
#         x1, y1, x2, y2 = calc_vectors(a-3, 100)
#         display.set_pen(black)
#         display.line(x1, y1, x2, y2)
       
    # Draw the full length
    x1, y1, x2, y2 = calc_vectors(a, 100)    
    display.set_pen(light_green)
    display.line(x1, y1, x2, y2)
    
    # Draw lenth as a % of full scan range (1200mm)
    scan_length = int(distance * 3)
    if scan_length > 100: scan_length = 100
    print(f'Scan length is {scan_length}, distance is: {distance}')
    x1, y1, x2, y2 = calc_vectors(a, scan_length)    
    display.set_pen(green)
    display.line(x1, y1, x2, y2)
    
    display.update()

    a += 1
    if a > 180:
        a = 1
        display.set_pen(black)
        display.clear()
        display.update()

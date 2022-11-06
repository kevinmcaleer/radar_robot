from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER
import gc
from math import sin, radians
gc.collect()
from time import sleep

display = PicoGraphics(DISPLAY_PICO_EXPLORER, rotate=0)
WIDTH, HEIGHT = display.get_bounds()

GREEN = {'red':0, 'green':255, 'blue':0}
BLACK = {'red':0, 'green':0, 'blue':0}

black = display.create_pen(BLACK['red'], BLACK['green'], BLACK['blue'])
green = display.create_pen(GREEN['red'], GREEN['green'], GREEN['blue'])

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
    
    print(f'a:{a}, b:{b}, c:{c}, A:{A}, B:{B}, C:{C}, angle: {angle}, length {length}, x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}')
    return x1, y1, x2, y2
    
a = 1
while True:
    x1, y1, x2, y2 = calc_vectors(a, 100)
#     print(f'x1:{x1}, y1:{y1}, x2:{x2}, y2:{y2}')
    display.set_pen(green)
    display.line(x1, y1, x2, y2)
    display.update()
    a += 1
    if a > 180:
        a = 1
        display.set_pen(black)
        display.clear()
        display.update()
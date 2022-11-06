# radar.py
# Kevin McAleer
# Nov 2022


from servo import Servo
from time import sleep
from range_finder import RangeFinder

from machine import Pin

trigger_pin = 2
echo_pin = 3

s = Servo(0)
r = RangeFinder(trigger_pin=trigger_pin, echo_pin=echo_pin)

def sweep(s,r):
    """ Returns a list of readings from a 180 degree sweep """
    
    readings = []
    
    for i in range(-90,90):
        s.value(i)
        sleep(0.01)
        readings.append(r.distance)
    return readings


while True or not keyboard_interrupt:
    
    print(sweep(s,r))
    sleep(0.25)
    
#     s.to_min()
#     print(f'distance is: {r.distance}, {s}')
#     sleep(0.5)
#     
#     s.to_mid()
#     print(f'distance is: {r.distance}, {s}')
#     sleep(0.5)
#     
#     s.to_max()
#     print(f'distance is: {r.distance}, {s}')
#     sleep(0.5)
    
 
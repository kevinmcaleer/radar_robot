# radar.py
# Kevin McAleer
# Nov 2022


from servo import Servo
from time import sleep
from range_finder import RangeFinder

from machine import Pin

trigger_pin = 2
echo_pin = 3

DATA_FILE = 'readings.csv'

s = Servo(0)
r = RangeFinder(trigger_pin=trigger_pin, echo_pin=echo_pin)

def take_readings(count):
    readings = []
    with open(DATA_FILE, 'ab') as file:
        for i in range(0, 90):
            s.value(i)
            value = r.distance
#             readings.append(value)
            print(f'distance: {value}, angle {i} degrees, count {count}')
            sleep(0.01)
        for i in range(90,-90, -1):
            s.value(i)
            value = r.distance
            readings.append(value)
            print(f'distance: {value}, angle {i} degrees, count {count}')
            sleep(0.01)
        for item in readings:
            file.write(f'{item}, ')
        file.write(f'{count} \n')
    
    print('wrote datafile')
    for i in range(-90,0,1):
        s.value(i)
        value = r.distance
        print(f'distance: {value}, angle {i} degrees, count {count}')
        sleep(0.05)

def demo():
    for i in range(-90, 90):
        s.value(i)
        print(f's: {s.value()}')
        sleep(0.01)
    for i in range(90,-90, -1):
        s.value(i)
        print(f's: {s.value()}')
        sleep(0.01)

def sweep(s,r):
    """ Returns a list of readings from a 180 degree sweep """
    
    readings = []
    
    for i in range(-90,90):
        s.value(i)
        sleep(0.01)
        readings.append(r.distance)
    return readings



for count in range(1,2):
    take_readings(count)
    sleep(0.25)
    
#     print(sweep(s,r))
#     sleep(0.25)
    
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
    
 
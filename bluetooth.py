import serial
import time 
from main import *

class Bluetooth():

    COM = None
    baudrate = None
    ser = None
    delay = None

    def __init__(self, COM, baudrate, delay):

        self.COM = COM
        self.baudrate = baudrate

        if not BT_DEBUG:
            self.ser = serial.Serial(port=COM, baudrate=baudrate)

        self.delay = delay 

    def send(self, line):
        value = bytearray(line, "utf-8")
        if BT_DEBUG:
            print(line)

        else:
            self.ser.write(value)

        time.sleep(self.delay)
        
    
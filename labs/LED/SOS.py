import pycom
import time

def long_t(color):
    pycom.rgbled(color) # red
    time.sleep(3)
    pycom.rgbled(0) # off
    time.sleep(1)

def short_t(color):
    pycom.rgbled(color) # red
    time.sleep(1)
    pycom.rgbled(0) # off
    time.sleep(1)

colors = [0x7f0000,0x007f00]

for cols in colors: # stop after 10 cycles
    for i in range(3):
        long_t(cols)
    for i in range(3):
        short_t(cols)
    for i in range(3):
        long_tcols()

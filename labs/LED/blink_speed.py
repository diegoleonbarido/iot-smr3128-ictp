import pycom
import time
timing=0.005
for i in range(1000):
    pycom.rgbled(0x7f0000) # red
    time.sleep(timing)
    pycom.rgbled(0) # off
    time.sleep(timing)

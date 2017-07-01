# test accelerometer (LIS2HH12)
# www.st.com/resource/en/datasheet/lis2hh12.pdfanslations/en.DM00096789.pdf
# based on this example
# # https://docs.pycom.io/pycom_esp32/pycom_esp32/tutorial/includes/pysense-examples.html#pysense-examples
#
from pysense import Pysense
from LIS2HH12 import LIS2HH12
import pycom
import micropython
import machine
import time

py = Pysense()
acc = LIS2HH12(py)
while True:
    if(acc.roll() > -80 and acc.roll() < -50):
        pycom.rgbled(0x007f00) # green
    else:
        pycom.rgbled(0x7f0000) # green
    time.sleep(1)

from machine import Pin
import time
import time

# Pin: P14 for Pysense board
# Pin: G17 for Extension board

pin_pressed_count = 0
is_pressed = False
pycom.heartbeat(False)

file_path = '/flash/log'
name = '/log.csv'

def handler(pin):
    global is_pressed
    global pin_pressed_count
    value = pin.value()
    #time_pressed_list = []
    #pressed_count_list = []
    pycom.rgbled(0)
    if not value and not is_pressed:
        time_pressed = time.localtime()
        #print(time_pressed,pin_pressed_count)
        pin_pressed_count += 1
        with open(file_path + name, 'r') as f:
            f.write(''.join(['{:02d}'.format(i) for i in time.localtime()][:6]) + "," + str(pin_pressed_count) +"\n")
        is_pressed = True

        if pin_pressed_count == 10:
            pycom.rgbled(0x007f00) # green
            print(time_pressed_list)
            print(pressed_count_list)

    elif value and is_pressed:
        is_pressed = False

        with open(file_path + name, 'r') as f:
            print(f.readall())
        #time_pressed_list.append(time_pressed)
        #pressed_count_list.append(pin_pressed_count)

        #line = ','.join([str(i) for i in time_pressed])
        #f = open('log/times_and_counts.csv','a')
        #f.write(line + "\n")
        #f.close()

    else:
        pass

btn = Pin("G17", mode=Pin.IN, pull=Pin.PULL_UP)
btn.callback(Pin.IRQ_FALLING | Pin.IRQ_RISING, handler)

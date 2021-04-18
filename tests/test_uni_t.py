from context import uni_t
import time
import timeit

dmm = uni_t.DMMMonitor('volts', interface='usb1')

dmm.start()

while True:
    print(str(dmm.value) + ' ' + dmm.units)
    time.sleep(1)
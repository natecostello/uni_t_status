from context import uni_t
import time
import timeit

# prior to running the test, ensure all usb devices are unplugged,
# then only plug in the DMM usb connector.

print("prior to runing the test, ensure all usb devices \
    are unplugged, then only plug in the DMM usb connector.")

dmm = uni_t.DMMMonitor('volts', '/dev/ttyUSB0')

dmm.start()

while not dmm.isValid:
    time.sleep(0.1)
    
while True:
    print(str(dmm.value) + ' ' + dmm.units)
    time.sleep(1)
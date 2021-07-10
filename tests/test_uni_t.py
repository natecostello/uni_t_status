from context import uni_t
import time
import timeit

# prior to running the test, ensure all usb devices are unplugged,
# then only plug in the DMM usb connector.

print("prior to runing the test, ensure all usb devices \
    are unplugged, then only plug in the DMM usb connector.")

dmm = uni_t.DMMMonitor('/dev/ttyUSB0')
dmm.parametername = 'test_param_name'

dmm.start()

# Commenting out to make sure it handles and rides through
# while not dmm.isValid:
#     time.sleep(0.1)

print("Take 10 samples, one per second")
count = 0
while count < 10:
    param = dmm.parameters[0]
    measurement = dmm.allmeasurements[param]
    print(param + ' : ' + measurement)
    count += 1
    time.sleep(1)

dmm.stop()

print("Test complete")
    
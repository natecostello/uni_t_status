import subprocess
import os
from threading import Thread
import time

sigrok_cmd = 'sigrok-cli --driver=uni-t-ut61e-ser:conn=/dev/ttyUSB0 --samples 1'

class DMMMonitor:
    
    def __init__(self, units, interface='usb0'):
        self.usbInterface = interface.upper()
        self.sigrok_dir = os.popen('which sigrok-cli').readline()[:-1]
        self.sigrok_cmd = f'sigrok-cli --driver=uni-t-ut61e-ser:conn=/dev/tty{self.usbInterface} --continuous'
        self.units = units
        self.value = 0
        self.output = ''

    def dmm_rx_task(self):
        while True:
            output = subprocess.run(sigrok_cmd, shell=True,
                                    check=True, capture_output=True, text=True)
            value_string = output.stdout
            self.value = float(value_string.split(' ')[1])

    def start(self):
        rx = Thread(target = self.dmm_rx_task)
        rx.daemon = True
        rx.start()
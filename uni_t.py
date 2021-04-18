import subprocess
import os
from threading import Thread
import time

class DMMMonitor:
    
    def __init__(self, units, interface='usb1'):
        self.usbInterface = interface.upper()
        self.sigrok_dir = os.popen('which sigrok-cli').readline()[:-1]
        self.sigrok_cmd = f'sigrok-cli --driver=uni-t-ut61e-ser:conn=/dev/tty{self.usbInterface} --samples 1'
        self.units = units
        self.value = 0
        self.output = ''

    def dmm_rx_task(self):
        while True:
            output = subprocess.run(self.sigrok_cmd, shell=True,
                                    check=True, capture_output=True, text=True)
            value_string = output.stdout
            self.value = round(float(value_string.split(' ')[1]),3)

    def start(self):
        rx = Thread(target = self.dmm_rx_task)
        rx.daemon = True
        rx.start()
from threading import Thread
import instrument_logger
from ut61e import UT61E
import time

class DMMMonitor(instrument_logger.Instrument):
    
    def __init__(self, port: str = None, dmm: UT61E = None) -> None:
        """port is a string of the form '/dev/ttyUSBx'"""
        if (dmm is not None):
            self._dmm = dmm
        elif (port is not None):
            self._dmm = UT61E(port)
        else:
            raise ValueError('Either a port or UT61E instance must be provided')
        
        self._parameterunits = ''
        self._parametername = ''
        self._parametervalue = '' # type is str

        self._started = False
        self._isValid = False

    @property
    def name(self) -> str:
        """Required by Instrument"""
        return 'ut61e'

    @property
    def allmeasurements(self) -> 'dict':
        """Required by Instrument"""
        all_meas = {}
        for param in self.parameters:
            all_meas[param] = self.getmeasurement(param)
        return all_meas

    @property
    def parameters(self) -> 'list[str]':
        """Required by Instrument"""
        return [
            self.name + '.' + self._parametername + '.' + self._parameterunits
        ]

    def getmeasurement(self, name: str) -> str:
        """Required by Instrument"""
        return self._parametervalue

    # @property
    # def units(self) -> str:
    #     return self._parameterunits

    # @units.setter
    # def units(self, u: str) -> None:
    #     self._parameterunits = u
    
    @property
    def parametername(self) -> 'str':
        return self._parametername
    
    @parametername.setter
    def parametername(self, p: str) -> None:
        self._parametername = p
    
    @property
    def isValid(self) -> 'str':
        return self._isValid

    def dmm_poller(self):
        while self._started:
            data = self._dmm.get_meas()
            if data['ovl']:
                self._parametervalue = 'OVL'
            else:
                self._parametervalue = str(data['norm_val'])

            self._parameterunits = data['norm_units']
            self._isValid = True
            time.sleep(0.4)
            

    def start(self):
        self._started = True
        rx = Thread(target = self.dmm_poller)
        rx.daemon = True
        rx.start()

    def stop(self):
        self._started = False

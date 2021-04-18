# uni_t

This is a package to collect data from a UNI-T UT61E DMM using sigrok.



This is an expirement in packaging following [this guide](https://packaging.python.org/tutorials/packaging-projects/), as modified by [this guide](https://docs.python-guide.org/writing/structure/).

### Getting Started

Note, this code requires sigrok and a UNI-T 61E DMM.  Some details can be found [here](https://github.com/natecostello/van_two_point_oh/blob/master/blog/2021-3-31/RPi-to-UNI-T-UT61E-Comms.md).

```
%python3 -m pip install git+https://github.com/natecostello/rec_bms_status.git
```
```
%python3
>>>from recq.binary import BinaryMonitor
>>> b = BinaryMonitor()
>>> b.chargeEnable
1
>>> b.sysPlus
0
>>> b.contactor
1

>>> from recq.canbus import CanBusMonitor
>>> import os
>>> os.system("sudo /sbin/ip link set can0 up type can bitrate 250000")
0
>>> c = CanBusMonitor()
>>> c.start()
>>> c.charge_current_limit
70.0
>>> c.alarmBits
'10101000 10100000 10000010 00000000'
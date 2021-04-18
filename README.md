# uni_t

This is a package to collect data from a UNI-T UT61E DMM using sigrok.



This is an expirement in packaging following [this guide](https://packaging.python.org/tutorials/packaging-projects/), as modified by [this guide](https://docs.python-guide.org/writing/structure/), and some help from section 2.2 of the [setup script documentation](https://docs.python.org/3/distutils/setupscript.html).

### Getting Started

Note, this code requires sigrok and a UNI-T 61E DMM.  Some details can be found [here](https://github.com/natecostello/van_two_point_oh/blob/master/blog/2021-3-31/RPi-to-UNI-T-UT61E-Comms.md).

```
%python3 -m pip install git+https://github.com/natecostello/uni_t_status.git
```
```
%python3
>>> import uni_t
>>> dmm = uni_t.DMMMonitor('volts', interface='usb0')
>>> dmm.start()
>>> dmm.value
3.242
>>> dmm.value
3.242
>>> dmm.value
3.242
>>> 
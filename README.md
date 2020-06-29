# corys-shitty-robot
Physical aimbot for Counter Strike :Global Offensive

## How to load arduino
An arduino to be used with this project needs to be flashed only once, after that every time the arduino receives power it will run that same code.

1. Install the arduino IDE on the raspberry pi
<pre><code> sudo apt-get install arduino </pre></code>

2. Detect which port the arduino is on, if you are unsure which is the arduino, run this command with and without it plugged in to the pi, and whatever one shows up when you plug it in, that's it. It should be either USBn or ACMn.
<pre><code> ls /dev/tty* </pre></code>

3. Compile and upload the .ino file, replacing USB0 here with the port detected in the previous step
<pre><code> arduino --verify --upload --board arduino:avr:nano:atmega328P --port /dev/tty/USB0 ./arduinoKBM/arduinoKBM.ino</pre></code>

*Note: --board argument should correspond with the board you are using (nano, mega, etc.). For more information visit https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc#options

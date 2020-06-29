# corys-shitty-robot
Physical aimbot for Counter Strike :Global Offensive


## How to load arduino
An arduino to be used with this project needs to be flashed only once, after that every time the arduino receives power it will run that same code.

1. Install the arduino IDE on the raspberry pi
<pre><code> sudo apt-get install arduino </pre></code>
2. Compile and upload the .ino file

<pre><code> sudo arduino --verify --upload --board arduino:avr:nano:atmega328P --port /dev/tty/USB0 ./arduinoKBM/arduinoKBM.ino</pre></code>

*Note: --board argument should correspond with the board you are using (nano, mega, etc.). For more information visit https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc#options

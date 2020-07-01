# corys-shitti-robot
Physical aimbot for Counter Strike :Global Offensive

## Raspbery Pi setup
Install necessary packages
<pre><code>sudo apt-get update
</pre></code>

Enable i2c connections on the pi in the config:
<pre><code> sudo raspi-config </pre></code>

Install this repo
<pre><code>
git clone https://github.com/thayes46/corys-shitty-robot.git
</pre></code>

Turn on the virtual environment for python
<pre><code>
source corys-shitty-robot/venv/bin/activate
</pre></code>

## How to load Arduino micro for Keyboard and Mouse simulation
An arduino to be used with this project needs to be flashed only once, after that every time the arduino receives power it will run that same code.

*Note: arduino used as a KBM must have the ATmega32u4 chip for native USB support

1. Install the arduino IDE on the raspberry pi
<pre><code> sudo apt-get install arduino </pre></code>

2. Detect which port the arduino is on, if you are unsure which is the arduino, run this command with and without it plugged in to the pi, and whatever one shows up when you plug it in, that's it. It should be either USBn or ACMn.
<pre><code> ls /dev/tty* </pre></code>

3. Compile and upload the .ino file, replacing USB0 here with the port detected in the previous step
<pre><code> arduino --verify --upload --board arduino:avr:micro:atmega32u4 --port /dev/tty/USB0 ./arduinoKBM/arduinoKBM.ino</pre></code>

*Note: --board argument should correspond with the board you are using (leonardo, micro, etc.). For more information visit https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc#options

If you receive an error along the lines of "permission denied: /dev/tty/USBn or /dev/tty/ACMn" run 
<pre><code> sudo adduser [your_username] dialout </pre></code>

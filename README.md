# corys-shitti-robot
Physical aimbot for [Osu!](https://osu.ppy.sh/home). Eventually to be used for FPS games such as [Valorant](https://playvalorant.com/en-us/).
This bot does not interact with the game's files at all, and instead uses only a visual input, currently a screengrab, to detect targets and click them in time

Void EULA of any title at your own risk

## Raspbery Pi setup
Enable I2C connections on the Pi in the config:
```
sudo raspi-config
```

Install this repo:
```
git clone https://github.com/thayes46/corys-shitty-robot.git
```

Install all dependent packages:
```
python3 -m pip install -r requirements.txt
```

## How to Load Arduino Micro for Keyboard and Mouse Simulation
An Arduino to be used with this project needs to be flashed only once, after that every time the Arduino receives power it will run that same code.

*Note: Arduino used as a KBM must have the ATMega32u4 chip for native USB support

1. Install the arduino IDE on the Raspberry Pi:
```
sudo apt-get install arduino
```

2. Detect which port the Arduino is on, if you are unsure which is the Arduino, run this command with and without it plugged in to the Pi, and whatever one shows up when you plug it in, that's it. It should be either `USBn` or `ACMn`.
```
ls /dev/tty*
```

3. Compile and upload the .ino file, replacing USB0 here with the port detected in the previous step
```
arduino --verify --upload --board arduino:avr:micro:atmega32u4 --port /dev/tty/USB0 ./arduinoKBM/arduinoKBM.ino
```

*Note: `--board` argument should correspond with the board you are using (Leonardo, Micro, etc.). For more information visit [here](https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc#options)

If you receive an error along the lines of `permission denied: /dev/tty/USBn or /dev/tty/ACMn` run
```
sudo adduser [your_username] dialout
```

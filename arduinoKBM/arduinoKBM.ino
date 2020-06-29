/*
 * Arduino KBM for corys-shitty-robot
 */
#include <Keyboard.h>
#include <Mouse.h>
#include <Wire.h>
#define SLAVE_ADDRESS 0x04

void setup() {
  //Communication set up to prepare inputs and outputs
  Wire.begin(SLAVE_ADDRESS);
  Keyboard.begin();
  Mouse.begin();
  Wire.onReceive(receiveEvent);
}

void loop() { 
  delay(100); //NOTE: remove/decrease this if notable lag, increase if overheating
}

/**
 * Handler for events received on I2C for events
 */
void receiveEvent(int numEvents) {
  //loop through all available events
  while (0 < Wire.available()) {
    char c = Wire.read();
    switch (c) {
      case 'w' :
        Keyboard.release('s');
        Keyboard.press('w');
        break;
      case 's' :
        Keyboard.release('w');
        Keyboard.press('s');
        break;
      case 'a' :
        Keyboard.release('d');
        Keyboard.press('a');
        break;
      case 'd' :
        Keyboard.release('a');
        Keyboard.press('d');
        break;
      case 'i' :
        Keyboard.release('w');
        break;
      case 'k' :
        Keyboard.release('s');
        break;
      case 'j' :
        Keyboard.release('a');
        break;
      case 'l' :
        Keyboard.release('d');
        break;
      case 'r' :
        Keyboard.write('r');
        break;
      case 'e' :
        Keyboard.write('e');
        break;
      case 'b' :
        Mouse.click();
        break;
      case 'n' :
        Mouse.press();
        break;
      case 'm' :
        Mouse.release();
        break;
      case 'v' :
        Keyboard.write(' ');
        break;
      case 'g' :  
        signed byte amountX = Wire.read();
        signed byte amountY = Wire.read();
        Mouse.move(amountX, amountY, 0);
        break;
      case 'h' :
        signed byte amountScroll = Wire.read();
        Mouse.move(0, 0, amountScroll);
        break;
      default:
        break;
    }
  }
}

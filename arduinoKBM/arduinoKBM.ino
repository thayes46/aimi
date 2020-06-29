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
  
}

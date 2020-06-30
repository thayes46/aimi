import smbus
import time

bus = smbus.SMBus(1)

#address for KBM is 0x04
addressKBM = 0x04
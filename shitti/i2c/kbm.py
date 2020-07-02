import smbus

bus = smbus.SMBus(1)

# address for KBM is 0x04

addressKBM = 0x04


def sendchar(value):
    try:
        if value[2] == '':
            bus.write_byte(addressKBM, value)
            return -1
    except TypeError:   # catch when sending mouse values
        if 127 >= value >= -128:
            bus.write_byte(addressKBM, value)
            return -1
    return 0

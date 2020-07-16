import smbus

bus = smbus.SMBus(1)

# address for KBM is 0x04

addressKBM = 0x04


def dragRel(x, y, duration):
    print("hey you didn't implement this")
    # TODO: make this a thing


# function to send a byte over the i2c bus
# returns 1 if success, 0 if failed
def sendchar(value):
    try:
        if value[2] == '':  # ensure there is only 1 character
            bus.write_byte(addressKBM, value)
            return 1
    except TypeError:  # catch when sending mouse values
        if 127 >= value >= -128:
            bus.write_byte(addressKBM, value)
            return 1
    return 0

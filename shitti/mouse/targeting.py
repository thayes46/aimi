# uncomment kbm when deploying on a device using the i2c bus
# uncomment pyautogui when running on same device as application
# TODO: replace pyautogui with pynput

# from ..i2c import kbm as mouse
import pyautogui as mouse


def clicktarget(targetx, targety):
    if not mouse.onScreen(targetx, targety):
        print("target out of bounds")
        return 0
    mouse.moveTo(targetx, targety, duration=.005)
    mouse.click()
    return 1

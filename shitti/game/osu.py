# script for the basics of playing osu
from ..processing import circles
import mss
import numpy as np
import cv2 as cv


def run():
    monitor = {'top': 0, 'left': 0, 'width': 600, 'height': 600}
    sct = mss.mss()
    image = sct.grab(monitor)
    image = np.array(image)
    image = np.flip(image[:, :, :3], 2)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    print('before call')
    ret = circles.houghcircle(image)
    for ind in ret:
        print(ind)

# script for the basics of playing osu
import mss
from skimage import io

from ..processing.circles import *


def run():
    """
    monitor = {'top': 0, 'left': 0, 'width': 600, 'height': 600}
    while 1:
        image = mss.mss().grab(monitor)
        houghcircle("images/circles.jpg", True, True)
    """
    ret = findcircle("images/Circles.mp4", 50, 0, 100)
    for ind in ret:
        print(ind)

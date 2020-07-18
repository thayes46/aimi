from .circleprocessing import houghcircle
import time
import mss
from numpy import flip, array
from cv2 import cvtColor, COLOR_RGB2BGR


def detectcircles(monitor):
    screen = mss.mss()
    # get time for framerate math
    last_time = time.time()

    # get current frame from area of screen
    currentframe = screen.grab(monitor)

    # need to convert to numpy array
    # progressframe used for when the frame isn't being seen as image
    progressframe = array(currentframe)

    # print fps (after every screen grab, not after processing
    print("fps: {}".format(1 / (time.time() - last_time)))

    # flipping shit bc dimensions are weird
    progressframe = flip(progressframe[:, :, :3], 2)
    progressframe = cvtColor(progressframe, COLOR_RGB2BGR)

    try:
        # get an array of all the circles in the frame
        discoveredcircles = houghcircle(progressframe)
        return [discoveredcircles, progressframe]
    except TypeError:
        pass

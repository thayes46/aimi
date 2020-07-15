from .circleprocessing import houghcircle
import time
import mss
from numpy import flip, array
from cv2 import cvtColor


def detectcircles(monitor):
    screen = mss.mss()
    # get time for framerate math
    last_time = time.time()

    # get current frame from area of screen
    currentframe = screen.grab(monitor)

    # need to convert to numpy array
    # progressframe used for when the frame isn't being seen as image
    progressframe = numpy.array(currentframe)

    # print fps (after every screen grab, not after frameprocessing
    print("fps: {}".format(1 / (time.time() - last_time)))

    # flipping shit bc dimensions are weird
    progressframe = numpy.flip(progressframe[:, :, :3], 2)
    progressframe = cv2.cvtColor(progressframe, cv2.COLOR_RGB2BGR)

    try:
        # get an array of all the circles in the frame
        discoveredcircles = circleprocessing.houghcircle(progressframe)
        return [discoveredcircles, progressframe]
    except TypeError:
        pass

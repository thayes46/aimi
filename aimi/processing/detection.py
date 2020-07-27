from .circleprocessing import hough_circle
import time
import mss
from numpy import flip, array
from cv2 import cvtColor, COLOR_RGB2BGR


def detect_circles(monitor):
    screen = mss.mss()
    # get time for framerate math
    last_time = time.time()

    # get current frame from area of screen
    current_frame = screen.grab(monitor)

    # need to convert to numpy array
    # progress_frame used for when the frame isn't being seen as image
    progress_frame = array(current_frame)

    # print fps (after every screen grab, not after processing
    print("fps: {}".format(1 / (time.time() - last_time)))

    # flipping shit bc dimensions are weird
    progress_frame = flip(progress_frame[:, :, :3], 2)
    progress_frame = cvtColor(progress_frame, COLOR_RGB2BGR)

    try:
        # get an array of all the circles in the frame
        discovered_circles = hough_circle(progress_frame)
        return [discovered_circles, progress_frame]
    except TypeError:
        pass

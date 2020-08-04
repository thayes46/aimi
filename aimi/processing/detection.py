from .circleprocessing import hough_circle
import time
import mss
from numpy import flip, array
import cv2 as cv


def detect_circles(monitor, init = False):
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
    progress_frame = cv.cvtColor(progress_frame, cv.COLOR_RGB2HSV)

    # limits of "red". Pure red is 0,255,255
    lower_red = array([0,150,150])
    upper_red = array([10,255,255])

    # mask creation and application
    mask = cv.inRange(progress_frame, lower_red, upper_red)

    # if init is False, invert mask
    if init == False:
        mask = cv.bitwise_not(mask,mask)

    # filter frame, either only show red or show everything but red    
    progress_frame = cv.bitwise_and(progress_frame, progress_frame, mask=mask)

    # change colorspace for use in hough_circle
    progress_frame = cv.cvtColor(progress_Frame, cv.COLOR_HSV2RGB)

    try:
        # get an array of all the circles in the frame
        discovered_circles = hough_circle(progress_frame)
        return [discovered_circles, progress_frame]
    except TypeError:
        pass

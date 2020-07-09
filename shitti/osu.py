# script for the basics of playing osu
from shitti.processing.circles import houghcircle
import mss
import time
import numpy
import cv2 as cv


# ideally in deployment mss is replaced with capture card reads

def run():
    with mss.mss() as sct:
        # set the area to watch to be the primary monitor
        # this can be changed to be a select area of pixels for testing
        # a window playing a video
        monitor = sct.monitors[1]

        while "Screen capturing":
            # save timestamp for fps count
            last_time = time.time()

            image = numpy.array(sct.grab(monitor))
            # show the found circles
            houghcircle(image, False)
            # print fps in the console
            print("fps: {}".format(1 / (time.time() - last_time)))
            if cv.waitkey(0):
                cv.destroyAllWindows()
                break

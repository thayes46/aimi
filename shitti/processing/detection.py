from . import circleprocessing
import time
import mss
import numpy
import cv2


def detectcircles(monitor, showcircles):
    screen = mss.mss()
    while 1:
        # get time for framerate math
        last_time = time.time()

        # get current frame from area of screen
        currentframe = screen.grab(monitor)

        # need to convert to numpy array
        # progressframe used for when the frame isn't being seen as image
        progressframe = numpy.array(currentframe)

        # print fps (after every screen grab, not after processing
        print("fps: {}".format(1 / (time.time() - last_time)))

        # flipping shit bc dimensions are weird
        progressframe = numpy.flip(progressframe[:, :, :3], 2)
        progressframe = cv2.cvtColor(progressframe, cv2.COLOR_RGB2BGR)

        try:
            # get an array of all the circles in the frame
            discoveredcircles = circleprocessing.houghcircle(progressframe)
            for circle in discoveredcircles:
                print(circle)
            if (showcircles):
                processedframe = circleprocessing.drawcircles(discoveredcircles,
                                                              progressframe)
                cv2.imshow("Circles detected", processedframe)
        except TypeError:
            pass
        # show where the circles are

        # listen for ESC to yeet (hopefully)
        escapekey = cv2.waitKey(25) & 0xFF
        if escapekey == 27:
            cv2.destroyAllWindows()
            break

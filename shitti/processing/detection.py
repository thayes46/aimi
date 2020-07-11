from . import circles
import time
import mss
import numpy as np
import cv2 as cv


def getcircle(monitor):
    sct = mss.mss()
    while 1:
        # get time for framerate math
        last_time = time.time()

        # get current frame from area of screen
        image = sct.grab(monitor)

        # need to convert to numpy array
        image = np.array(image)

        # print fps (after every screen grab, not after processing
        print("fps: {}".format(1 / (time.time() - last_time)))

        # flipping shit bc dimensions are weird
        image = np.flip(image[:, :, :3], 2)
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

        # get an array of all the circles in the frame
        ret = circles.houghcircle(image)
        for ind in ret:
            print(ind[1])
        final = circles.drawcircles(ret, image)
        # show where the circles are
        cv.imshow("Circle bois", final)

        # listen for ESC to yeet (hopefully)
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            cv.destroyAllWindows()
            break

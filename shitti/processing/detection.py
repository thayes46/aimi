from . import circles
import time
import mss
import numpy as np
import cv2 as cv


def getcircle(monitor):
    sct = mss.mss()
    while 1:
        last_time = time.time()
        image = sct.grab(monitor)
        image = np.array(image)
        print("fps: {}".format(1 / (time.time() - last_time)))
        image = np.flip(image[:, :, :3], 2)
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        ret = circles.houghcircle(image)
        for ind in ret:
            print(ind)
        cv.imshow("Circle bois", image)
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            cv.destroyAllWindows()
            break

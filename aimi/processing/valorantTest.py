import cv2 as cv
import numpy as np
import mss
import time

# Set range of screen to be recorded
with mss.mss() as sct:
    video = {"top": 200, "left": 850, "width": 1050, "height": 525}

    while True:
        # Initialize some shit
        last_time = time.time()
        bot = ()
        top = ()

        # Convert screenshot into a numpy array and convert to HSV
        img = np.array(sct.grab(video))
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        # Set limits for detected pixels in HSV
        lower_red = np.array([0, 75, 75])
        upper_red = np.array([3, 255, 255])

        # Create mask of pixels within color range, bitwise and with image
        mask = cv.inRange(hsv, lower_red, upper_red)
        res = cv.bitwise_and(img, img, mask=mask)

        # # Find first pixel in mask that is not 0
        # rows,cols = mask.shape
        # for i in range(rows-1, 0, -1):
        #     for j in range(cols):
        #         if mask[i, j] != 0:
        #             bot = (j, i)
        #             break
        #     else:
        #         continue
        #         break
        #
        # # Find last pixel in image that is not 0
        # for i in range(rows):
        #     for j in range(cols):
        #         if mask[i, j] != 0 :
        #             top = (j, i)
        #             break
        #     else:
        #         continue
        #         break
        #
        # # Make sure that bottom and top were detected
        # if bot != () and top != ():
        #     # Set y-value of "head"
        #     ind = int(bot[1]/8 + 7*top[1]/8)
        #
        #     # Put dot on "head" based
        #     cv.circle(img, (top[0], ind), 1, (0, 255, 0), 2)

        # Show frame
        # cv.imshow('mask', mask)
        # cv.imshow('vid', img)
        cv.imshow('res', res)

        # Print 1/time taken to complete loop (fps)
        print("fps: {}".format(1/(time.time()-last_time)))

        # Break loop and close windows when esc is pressed
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            cv.destroyAllWindows()
            break

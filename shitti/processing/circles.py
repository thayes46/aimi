import time

import cv2 as cv
import numpy as np


def findcircle(source, mindist, minrad, maxrad):
    # start capturing video. 0 is onboard webcam, will need to change that for
    # Capture Card
    print(source, mindist, minrad, maxrad)
    cap = cv.VideoCapture(source)
    if not cap.isOpened():
        print("error opening video feed")
        return 0
    while 1:
        # read frame
        _, frame = cap.read()
        size = frame.shape
        bwframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        circles = cv.HoughCircles(bwframe, cv.HOUGH_GRADIENT, 1, mindist,
                                  param1=50, param2=30, minRadius=minrad,
                                  maxRadius=maxrad)
        try:
            circles = np.uint16(np.around(circles))
            # yield circles[0]
        except TypeError:
            continue
        # The following is all for displaying a visual of where the circles are

        # iterate through list of circles. Make green circle around
        # circumference and small red dot at center
        try:
            for i in circles[0, :]:
                # make sure that circle is inside the frame
                # can probably remove for Osu! but need for webcam
                print(i)
                if i[0] in range(size[1]) and i[1] in range(size[0]):
                    cv.circle(frame, (i[0], i[1]), i[2], (0, 0, 255), 2)
                    cv.circle(frame, (i[0], i[1]), 2, (0, 255, 255), 3)

                    # this should be getting the bgr values at the center of
                    # each circle

                    b = frame.item(int(i[1]), int(i[0]), 0)
                    g = frame.item(int(i[1]), int(i[0]), 1)
                    r = frame.item(int(i[1]), int(i[0]), 2)

                    # return x-center, y-center, radius, r value, g value, and
                    # b value and continue running function
                    # i[0] = x, i[1] = y, i[2] = radius
                    yield [i, r, g, b]

                    # print centerpoint, radius, and color to console
                    print('Center: (%d,%d)' % (i[0], i[1]))
                    print('Radius: %d' % i[2])
                    print('Color (RGB): (%d,%d,%d)' % (r, g, b))
        except TypeError:
            continue
        # show each frame
        cv.imshow("Circle bois", frame)
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            cap.release()
            cv.destroyAllWindows()
            break
    return 1

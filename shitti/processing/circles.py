import cv2 as cv
import numpy as np


# finding circles given video feed
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
        bwframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        circles = cv.HoughCircles(bwframe, cv.HOUGH_GRADIENT, 1, mindist,
                                  param1=50, param2=30, minRadius=minrad,
                                  maxRadius=maxrad)
        try:
            circles = np.uint16(np.around(circles))
            yield drawcircles(circles, frame)
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


# finding circles for a still image
def houghcircle(image):
    # turn to black and white for hough circles
    bwimg = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    bwimg = cv.medianBlur(bwimg, 5)
    circles = cv.HoughCircles(bwimg, cv.HOUGH_GRADIENT, 1, 50, param1=50,
                              param2=30,
                              minRadius=7, maxRadius=90)
    try:
        return np.uint16(np.around(circles))
    except TypeError:
        # it gets angry if there aren't any circles
        print('ruh ro, no circles here')


# helper function to check for bounds and draw the circles
def drawcircles(circles, image):
    size = image.shape
    for i in circles[0, :]:
        # make sure that circle is inside the frame
        # can probably remove for Osu! but need for webcam
        if i[0] in range(size[1]) and i[1] in range(size[0]):
            cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)

            b = image.item(int(i[1]), int(i[0]), 0)
            g = image.item(int(i[1]), int(i[0]), 1)
            r = image.item(int(i[1]), int(i[0]), 2)

            cv.circle(image, (i[0], i[1]), 2, (0, 255, 255), 3)
    return image

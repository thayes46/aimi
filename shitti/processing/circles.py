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


def houghcircle(image):
    img = image
    size = img.shape
    bwimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    bwimg = cv.medianBlur(bwimg, 5)
    circles = cv.HoughCircles(bwimg, cv.HOUGH_GRADIENT, 1, 1, param1=50,
                              param2=30,
                              minRadius=3, maxRadius=90)
    try:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # make sure that circle is inside the frame
            # can probably remove for Osu! but need for webcam
            print(i)
            if i[0] in range(size[1]) and i[1] in range(size[0]):
                cv.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 2)
                cv.circle(img, (i[0], i[1]), 2, (0, 255, 255), 3)

                b = img.item(int(i[1]), int(i[0]), 0)
                g = img.item(int(i[1]), int(i[0]), 1)
                r = img.item(int(i[1]), int(i[0]), 2)
                yield [i, r, g, b]

    except TypeError:
        print('ruh ro')

    print('yeet yeet motherfucker bitch')

# reads the image, if it should wait for a keypress before moving on, and if it
# should print all found circle data to the console
def houghcircleBITCH(image, wait, printData):
    # read in image and convert to grayscale
    img = image
    size = image.shape
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.medianBlur(img, 5)

    # find circles using Hough Transform. Radius and separation values found
    # through trial and error
    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 1, param1=50,
                              param2=30,
                              minRadius=3, maxRadius=200)
    try:
        circles = np.uint16(np.around(circles))
        # yield circles[0]
    except TypeError:
        print('ruh ro')
    # iterate though list of circles and put a green circle around them and
    # a red dot at the center
    try:
        for i in circles[0, :]:
            # make sure that circle is inside the frame
            # can probably remove for Osu! but need for webcam
            print(i)
            if i[0] in range(size[1]) and i[1] in range(size[0]):
                cv.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 2)
                cv.circle(img, (i[0], i[1]), 2, (0, 255, 255), 3)

                # this should be getting the bgr values at the center of
                # each circle

                b = img.item(int(i[1]), int(i[0]), 0)
                g = img.item(int(i[1]), int(i[0]), 1)
                r = img.item(int(i[1]), int(i[0]), 2)

                # return x-center, y-center, radius, r value, g value, and
                # b value and continue running function
                # i[0] = x, i[1] = y, i[2] = radius
                yield [i, r, g, b]

                # print centerpoint, radius, and color to console
                print('Center: (%d,%d)' % (i[0], i[1]))
                print('Radius: %d' % i[2])
                print('Color (RGB): (%d,%d,%d)' % (r, g, b))
    except TypeError:
        pass
    if wait:
        # show image until any key is pressed
        cv.imshow('detected circles', img)
        k = cv.waitKey(5) & 0xFF
        while k != 27:
            continue
        cv.destroyAllWindows()
    else:
        cv.imshow('detected circles', img)

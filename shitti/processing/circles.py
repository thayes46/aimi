import cv2 as cv
import numpy as np

def findcircle(source, mindist, minrad, maxrad):
    # start capturing video. 0 is onboard webcam, will need to change that for
    # Capture Card
    print(source, mindist, minrad, maxrad)
    cap = cv.VideoCapture(0)
    while 1:
        # read frame
        _, frame = cap.read()
        size = frame.shape
        print(size)
        bwframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        circles = cv.HoughCircles(bwframe, cv.HOUGH_GRADIENT, 1, mindist,
                                  param1=50, param2=30, minRadius=minrad,
                                  maxRadius=maxrad)
        circles = np.uint16(np.around(circles))
        print(circles)
        break

    return 1

# define function Find Circle
# inputs: video source, minimum distance between circles, minimum circle
# radius, and maximum circle radius
# outputs: center of circle, radius of circle, rgb color of circle
def findcircle2(source, mindist, minrad, maxrad):
    # start capturing video. 0 is onboard webcam, will need to change that for
    # Capture Card

    print('Inside findcircle function')
    cap = cv.VideoCapture(source)

    while 1:
        # read frame
        _, frame = cap.read()

        # find size of frame
        size = frame.shape

        # convert frame to grayscale
        bwframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # find circles using Hough Transformation. min and max radius will need
        # to be set when we have good values
        circles = cv.HoughCircles(bwframe, cv.HOUGH_GRADIENT, 1, mindist,
                                  param1=50, param2=30, minRadius=minrad,
                                  maxRadius=maxrad)

        # not sure why this round is necessary honestly
        circles = np.uint16(np.around(circles))

        # iterate through list of circles. Make green circle around
        # circumference and small red dot at center
        for i in circles[0, :]:
            # make sure that circle is inside the frame
            # can probably remove for Osu! but need for webcam
            if i[0] in range(size[0]) and i[1] in range(size[1]):
                cv.circle(frame, (i[0], i[1]), i[2], (0, 0, 255), 2)
                cv.circle(frame, (i[0], i[1]), 2, (0, 255, 255), 3)

                # this should be getting the bgr values at the center of
                # each circle
                b = frame.item(int(i[0]), int(i[1]), 0)
                g = frame.item(int(i[0]), int(i[1]), 1)
                r = frame.item(int(i[0]), int(i[1]), 2)

                # return x-center, y-center, radius, r value, g value, and
                # b value and continue running function
                # i[0] = x, i[1] = y, i[2] = radius
                yield [i, r, g, b]

                """# print centerpoint, radius, and color to console
                print('Center: (%d,%d)' % (i[0],i[1]))
                print('Radius: %d' % i[2])
                print('Color (RGB): (%d,%d,%d)' % (r,g,b))"""

        # show each frame and break loop when esc key pressed
        cv.imshow('Feed', frame)
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            break

    # turn off camera and close window
    cap.release()
    cv.destroyAllWindows()


# reads the image, if it should wait for a keypress before moving on, and if it
# should print all found circle data to the console
def houghcircle(image, wait, printData):
    # read in image "circles.jpg" and convert to grayscale
    img = cv.imread(image)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.medianBlur(img, 5)

    # find circles using Hough Transform. Radius and separation values found
    # through trial and error
    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 200, param1=50,
                              param2=30,
                              minRadius=100, maxRadius=200)
    circles = np.uint16(np.around(circles))

    # iterate though list of circles and put a green circle around them and
    # a red dot at the center
    for i in circles[0, :]:
        cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

        # colors being weird
        b = img[int(i[0]), int(i[1]), 0]
        g = img[int(i[0]), int(i[1]), 1]
        r = img[int(i[0]), int(i[1]), 2]

        if printData:
            # print shit
            print('Center: (%d,%d)' % (i[0], i[1]))
            print('Radius: %d' % i[2])
            print('Color (RGB): (%d,%d,%d)' % (r, g, b))

    if wait:
        # show image until any key is pressed
        cv.imshow('detected circles', img)
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        cv.imshow('detected circles', img)


#print('after all function definitions')
# Examples for circles
# call of findCircle
# ret = findcircle(0, 500, 0, 50)

# prints ind for each iteration of the function
# ind[0][0] = x, ind[0][1] = y, ind[0][2] = radius, ind[1] = r, ind[2] = g,
# ind[3] = b
# for ind in ret:
#     print(ind[1])

# call of houghcircle on test image
# houghcircle('../../images/circles.jpg')

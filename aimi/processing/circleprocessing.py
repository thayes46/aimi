import cv2
import numpy


# finding circles for a still image
def hough_circle(image):
    # turn to black and white for hough circles
    grey_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    grey_image = cv2.medianBlur(grey_image, 5)
    circles = cv2.HoughCircles(grey_image, cv2.HOUGH_GRADIENT, 1, 50,
                               param1=50,
                               param2=30,
                               minRadius=7, maxRadius=90)
    try:
        return numpy.uint16(numpy.around(circles))
    except TypeError:
        # it gets angry if there aren't any circles
        pass


# helper function to check for bounds and draw the circles
def draw_circles(circles, image):
    size = image.shape
    try:
        circles_dims = numpy.array(circles)
        circles_dims = circles_dims.shape
        if circles_dims[1] is None:
            for circle in circles[0, :]:
                # make sure that circle is inside the frame
                # can probably remove for Osu! but need for webcam
                if circle[0] in range(size[1]) and circle[1] in range(size[0]):
                    cv2.circle(image, (circle[0], circle[1]),
                               circle[2], (0, 0, 255), 2)
                    cv2.circle(image, (circle[0], circle[1]),
                               2, (0, 255, 255), 3)
    except IndexError:
        if circles[0] in range(size[1]) and circles[1] in range(size[0]):
            cv2.circle(image, (circles[0], circles[1]),
                       circles[2], (0, 0, 255), 2)
            cv2.circle(image, (circles[0], circles[1]),
                       2, (0, 255, 255), 3)

    return image


# useful for grabbing color values later
# for i in circles[0, :]:
# b = image.item(int(i[1]), int(i[0]), 0)
# g = image.item(int(i[1]), int(i[0]), 1)
# r = image.item(int(i[1]), int(i[0]), 2)

# finding circles given video feed
# NOT IN USE, until using camera
"""
def findcircle(source, mindist, minrad, maxrad):
    # start capturing video. 0 is onboard webcam, will need to change that for
    # Capture Card
    print(source, mindist, minrad, maxrad)
    videofeed = cv2.VideoCapture(source)
    if not videofeed.isOpened():
        print("error opening video feed")
        return 0
    while 1:
        # read frame
        _, currentframe = videofeed.read()
        bwframe = cv2.cvtColor(currentframe, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(bwframe, cv2.HOUGH_GRADIENT, 1, mindist,
                                   param1=50, param2=0.9, minRadius=minrad,
                                   maxRadius=maxrad)
        try:
            circles = numpy.uint16(numpy.around(circles))
            yield draw_circles(circles, currentframe)
        except TypeError:
            continue
        # show each frame
        cv2.imshow("Circle bois", currentframe)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            videofeed.release()
            cv2.destroyAllWindows()
            break
    return 1
"""

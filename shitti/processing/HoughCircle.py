import numpy as np
import cv2 as cv

# read in image "circles.jpg" and convert to grayscale
cimg = cv.imread("circles.jpg")
img = cv.cvtColor(cimg, cv.COLOR_BGR2GRAY)
img = cv.medianBlur(img, 5)

# find circles using Hough Transform. Radius and separation values found
# through trial and error
circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 200, param1=50, param2=30,
                          minRadius=100, maxRadius=200)
circles = np.uint16(np.around(circles))

# iterate though list of circles and put a green circle around them and a red
# dot at the center
for i in circles[0, :]:
    cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

    # colors being weird
    b = cimg[int(i[0]), int(i[1]), 0]
    g = cimg[int(i[0]), int(i[1]), 1]
    r = cimg[int(i[0]), int(i[1]), 2]

    # print shit
    print('Center: (%d,%d)' % (i[0], i[1]))
    print('Radius: %d' % i[2])
    print('Color (RGB): (%d,%d,%d)' % (r, g, b))

# show image until any key is pressed
cv.imshow('detected circles', cimg)
cv.waitKey(0)
cv.destroyAllWindows()

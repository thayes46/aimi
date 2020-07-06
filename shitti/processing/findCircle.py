import cv2 as cv
import numpy as np

# start capturing video. 0 is onboard webcam, will need to change that for Cap Card
cap = cv.VideoCapture(0)


while(1):
    # read frame
    _,frame = cap.read()

    # convert frame to grayscale
    bwframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    # find circles using Hough Transformation. min and max radius will need to be set when we have good values
    circles = cv.HoughCircles(bwframe,cv.HOUGH_GRADIENT,1,500,param1=50,param2=30,minRadius=0,maxRadius=50)

    # not sure why this round is necessary honestly
    circles = np.uint16(np.around(circles))

    # iterate through list of circles. Make green circle around circumference and small red dot at center
    for i in circles[0,:]:
        cv.circle(frame,(i[0],i[1]),i[2],(0,0,255),2)
        cv.circle(frame,(i[0],i[1]),2,(0,255,255),3)

        # this should be getting the bgr values at the center of each circle
        b = frame.item(int(i[0]),int(i[1]),0)
        g = frame.item(int(i[0]),int(i[1]),1)
        r = frame.item(int(i[0]),int(i[1]),2)

        # print centerpoint, radius, and color to console
        print('Center: (%d,%d)' % (i[0],i[1]))
        print('Radius: %d' % i[2])
        print('Color (RGB): (%d,%d,%d)' % (r,g,b))

    # show each frame and break loop when esc key pressed
    cv.imshow('Feed',frame)
    k=cv.waitKey(5) & 0xFF
    if k==27:
        break

# turn off camera and close window
cap.release()
cv.destroyAllWindows()

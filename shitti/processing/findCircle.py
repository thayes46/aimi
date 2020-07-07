import cv2 as cv
import numpy as np

# define function Find Circle
# inputs: video source, minimum distance between circles, minimum circle radius, maximum circle radius
# outputs: center of circle, radius of circle, rgb color of circle
def FindCircle(source,minDist,minRad,maxRad):
    # start capturing video. 0 is onboard webcam, will need to change that for Cap Card
    cap = cv.VideoCapture(source)


    while(1):
        # read frame
        _,frame = cap.read()

        # find size of frame
        size = frame.shape

        # convert frame to grayscale
        bwframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

        # find circles using Hough Transformation. min and max radius will need to be set when we have good values
        circles = cv.HoughCircles(bwframe,cv.HOUGH_GRADIENT,1,minDist,param1=50,param2=30,minRadius=minRad,maxRadius=maxRad)

        # not sure why this round is necessary honestly
        circles = np.uint16(np.around(circles))

        # iterate through list of circles. Make green circle around circumference and small red dot at center
        for i in circles[0,:]:
            # make sure that circle is inside the frame
            # can probably remove for Osu! but need for webcam
            if i[0] in range(size[0]) and i[1] in range(size[1]):
                cv.circle(frame,(i[0],i[1]),i[2],(0,0,255),2)
                cv.circle(frame,(i[0],i[1]),2,(0,255,255),3)

                # this should be getting the bgr values at the center of each circle
                b = frame.item(int(i[0]),int(i[1]),0)
                g = frame.item(int(i[0]),int(i[1]),1)
                r = frame.item(int(i[0]),int(i[1]),2)

                # return x-center, y-center, radius, r value, g value, and b value and continue running function
                # i[0] = x, i[1] = y, i[2] = radius
                yield [i,r,g,b]

                """# print centerpoint, radius, and color to console
                print('Center: (%d,%d)' % (i[0],i[1]))
                print('Radius: %d' % i[2])
                print('Color (RGB): (%d,%d,%d)' % (r,g,b))"""

        # show each frame and break loop when esc key pressed
        cv.imshow('Feed',frame)
        k=cv.waitKey(5) & 0xFF
        if k==27:
            break

    # turn off camera and close window
    cap.release()
    cv.destroyAllWindows()

# function call
ret = FindCircle(0,500,0,50)

# prints ind for each iteration of the function
# ind[0][0] = x, ind[0][1] = y, ind[0][2] = radius, ind[1] = r, ind[2] = g, ind[3] = b
for ind in ret:
    print(ind[1])

import cv2 as cv
import numpy as np

# Read in image
img = cv.imread('enemy.png')

# Initialize shit
bot = ()
top = ()

# Convert image to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Set range of "red"
lower_red = np.array([0, 75, 75])
upper_red = np.array([3, 255, 255])

# Create mask of pixels within red range and bitwise and with image
mask = cv.inRange(hsv, lower_red, upper_red)
res = cv.bitwise_and(img, img, mask=mask)

# Find first pixel in mask that is not 0
rows, cols = mask.shape
for i in range(rows-1, 0, -1):
    for j in range(cols):
        if mask[i, j] != 0:
            bot = (j, i)
            break
    else:
        continue
    break

# Find last pixel in mask that is not 0
for i in range(rows):
    for j in range(cols):
        if mask[i, j] != 0:
            top = (j, i)
            break
    else:
        continue
    break

# Make sure that pixels were found to avoid errors
if bot != () and top != ():
    # Set y-value to be 1/8 distance between top and bottom
    ind = int(bot[1]/8+7*top[1]/8)

    # Place dot at "head"
    cv.circle(img, (top[0], ind), 1, (0, 255, 0), 2)

# Display images
# cv.imshow('mask', mask)
cv.imshow('img', img)
cv.imshow('res', res)

# Close windows when any key pressed
k = cv.waitKey(0)
cv.destroyAllWindows()

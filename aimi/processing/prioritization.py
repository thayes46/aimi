from numpy import array
from cv2 import inRange, cvtColor, COLOR_RGB2HSV

# sorts list of circles based on radius
def sort_targets(targets):
    targets[targets[:,2].argsort()]
    return targets

# checks if there is white on the screen indicating a slider
# to be called after initial click
def check_slider(frame):
    # convert frame from RGB to HSV
    frame = cvtColor(frame, COLOR_RGB2HSV)

    # define limits for "white"
    lower_white = array([0, 0, 200])
    upper_white = array([255, 255, 255])

    # create mask of all white pixels
    mask = inRange(frame, lower_white, upper_white)

    # if any values of mask are 1, there is white on the screen
    # this indicates a slider and returns true
    if mask.any():
        return True
    else:
        return False

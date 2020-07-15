from ..frameprocessing import detection
from ..mouse import targeting
from ..frameprocessing.circleprocessing import drawcircles
import cv2

def run():
    # define area of screen to watch for circles
    monitor = {'top': 0, 'left': 550, 'width': 500, 'height': 500}
    # Variable to control whether a window is shown or not
    showcircles = True
    # do the vision thing
    while 1:
        detectionresults = detection.detectcircles(monitor)
        circles = detectionresults[0]
        if showcircles:
            try:
                progressframe = detectionresults[1]
                displayframe = drawcircles(circles, progressframe)
                cv2.imshow("Circles detected", displayframe)
            except TypeError:
                pass
        # tell the mouse to go to the biggest circle
        # TODO: implement targeting.py

        # cv window is kil
        escapekey = cv2.waitKey(25) & 0xFF
        if escapekey == 27:
            cv2.destroyAllWindows()

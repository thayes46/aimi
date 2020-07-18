from ..frameprocessing import detection
from ..mouse import targeting
from ..frameprocessing.circleprocessing import drawcircles
from pynput import keyboard
import cv2

break_program = False
monitor = {'top': 60, 'left': 60, 'width': 1000, 'height': 800}


def run():
    global monitor
    running = True
    # Variable to control whether a window is shown or not
    showcircles = True

    print("You are about to let this program take control of your mouse.\n"
          "It will click in this region:")
    print(monitor)
    print("If everything is prepared type \"ok\". "
          "Type anything else to quit")
    typedinput = input()
    if typedinput == "ok":
        print("Ok. Starting. Press ESCAPE at any time to stop")
    else:
        print("Exiting")
        return 0
    global break_program
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        print("listening for inputs")
        while running:
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
            # TODO: determine which circle to click
            try:
                if circles.size > 0:
                    for eachcircle in circles[0]:
                        print("clicking circle:")
                        print(eachcircle)
                        targeting.clicktarget(eachcircle[0], eachcircle[1])
            except AttributeError:
                pass
            # cv window is kil
            escapekey = cv2.waitKey(25) & 0xFF
            if escapekey == 27:
                cv2.destroyAllWindows()
                running = False
            listener.join()


# Can't quite tell how to abstract this to an API call yet.
# TODO: Abstract the below

def on_press(key):
    print('{0} pressed'.format(
        key))


def on_release(key):
    global break_program
    if key == keyboard.Key.esc:
        break_program = True
        return False

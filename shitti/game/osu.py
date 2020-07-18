from ..processing import detection
from ..mouse import targeting
from ..processing.circleprocessing import drawcircles
from pynput import keyboard
import cv2

break_program = False
monitor = {'top': 60, 'left': 0, 'width': 1819, 'height': 979}


def run():
    global monitor
    global break_program

    running = True
    # Variable to control whether a window is shown or not
    showcircles = False

    # Probably shouldn't just let this thing run buck wild
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

    # listen to all keyboard inputs so that esc at any point past here will
    # stop it, call it a failsafe if you want
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        # Main game loop
        lastcircle = None
        while running and not break_program:
            detectionresults = detection.detectcircles(monitor)
            circles = detectionresults[0]
            if showcircles:
                try:
                    progressframe = detectionresults[1]
                    displayframe = drawcircles(circles, progressframe)
                    cv2.imshow("Circles detected", displayframe)
                except TypeError:
                    pass

            # TODO: Add bool to circles to see if they are a color that means
            # TODO: that they are to be dragged until they are no longer there

            # TODO: then have the below code either click or click and drag

            # TODO: make the below all go into clickcircles

            try:
                if circles.size > 0:
                    for eachcircle in circles[0]:
                        print("Comparing for duplicates")
                        if (lastcircle is None) or not \
                                (eachcircle == lastcircle).any():
                            print(f"clicking circle at {eachcircle[0]}"
                                  f", {eachcircle[1]}")
                            targeting.clicktarget(eachcircle[0], eachcircle[1])
                            if lastcircle is None:
                                lastcircle = eachcircle
                            else:
                                lastcircle = eachcircle.copy()
                        else:
                            print(f"already clicked circle at "
                                  f"{eachcircle[0]}, {eachcircle[1]}")
                            pass
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

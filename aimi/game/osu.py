from pynput import keyboard
from ..processing import detection, prioritization
from ..mouse import targeting
from ..processing.circleprocessing import draw_circles
from ..keyboard.listener import break_program, on_press, on_release
import cv2

# left: 1920 is for testing and forcing to scan display without any noi se

monitor = {'top': 0, 'left': 0, 'width': 1000, 'height': 1000}


def run():
    global monitor
    running = True
    # Variable to control whether a window is shown or not
    show_window = False

    # Probably shouldn't just let this thing run buck wild
    print("You are about to let this program take control of your mouse.\n"
          "It will click in this region:")
    print(monitor)
    print("If everything is prepared type \"ok\". "
          "Type anything else to quit")
    typed_input = input()
    if typed_input == "ok":
        print("Ok. Starting. Press ESCAPE at any time to stop")
    else:
        print("Exiting")
        return 0

    # listen to all keyboard inputs so that esc at any point past here will
    # stop it, call it a failsafe if you want
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listening:

        # Main loop
        last_target = None
        # frame_count = 0 # Don't remember what this was for...
        while running and not break_program:
            detection_results = detection.detect_circles(monitor)
            # try will succeed
            try:
                # circle array is 0th element
                targets = detection_results[0]

                # show the window with tracing if you want, not recommended
                if show_window:
                    # frame is 1st element
                    progress_frame = detection_results[1]
                    display_frame = draw_circles(targets, progress_frame)
                    cv2.imshow("Circles detected", display_frame)

                # prioritize targets and click em
                # sorted_targets = prioritization.sort_targets(targets)
                sorted_targets = targets
                print(f"previous last target is {last_target}")
                last_target = targeting.click_circles(sorted_targets,
                                                      last_target, detection_results[1])
                print(f"new last target is {last_target}")
            except TypeError as e:
                # Will only fall here when there are no circles at all
                print(f"Hit typeError in main loop: {e}")
                pass

            # cv window is kil
            escape_key = cv2.waitKey(25) & 0xFF
            if escape_key == 27:
                cv2.destroyAllWindows()
                running = False

        # idk why it has to be at this level, doesn't make sense but it works
        listening.join()

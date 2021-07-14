# uncomment kbm when deploying on a device using the i2c bus
# uncomment pynput when running on same device as application

# from ..i2c import kbm as mouse
from pynput.mouse import Button, Controller
# from ..processing.circleprocessing import draw_circles
import os

# import cv2

mouse = Controller()

# FIXME: make an environment variable
base_image_path = r"/home/todd/aimi/images/clicked"
os.chdir(base_image_path)
image_ID = 0


def click_target(targetx, targety):
    mouse.position = (targetx, targety)
    mouse.press(Button.left)
    mouse.release(Button.left)
    return 1


def click_circles(sorted_circles, last_circle, frame):
    # TODO: add support if each_circle[3] is true to hold the click
    global image_ID
    try:
        if sorted_circles.size > 0:
            for each_circle in sorted_circles:
                print("Circle at ", each_circle)
                if (last_circle is None) or not \
                        (each_circle[0] == last_circle[0] and
                         each_circle[1] == last_circle[1]):
                    print(f"clicking circle at {each_circle[0]}"
                          f", {each_circle[1]}")
                    click_target(each_circle[0], each_circle[1])


                    impath = "" + str(image_ID) + ".jpg"
                    print(f"Writing image {impath}")
                    image_ID = image_ID + 1

                    # circle = each_circle
                    # annotated_frame = draw_circles(circle, frame)
                    # cv2.imwrite(impath, annotated_frame)
                    if last_circle is None:
                        last_circle = each_circle
                    else:
                        last_circle = each_circle
                else:
                    print(f"already clicked circle at "
                          f"{each_circle[0]}, {each_circle[1]}")
            return last_circle
    except AttributeError:
        print("hit attribute error in mouse/targeting.clickcircles:")
        print(AttributeError.message())
        return last_circle
        pass

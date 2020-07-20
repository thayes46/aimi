# uncomment kbm when deploying on a device using the i2c bus
# uncomment pynput when running on same device as application

# from ..i2c import kbm as mouse
from pynput.mouse import Button, Controller

mouse = Controller()

def click_target(targetx, targety):
    # if not mouse.onScreen(targetx, targety):
    #     print("target out of bounds")
    #     return 0
    mouse.position = (targetx, targety)
    mouse.press(Button.left)
    mouse.release(Button.left)
    return 1


def click_circles(sorted_circles, last_circle):
    # TODO: add support if each_circle[3] is true to hold the click
    try:
        if sorted_circles.size > 0:
            for each_circle in sorted_circles[0]:
                print("Comparing for duplicates")
                if (last_circle is None) or not \
                        (each_circle == last_circle).any():
                    print(f"clicking circle at {each_circle[0]}"
                          f", {each_circle[1]}")
                    click_target(each_circle[0], each_circle[1])
                    if last_circle is None:
                        last_circle = each_circle
                    else:
                        last_circle = each_circle.copy()
                else:
                    print(f"already clicked circle at "
                          f"{each_circle[0]}, {each_circle[1]}")
            return last_circle
    except AttributeError:
        pass

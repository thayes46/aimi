from ..processing import detection


def run():
    # define area of screen to watch for circles
    monitor = {'top': 0, 'left': 1920, 'width': 1920, 'height': 1080}

    # do the vision thing
    detection.getcircle(monitor)
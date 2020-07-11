from ..processing import detection


def run():
    # define area of screen to watch for circles
    monitor = {'top': 0, 'left': 550, 'width': 500, 'height': 500}

    # do the vision thing
    detection.detectcircles(monitor, True)

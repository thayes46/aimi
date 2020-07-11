from ..processing import detection


def run():
    monitor = {'top': 0, 'left': 1920, 'width': 1920, 'height': 1080}
    detection.getcircle(monitor)

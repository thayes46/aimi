# script for the basics of playing osu
from ..processing.circles import *


def run():
    ret = findcircle("images/Circles.mp4", 50, 0, 100)
    for ind in ret:
        print(ind)

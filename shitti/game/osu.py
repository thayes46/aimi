# script for the basics of playing osu
from ..processing import circles


def run():

    print('before call')
    ret = circles.findcircle(0, 500, 0, 50)
    for ind in ret:
        print(ind[1])
    print('after call')

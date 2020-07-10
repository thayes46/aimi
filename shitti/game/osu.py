# script for the basics of playing osu
from ..processing import circles


# ideally in deployment mss is replaced with capture card reads

def run():
    print('before call')
    circles.findcircle("../../images/BasicallyOsu.gif", 30, 1, 50)
    print('after call')

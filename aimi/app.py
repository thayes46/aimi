# this is the main runner script for aimi, the physical aimbot

from .game import osu


def run(testing):
    osu.run(testing)

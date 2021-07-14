from aimi import app
import sys

if __name__ == '__main__':
    if sys.argv[-1] == "-t":
        app.run(True)
    else:
        app.run(False)

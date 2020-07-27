break_program = False


def on_press(key):
    print('{0} pressed'.format(
        key))


def on_release(key):
    global break_program
    if key == key.esc:
        break_program = True
        return False

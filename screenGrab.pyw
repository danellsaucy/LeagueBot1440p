from PIL import ImageGrab
import os
import time
# Globals
# --------------------
x_pos = 479
y_pos = 249

def screenGrab():
    box = (x_pos+1, y_pos+1, 1601+x_pos, 900+y_pos)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()
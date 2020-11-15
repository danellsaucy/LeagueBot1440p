import time
import win32api, win32con
import random

x_pos = 479
y_pos = 249
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("left Click.") #Debugging

def rightClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
    print("left Click.")  # Debugging

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print("left Down")

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print("left release")

def mousePos(cord):
    win32api.SetCursorPos((x_pos + cord[0], y_pos + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pos
    y = y - y_pos
    print(x,y)

startTime = time.time()
time.sleep(5)
mousePos((672, 857))
print("Done")

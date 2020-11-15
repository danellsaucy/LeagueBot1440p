from PIL import ImageGrab
import os
import time
import win32api, win32con
import random
from PIL import ImageOps

# Globals
# --------------------
x_pos = 479
y_pos = 249


class Cord:
    # accept button conditions
    accept_button = (830, 692)
    accept_button2 = (800, 385)
    accept_button3 = (802, 421)

    # loading screen
    loading_screen = (1536, 714)
    loading_screen2 = (119, 265)
    loading_screen3 = (123, 793)

    # in game conditions
    in_game_w_champ = (718, 30)
    in_game_w_champ2 = (933, 24)
    in_game_w_champ3 = (1199, 245)

    # game lost
    game_lost = (744, 473)
    game_lost1 = (985, 470)
    game_lost2 = (256, 812)

    # champion locations
    champ1 = (541, 884)
    champ2 = (708, 884)
    champ3 = (875, 884)
    champ4 = (1043, 884)
    champ5 = (1212, 884)

    blue_champ1 = (38, 102, 159)
    blue_champ2 = (30, 76, 121)

    purp_champ1 = (195, 11, 144)
    purp_champ2 = (145, 8, 107)

    gold_champ1 = (161, 96, 11)
    gold_champ2 = (218, 130, 17)

    # overall placement
    first = (0, 0)
    second = (293, 239)
    third = (0, 0)
    fourth = (0, 0)
    fifth = (0, 0)
    sixth = (0, 0)
    seventh = (0, 0)
    eigth = (0, 0)
    place_color = (204, 99, 68)

    # other buttons
    re_roll = (307, 872)
    buy_xp = (297, 813)
    surrender = (698, 419)
    play_again = (672, 857)
    cursor_middle = (796, 303)

    # mission screen
    mission_screen1 = (227, 335)
    mission_screen1_color = (11, 11, 47)
    mission_screen2 = (1310, 441)
    mission_screen2_color = (65, 19, 30)
    mission_screen3 = (1230, 382)
    mission_screen3_color = (65, 46, 32)
    mission_ok = (805, 763)


def screenGrab():
    box = (x_pos + 1, y_pos + 1, 1601 + x_pos, 900 + y_pos)
    im = ImageGrab.grab(box)
    ##im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    # print("left Click.") #Debugging


def randomLeftClick():
    for x in range(random.randint(5, 6), random.randint(10, 13)):
        leftClick()


def rightClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
    print("left Click.")  # Debugging


def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    print("left Down")


def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    print("left release")


def mousePos(cord):
    win32api.SetCursorPos((x_pos + cord[0], y_pos + cord[1]))


def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pos
    y = y - y_pos
    print(x, y)


def acceptGame():
    # accepts game
    queue = False;
    in_game = False;
    startTime = time.time()
    while not queue:
        s = screenGrab()
        if s.getpixel(Cord.loading_screen) == (115, 150, 66) or s.getpixel(Cord.loading_screen2) == (195, 78, 151) \
                or s.getpixel(Cord.loading_screen3) == (194, 198, 194):
            print("I think im in game")
            queue = True

        if s.getpixel(Cord.accept_button) == (30, 37, 42) or s.getpixel(Cord.accept_button2) == (12, 69, 90) \
                or s.getpixel(Cord.accept_button3) == (211, 176, 101):
            print("Accepting game")
            mousePos((830, 692))
            leftClick()
            time.sleep(4 - (time.time() - startTime) % 4)

        else:
            print("Waiting")
            time.sleep(4 - (time.time() - startTime) % 4)

        if s.getpixel(Cord.loading_screen) == (115, 150, 66) or s.getpixel(Cord.loading_screen2) == (195, 78, 151) \
                or s.getpixel(Cord.loading_screen3) == (194, 198, 194):
            print("I think im in game")
            queue = True

    startTime = time.time()
    while not in_game:
        s = screenGrab()
        if s.getpixel(Cord.in_game_w_champ) == (22, 48, 46) or s.getpixel(Cord.in_game_w_champ2) == (22, 43, 41) \
                or s.getpixel(Cord.in_game_w_champ3) == (80, 94, 59):
            print("I am in game right now")
            in_game = True

        else:
            print("Waiting for game to load")
            time.sleep(4 - (time.time() - startTime) % 4)

        time.sleep(4 - (time.time() - startTime) % 4)


def firstGame():
    # location of league play button
    mousePos((147, 54))
    leftClick()
    time.sleep(2)

    # location of TFT menu
    mousePos((1096, 285))
    leftClick()
    time.sleep(2)

    # select normal game mode
    mousePos((991, 643))
    leftClick()
    time.sleep(1)

    # click confirm
    mousePos((675, 857))
    leftClick()
    time.sleep(2)

    # finds game
    mousePos((675, 857))
    leftClick()
    time.sleep(1)


def whileGame():
    global_time = 1020
    # champion locations
    champ1 = (541, 884)
    champ2 = (708, 884)
    champ3 = (875, 884)
    champ4 = (1044, 884)
    champ5 = (1212, 884)
    champList = [champ1, champ2, champ3, champ4, champ5]

    startTime = time.time()
    time.sleep(1)
    while global_time - round((time.time() - startTime), 0) % global_time != 1:
        print(global_time - round((time.time() - startTime), 0) % global_time)
        time.sleep(1)
        if 29 - round((time.time() - startTime), 0) % 29 == 29:
            mousePos(Cord.cursor_middle)
            s = screenGrab()
            if s.getpixel(Cord.champ1) == Cord.gold_champ1 or s.getpixel(Cord.champ1) == Cord.gold_champ2:
                print("Gold champ spotted in spot 1!")
                mousePos(champ1)
                time.sleep(0.5)
                randomLeftClick()
                print("Gold champion has been bought!")
                mousePos(Cord.cursor_middle)

            elif s.getpixel(Cord.champ2) == Cord.gold_champ1 or s.getpixel(Cord.champ2) == Cord.gold_champ2:
                print("Gold champ spotted in spot 2!")
                mousePos(champ2)
                time.sleep(0.5)
                randomLeftClick()
                print("Gold champion has been bought!")
                mousePos(Cord.cursor_middle)

            elif s.getpixel(Cord.champ3) == Cord.gold_champ1 or s.getpixel(Cord.champ3) == Cord.gold_champ2:
                print("Gold champ spotted in spot 3!")
                mousePos(champ3)
                time.sleep(0.5)
                randomLeftClick()
                print("Gold champion has been bought!")
                mousePos(Cord.cursor_middle)

            elif s.getpixel(Cord.champ4) == Cord.gold_champ1 or s.getpixel(Cord.champ4) == Cord.gold_champ2:
                print("Gold champ spotted in spot 4!")
                mousePos(champ4)
                time.sleep(0.5)
                randomLeftClick()
                print("Gold champion has been bought!")
                mousePos(Cord.cursor_middle)

            elif s.getpixel(Cord.champ5) == Cord.gold_champ1 or s.getpixel(Cord.champ5) == Cord.gold_champ2:
                print("Gold champ spotted in spot 5!")
                mousePos(champ5)
                time.sleep(0.5)
                randomLeftClick()
                print("Gold champion has been bought!")
                mousePos(Cord.cursor_middle)

            elif s.getpixel(Cord.champ1) == Cord.purp_champ1 or s.getpixel(Cord.champ1) == Cord.purp_champ2:
                print("Purple champ spotted in spot 1!")
                mousePos(champ1)
                time.sleep(0.5)
                randomLeftClick()
                print("Purple champion has been bought!")
                mousePos(Cord.cursor_middle)

            elif s.getpixel(Cord.champ2) == Cord.purp_champ1 or s.getpixel(Cord.champ2) == Cord.purp_champ2:
                print("Purple champ spotted in spot 2!")
                mousePos(champ2)
                time.sleep(0.5)
                randomLeftClick()
                print("Purple champion has been bought!")
                mousePos(Cord.cursor_middle)

            elif s.getpixel(Cord.champ3) == Cord.purp_champ1 or s.getpixel(Cord.champ3) == Cord.purp_champ2:
                print("Purple champ spotted in spot 3!")
                mousePos(champ3)
                time.sleep(0.5)
                randomLeftClick()
                print("Purple champion has been bought!")
                mousePos(Cord.cursor_middle)

            elif s.getpixel(Cord.champ4) == Cord.purp_champ1 or s.getpixel(Cord.champ4) == Cord.purp_champ2:
                print("Purple champ spotted in spot 4!")
                mousePos(champ4)
                time.sleep(0.5)
                randomLeftClick()
                print("Purple champion has been bought!")
                mousePos(Cord.cursor_middle)

            elif s.getpixel(Cord.champ5) == Cord.purp_champ1 or s.getpixel(Cord.champ5) == Cord.purp_champ2:
                print("Purple champ spotted in spot 5!")
                mousePos(champ5)
                time.sleep(0.5)
                randomLeftClick()
                print("Purple champion has been bought!")
                mousePos(Cord.cursor_middle)

            elif s.getpixel(Cord.champ1) == Cord.blue_champ1 or s.getpixel(Cord.champ1) == Cord.blue_champ2:
                print("Blue champ spotted in spot 1!")
                mousePos(champ1)
                time.sleep(0.5)
                randomLeftClick()
                print("Blue champion has been bought!")
                mousePos(Cord.cursor_middle)

            elif s.getpixel(Cord.champ2) == Cord.blue_champ1 or s.getpixel(Cord.champ2) == Cord.blue_champ2:
                print("Blue champ spotted in spot 2!")
                mousePos(champ2)
                time.sleep(0.5)
                randomLeftClick()
                print("Blue champion has been bought!")
                mousePos(Cord.cursor_middle)

            elif s.getpixel(Cord.champ3) == Cord.blue_champ1 or s.getpixel(Cord.champ3) == Cord.blue_champ2:
                print("Blue champ spotted in spot 3!")
                mousePos(champ3)
                time.sleep(0.5)
                randomLeftClick()
                print("Blue champion has been bought!")
                mousePos(Cord.cursor_middle)

            elif s.getpixel(Cord.champ4) == Cord.blue_champ1 or s.getpixel(Cord.champ4) == Cord.blue_champ2:
                print("Blue champ spotted in spot 4!")
                mousePos(champ4)
                time.sleep(0.5)
                randomLeftClick()
                print("Blue champion has been bought!")
                mousePos(Cord.cursor_middle)

            elif s.getpixel(Cord.champ5) == Cord.blue_champ1 or s.getpixel(Cord.champ5) == Cord.blue_champ2:
                print("Blue champ spotted in spot 5!")
                mousePos(champ5)
                time.sleep(0.5)
                randomLeftClick()
                print("Blue champion has been bought!")
                mousePos(Cord.cursor_middle)

            else:
                print("No good champions found, skipping for now.")

        if 240 - round((time.time() - startTime), 0) % 240 == 240:
            if (global_time - round((time.time() - startTime), 0) % global_time) < 330:
                print("I am in buy xp loop")
                mousePos(Cord.buy_xp)
                randomLeftClick()
                time.sleep(0.1)
                print("Bought XP")
                randomLeftClick()
                time.sleep(0.1)
                print("Bought XP")
                randomLeftClick()
                time.sleep(0.1)
                print("Bought XP")
                randomLeftClick()
                time.sleep(0.1)
                print("Bought XP")
                randomLeftClick()
                time.sleep(0.1)
                print("Bought XP")
                randomLeftClick()
                time.sleep(0.1)
                print("Bought XP")
                randomLeftClick()
                time.sleep(0.1)
                print("Bought XP")
                randomLeftClick()
                time.sleep(0.1)
                print("Bought XP")
                randomLeftClick()
                time.sleep(0.1)
                print("Bought XP")
                randomLeftClick()
                time.sleep(0.1)
                print("Bought XP")
                mousePos(Cord.cursor_middle)
            elif (global_time - round((time.time() - startTime), 0) % global_time) < 500:
                print("I am in buy xp loop")
                mousePos(Cord.buy_xp)
                randomLeftClick()
                time.sleep(0.1)
                print("Bought XP")
                randomLeftClick()
                time.sleep(0.1)
                print("Bought XP")
                randomLeftClick()
                time.sleep(0.1)
                print("Bought XP")
                randomLeftClick()
                time.sleep(0.1)
                print("Bought XP")
                randomLeftClick()
                time.sleep(0.1)
                print("Bought XP")
                mousePos(Cord.cursor_middle)
            elif (global_time - round((time.time() - startTime), 0) % global_time) < 750:
                print("I am in buy xp loop")
                mousePos(Cord.buy_xp)
                randomLeftClick()
                time.sleep(0.1)
                print("Bought XP")
                randomLeftClick()
                time.sleep(0.1)
                print("Bought XP")
                randomLeftClick()
                time.sleep(0.1)
                print("Bought XP")
                mousePos(Cord.cursor_middle)


def surrenderGame():
    print("It is now time to FF!")
    win32api.keybd_event(0x0D, 0, 0, 0)
    time.sleep(1)
    win32api.keybd_event(0xBF, 0, 0, 0)
    time.sleep(1)
    win32api.keybd_event(0x46, 0, 0, 0)
    time.sleep(1)
    win32api.keybd_event(0x46, 0, 0, 0)
    time.sleep(1)
    win32api.keybd_event(0x0D, 0, 0, 0)
    time.sleep(1)
    mousePos(Cord.surrender)
    leftClick()
    print("I surrendered!")
    time.sleep(10)


def playAgain():
    mousePos(Cord.play_again)
    leftClick()
    time.sleep(2)

    # finds game
    mousePos((675, 857))
    leftClick()
    time.sleep(1)


def startGame():
    replayGame = True
    counter = 1
    firstGame()
    acceptGame()
    whileGame()
    surrenderGame()
    print("You played", counter, "games")
    while replayGame:
        playAgain()
        acceptGame()
        whileGame()
        surrenderGame()
        counter = counter + 1
        print("You played", counter, "games")


def main():
    startGame()
    #get_cords()
    #im = screenGrab()
    #print(im.getpixel((329, 180)))
    #print(im.getpixel((292, 180)))
    #print(im.getpixel((Cord.mission_screen3)))


if __name__ == '__main__':
    main()

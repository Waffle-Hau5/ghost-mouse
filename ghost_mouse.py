import pyautogui
import random
import time
import math


# Just some functions at the moment...


def sleeptime(pause):
    if pause >= 996:
        sleeper = random.uniform(10, 20)
        print(f"Script pause: [LARGE], sleeping {sleeper} seconds...")
        time.sleep(sleeper)
    if pause >= 700:
        sleeper = (random.uniform(0.1, 2))
        print(f"Script pause: [SMALL], sleeping {sleeper} seconds...")
        time.sleep(sleeper)


def move_mouse(image_file, confidence=None, click=None):
    start_x, start_y = pyautogui.position()
    location = pyautogui.locateOnScreen(image_file, confidence=confidence)
    if location is None:
        print("Image not found on screen.")
        return

    x, y, image_width, image_height = location

    # Randomly select a destination within provided image height and width.
    dest_x = x + random.uniform(0, image_width)
    dest_y = y + random.uniform(0, image_height)

    # quicc maths, cuz curves are nice..
    angle = math.atan2(dest_y - y, dest_x - x)
    x += math.cos(angle)
    y += math.sin(angle)
    movetime = random.uniform(0.2, 0.4)
    print(f"MoveTo duration: {movetime}")
    pyautogui.moveTo(dest_x, dest_y, duration=movetime)
    # mouse pauses for up to 3 times per movement.
    for i in range(3):
        pause = random.randint(1, 1000)
        sleeptime(pause)
    if click:
        pyautogui.doubleClick()
        return


move_mouse("images/click.png", 0.8, True)

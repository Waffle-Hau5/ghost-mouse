import pyautogui
import math
import random
import time


# Written in python 3.8, I intend on fleshing this out a bit, making this a bot to mine gold in a "time-sink" game.
# Main function for mouse's movement, may make different variations of movement to throw the "bot detection" off.

def move_mouse(image_file, click_at_location=None, grayscale=False, confidence=None):

    location = pyautogui.locateOnScreen(image_file, grayscale=grayscale, confidence=confidence)

    if not location:
        print("Your reference was not found.. Try decreasing confidence.")
    if location:
        # If the image_file is found, unpack the x and y coordinates of the top-left corner
        # and the width and height of the image...
        x, y, image_width, image_height = location

        # Instead of clicking on the corner of the image provided, it will randomly choose a location
        # within the image bounds, somewhat like a human would.

        x += random.uniform(0, image_width)
        y += random.uniform(0, image_height)

        # Gets the current position of the mouse...
        start_x, start_y = pyautogui.position()

        # Calculate the distance between the starting and ending positions.
        distance = math.sqrt((x - start_x) ** 2 + (y - start_y) ** 2)

        # Setting random number of steps to take.
        randomsteps = random.randint(1, 30)
        steps = int(distance / randomsteps)
        angle = math.atan2(y - start_y, x - start_x)

        # Set your max random deviation "angle" during mouse movement here..
        max_deviation = 10

        # Here's the goods:
        for i in range(steps):

            # Calculate the x and y coordinates with an angle
            x = start_x + i * 10 * math.cos(angle)
            y = start_y + i * 10 * math.sin(angle)

            # Added a random deviation to the x and y coordinates...
            x += random.uniform(-max_deviation, max_deviation)
            y += random.uniform(-max_deviation, max_deviation)
            pyautogui.moveTo(x, y)

            # Added a random "human-like" pauses for the botto.
            # Currently, 40% chance quick pause, 3% long pause...
            pause = random.randint(1, 100)
            if pause > 60:
                time.sleep(random.uniform(0.1, 0.5))
            elif pause > 97:
                time.sleep(random.uniform(10, 30))

        if click_at_location:
            pyautogui.doubleClick((x, y))


# Execute function as such; greyscale is set as None but could be useful, no need to define.
# Confidence goes from a scale of 0-1 in floats as you'll see below.
# Obviously you can just call the function like move_mouse("click.png", True, 0.5)
# But for demonstration:
move_mouse(image_file="click.png", click_at_location=True, confidence=0.5)

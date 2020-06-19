import pyautogui
import numpy as np  
import cv2
from PIL import ImageGrab

blueLine = ImageGrab.grab(bbox=(1,217,939,218))

ct = 0

while True:
    for y in range(217,703,75):
            img = ImageGrab.grab(bbox=(1,y,939,y + 1))
            if img != blueLine:
                line = np.array(img)
                for x in range(40, 940, 75):
                    notBlue = line[0][x][0] > 60
                    if notBlue:
                        pyautogui.click(x, y)
                        ct += 1
                        if ct >= 50:
                            print("leave")
                            exit()


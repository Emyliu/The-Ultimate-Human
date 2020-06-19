import pyautogui
import numpy as np  
import cv2
from PIL import ImageGrab

blueLine = ImageGrab.grab(bbox=(1,214,939,215))

ct = 0

while True:
    for y in range(214,703,75):
            img = ImageGrab.grab(bbox=(1,y,939,y + 1))
            if img != blueLine:
                line = np.array(img)
                bluePixel = np.array([43, 135, 209])
                for x in range(40, 940, 75):
                    small = line[0][x]
                    bluePixelTester = small == bluePixel
                    if not bluePixelTester.all():
                        pyautogui.click(x, y)
                        ct += 1
                        if ct >= 50:
                            print("leave")
                            exit()


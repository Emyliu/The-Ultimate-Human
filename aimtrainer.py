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
                for x in range(40, 940, 80):
                    small = ImageGrab.grab(bbox=(x,y,x + 1, y + 1))
                    smallNp = np.array(small)
                    clickTest = smallNp == np.array([43, 135, 209])
                    if not clickTest.all():
                        pyautogui.click(x, y)
                        ct += 1
                        if ct >= 30:
                            print("leave")
                            exit()



print("Done")
import pyautogui
import numpy as np  
import cv2
from PIL import ImageGrab

b = np.array([75, 219, 106])
ct = 0


while ct < 5:
    img = ImageGrab.grab(bbox=(300,400,301,401))
    img_np = np.array(img)
    comp2 = img_np == b
    if comp2.all():
        ct += 1
        if ct < 5:
            pyautogui.click(100, 200)
            pyautogui.click(100, 200)
        else:
            pyautogui.click(100, 200)


print("Done")
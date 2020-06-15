from PIL import ImageGrab, ImageOps, Image 
import pyautogui 
import time 
import numpy as np

class coordinates():
    button = (680, 660)
    
def play():
    pyautogui.click(coordinates.button)

def imagegrab():
    box = (660, 455, 735, 500)

    # grabbing all the pixels values in form of RGB tupples    
    image = ImageGrab.grab(box) 
  
    # converting RGB to Grayscale to 
    # make processing easy and result faster  
    grayImage = ImageOps.grayscale(image) 
  
    # using numpy to get sum of all grayscale pixels  
    a = np.array(grayImage.getcolors()) 
  
    # returning the sum 
    print(a.sum())
    return a.sum()

pyautogui.click(coordinates.button)
i=0
while True:
    if(imagegrab() > 11000):
        play()
        i += 1
        if(i<40):
            time.sleep(1)
        else:
            time.sleep(0.3)


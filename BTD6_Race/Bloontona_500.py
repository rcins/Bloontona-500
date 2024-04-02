import pyautogui 
import time
import cv2 as cv
import numpy as np 

# Function finds Icon on screen

def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = pyautogui.locateCenterOnScreen(image, confidence=.7)

    if position is None:
        print(f'{image} not found...')
        return 0
    else:
        pyautogui.moveTo(position, duration=.1)
        pyautogui.moveRel(off_x, off_y)
        pyautogui.click(clicks=clicks, interval=.3)


Ready_Status = False

input("Press ENTER to begin the script for Bloontona 500 Achievement...")

#Short Countdown Before  Script Begins.
print("The Script is about to begin, you have 10 seconds to cancel this and close the script.")
time.sleep(10)

Ready_Status = True
Loops = 0
#Looping our code

while Ready_Status == True:
    #Race Icon
    nav_to_image('Images\Race_monkey.png', 1)
    time.sleep(0.05)

    #Race Button
    nav_to_image('Images\Race_button.png', 1)
    time.sleep(3)

    #Ok Button
    nav_to_image('Images\OK.jpg', 1)
    time.sleep(0.05)

    #Settings Button
    nav_to_image('Images\Settings_Icon.png', 1)
    time.sleep(1)

    #Return To Home Icon
    nav_to_image('Images\Home_Icon.png', 1)
    Loops +=1
    time.sleep(3)
    
    if Loops == 500:
        Ready_Status = False
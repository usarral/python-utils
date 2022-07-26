import time
import subprocess
import pyautogui

def TeamViewer():
    
    subprocess.call("C:\Program Files\TeamViewer\TeamViewer.exe")   
    pass;

def main():
    bootMouseX, bootMouseY = pyautogui.position() # Get the XY position of the mouse.
    time.sleep(30) # Wait 30 seconds.
    endMouseX, endMouseY = pyautogui.position() # Get the XY position of the mouse.

    if (bootMouseX == endMouseX) and (bootMouseY == endMouseY):
        TeamViewer();
    else:
        print("User is on the computer")

main()

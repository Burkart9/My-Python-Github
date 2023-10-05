# Libs
import time
import pyautogui

# Functions
def auto_click(t:int):
    time.sleep(t)
    print("Start!")
    pyautogui.rightClick(1900,900)
    print("右键点击一次")
    time.sleep(0.1)
    pyautogui.leftClick(1900,900)
    print("左键点击一次")




# Main
if __name__=="__main__":
    auto_click(1)
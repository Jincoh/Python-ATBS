# active window doesn't work on linux thus won't be included in this script

import pyautogui as pgui

def main():

    pgui.tripleClick(1222,294)
    pgui.hotkey("ctrl", "c")
    pgui.click(345,397)
    pgui.hotkey("ctrl","shift", "v")

if __name__ == "__main__":
    main() 

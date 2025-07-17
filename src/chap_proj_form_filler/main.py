import pyautogui

def main():
    pyautogui.click(715,480)

    pyautogui.write("some text\t", 0.02)
    pyautogui.write("some more text\t", 0.02)

    pyautogui.write(" ", 0.25)
    pyautogui.write(["down", "down", "down"], 0.25)
    pyautogui.write(" ", 0.5)
    pyautogui.write("\t")

    pyautogui.write(["space"], 0.5)
    pyautogui.write("\t\t", 0.25)
    pyautogui.write("The last text\t", 0.02 )


if __name__ == "__main__":
    main()

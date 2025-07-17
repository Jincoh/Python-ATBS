import pyautogui
import random
import time

def main():
    while(True):
        try:
            wait = random.randint(180, 300)
            time.sleep(wait)
            print(wait)

            pyautogui.move(random.randint(-100, 100),random.randint(-100,100))
        except KeyboardInterrupt:
            print("keyboard interrupt")
            return

if __name__ == "__main__":
    main()

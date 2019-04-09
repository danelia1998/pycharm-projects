import pyautogui
import time
def autoClicker():
    pyautogui.moveTo(316, 740, duration=0.5)
    pyautogui.click(316, 740)
    play = 1
    while play == 1:
        for eachClick in range(1,10):
                #for each loop
            pyautogui.doubleClick(590,350)
                    #for click in
            pyautogui.moveTo(1157,404,duration = 1)
            pyautogui.click(1157,404)
            pyautogui.moveTo(590,350,duration = 1)
        play = int(input("Wanna continue?if yes press 1"))
        pyautogui.moveTo(316, 740, duration=0.1)
        pyautogui.click(316, 740)


def main():
    autoClicker()
if __name__ == '__main__':
    main()


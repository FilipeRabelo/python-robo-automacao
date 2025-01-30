import pandas as pd
import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://www.youtube.com/index')
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=466, y=141)
pyautogui.write('@jujuerafashow')
pyautogui.press('enter')

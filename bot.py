import pyautogui as pg
import time

time.sleep(10)
txt = open('palavras.txt', 'r+')

for i in txt:
    pg.write(i)
    pg.press('Enter')

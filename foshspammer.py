import pyautogui as pg
import time

time.sleep(10)

txt = open('text.txt', 'r')

for i in txt:
    pg.write(i)
    pg.press('Enter')
print('Fosh Ha Ba Movafageiat Chop Shodand!')

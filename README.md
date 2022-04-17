import pyatogui as pg
import time

time.sleep(10)

txt = open('text.txt', 'r')

for i in txt:
    pg.write("To Ek %s Haste"%(i))
    pg.press('Enter')

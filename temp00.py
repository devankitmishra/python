import random
# @python.coder_

import pyautogui as pg

import time
animal = ('monkey')

time.sleep(8)

for i in range(50):
    a = random.choice(animal)
    pg.write("You are a "+a)
    pg.press("enter")
import pyautogui as pg
import time
time.sleep(3)

messages = ("hi!",
          "this messages",
          "written by a bot",
          "hahaha",
          "cool right",
          "this is an experiment by yugurlu")
i = 0
for i in range(len(messages)):
    a = (messages[i])
    pg.write(a, 0.1)
    pg.press("enter")
    time.sleep(1.5)
    i += 1

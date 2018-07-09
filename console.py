import time
import keyboard
import ctypes
import random

print("PythonAutoClicker by Fexooo")
print("GitHub: github.com/Fexooo")
varstart = 1;
varend = 1;
time.sleep(1)

print("How much Clicks per Second?")
speed = input("CPS: ")
print("Which Key should trigger it? (Key has to be in lower case!)")
ckey = input("Key: ")
print("Which Key should close this Program?")
ekey = input("Key: ")
print("Constant CPS? y/n")
constant = input(">")
if constant != "y":
    print("Variation Start and End: (open README.MD for more Information on how to use Variation)")
    varstart = input("Start (leave free for constant): ")
    varend = input("End (leave free for constant): ")
    while True:
        speedfl = float(speed)
        speedfi = float(1 / speedfl)
        if keyboard.is_pressed(ckey):
            ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
            ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
            time.sleep(speedfi * random.uniform(float(varstart), float(varend)))
        if keyboard.is_pressed(ekey):
            print("Shutdown by Key!")
            exit()
else:
    while True:
        speedfl = float(speed)
        speedfi = float(1 / speedfl)
        if keyboard.is_pressed(ckey):
            ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
            ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
            time.sleep(speedfi)
        if keyboard.is_pressed(ekey):
            print("Shutdown by Key!")
            exit()
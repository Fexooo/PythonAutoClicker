import time
import keyboard
import ctypes
import random
from tkinter import *
from tkinter import messagebox

version = "1.1"
started = 0

def deve():
    messagebox.showinfo("PythonAutoClicker " + version, "Welcome to PythonAutoClicker " + version + "! \n If you need help on how to use this program open the README.MD! \n Programmed by Fexo! \n Github: Fexooo \n Twitter: @FexoYT \n Instagram: @F.exoo \n YouTube: Fexo")

def run():
    ekey = ek.get()
    ckey = ck.get()
    ecpsvar = ecps.get()
    evs = evstart.get()
    eve = evend.get()
    speedfl = float(ecpsvar)
    speedfi = float(1 / speedfl)
    if keyboard.is_pressed(ekey):
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
        time.sleep(speedfi * random.uniform(float(evs), float(eve)))
        root.after(0, run)
    if keyboard.is_pressed(ckey):
        root.destroy
        exit()
    root.after(1, run)

def start():
    print("Start!")
    ekey = ek.get()
    ckey = ck.get()
    ecpsvar = ecps.get()
    evs = evstart.get()
    eve = evend.get()
    if ekey and ckey and ecpsvar != "":
        if evs and eve != "":
            lockentrys()
        else:
            messagebox.showerror("PythonAutoClicker " + version, "An Error has occured! Code: 2 \n Please make sure the Variation Values are set!")
    else:
        messagebox.showerror("PythonAutoClicker " + version, "An Error has occured! Code: 1 \n Please make sure the Activation, Close Key and CPS are set!")


root = Tk()
root.title("PythonAutoClicker " + version)
root.geometry("300x230")
root.iconbitmap("main.ico")

top = Frame(root)
top.pack()

mid = Frame(root)
mid.pack()

bot = Frame(root)
bot.pack(side=BOTTOM)

head = Label(top, text="PythonAutoClicker " + version)
head.config(font=("Arial", 20))
head.pack()

dev = Label(top, text="by Fexooo")
dev.config(font=("Arial", 10))
dev.pack()

Label(mid, text="CPS:").grid(row=0)

ecps = Entry(mid)
ecps.grid(row=0, column=1)

Label(mid, text="Activation Key:").grid(row=1)

ek = Entry(mid)
ek.grid(row=1, column=1)

Label(mid, text="Close Key:").grid(row=2)

ck = Entry(mid)
ck.grid(row=2, column=1)

Label(mid, text="Variation (1 for no Variation)").grid(row=4)

Label(mid, text="Start Value:").grid(row=5)
evstart = Entry(mid)
evstart.grid(row=5, column=1)
Label(mid, text="End Value:").grid(row=6)
evend = Entry(mid)
evend.grid(row=6, column=1)
start = Button(bot, command=start, text="Start").grid(row=1, column=0)
help = Button(bot, command=deve, text="Help").grid(row=1, column=1)

def lockentrys():
    ek.config(state='disabled')
    ck.config(state='disabled')
    ecps.config(state='disabled')
    evstart.config(state='disabled')
    evend.config(state='disabled')
    run()

root.mainloop()
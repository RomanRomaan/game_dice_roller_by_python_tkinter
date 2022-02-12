from tkinter import *
import random, time
import tkinter as tk
from turtle import left

def throw():
    x = random.choice(['dice/img/one.png','dice/img/two.png', 'dice/img/three.png', \
        'dice/img/four.png', 'dice/img/five.png', 'dice/img/six.png'])
    return x    


def img(event):
    global b1, b2
    for i in range(18):
        b1 = PhotoImage(file=(throw()))
        b2 = PhotoImage(file=(throw()))
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time.sleep(0.12)

root = Tk()
root.geometry('800x400')
root.title('Игра в кости.  Сделай бросок!')
root.resizable(height=False, width=False)                   # не рисайзится
root.iconphoto(True, PhotoImage(file=('dice/img/icon.png')))   # окно
font = PhotoImage(file=('dice/img/bg.png'))

Label(root, image=font).pack()                         #расместить на окне image=font

lab1 = Label(root)
lab1.place(relx=0.5, rely=0.5, anchor=CENTER)

lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)

root.bind('<1>', img)
img('event')

root.mainloop()




# pip install pyinstaller
# pyinstaller -w dice.py
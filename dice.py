from tkinter import *
import random, time


root = Tk()
root.geometry('800x400')
root.title('Игра в кости.')
root.resizable(height=False, width=False)                   # не рисайзится
root.iconphoto(True, PhotoImage(file=('dice/img/icon.png')))   # окно
font = PhotoImage(file=('dice/img/bg.png'))
Label(root, image=font).pack()                         #расместить на окне image=font


def throw():
    x = random.choice(['dice/img/one.png','dice/img/two.png', 'dice/img/three.png', \
        'dice/img/four.png', 'dice/img/five.png', 'dice/img/six.png'])
    return x


def get_img(event):
    global b1, b2
    
    for i in range(3):
        b1 = PhotoImage(file=(throw()))
        b2 = PhotoImage(file=(throw()))

        lab1['image'] = b1
        lab2['image'] = b2  

        root.update()
        time.sleep(0.12)
          


lab1 = Label(root)
lab1.place(relx=0.4, rely=0.4, anchor=CENTER)

lab2 = Label(root)
lab2.place(relx=0.6, rely=0.4, anchor=CENTER)

trying = 0
while trying != 6:
    if lab1 or lab2 == 'dice/img/one.png':
        counter = 1
    if lab1 or lab2 == 'dice/img/two.png':
        counter = 2
    if lab1 or lab2 == 'dice/img/three.png':
        counter = 3                
    if lab1 or lab2 == 'dice/img/four.png':
        counter = 4
    if lab1 or lab2 == 'dice/img/five.png':
        counter = 5
    if lab1 or lab2 == 'dice/img/six.png':
        counter = 6    
    trying += 1    


label_name1 = Label(text='Игрок ', fg='white', bg='blue2', width=14, height=2)
label_name1.place(relx=0.54, rely=0.15, anchor=NW)

label_name2 = Label(text='Компьютер ', fg='white', bg='blue2', width=14, height=2)
label_name2.place(relx=0.33, rely=0.15, anchor=NW)

count1 = Label(text=f'Счет: {counter}', font=32, fg='white', bg='green', width=10, height=2)
count1.place(relx=0.337, rely=0.57)

count2 = Label(text=f'Счет: {counter}', font=32, fg='white', bg='green', width=10, height=2)
count2.place(relx=0.54, rely=0.57)


button = Button(width=20, height=2,fg='white', font=32, bg='blue', text='Сделай бросок!')
button.place(relx=0.5,  rely=0.78, anchor=CENTER )


root.bind('<1>', get_img)
get_img('event')


root.mainloop()




# pip install pyinstaller
# pyinstaller -w dice.py
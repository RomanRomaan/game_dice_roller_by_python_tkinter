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
    print(x)   
    return x  


def get_count(x):
    if x == 'dice/img/one.png':
        return 1
    elif x == 'dice/img/two.png': 
        return 2
    elif x == 'dice/img/three.png': 
        return 3
    elif x == 'dice/img/four.png': 
        return 4
    elif x == 'dice/img/five.png': 
        return 5
    elif x == 'dice/img/six.png': 
        return 6        


def get_img(event):
    global b1, b2
    
    #for i in range(1):
    b1 = PhotoImage(file=(throw()))
    b2 = PhotoImage(file=(throw()))

    lab1['image'] = b1
    lab2['image'] = b2  

    slab1 = get_count(b1)
    slab2 = get_count(b2)

    root.update()
    time.sleep(0.12) 

    #ub_dice_label1.config(text=slab1)
    #sub_dice_label2.config(text=slab2)
            

lab1 = Label(root)
lab1.place(relx=0.4, rely=0.4, anchor=CENTER)
sub_dice_labal1 = Label(text="5555")
sub_dice_labal1.place(relx=0.54, rely=0.57)


lab2 = Label(root)
lab2.place(relx=0.6, rely=0.4, anchor=CENTER)


label_name1 = Label(text='Игрок ', fg='white', bg='blue2', width=14, height=2)
label_name1.place(relx=0.54, rely=0.15, anchor=NW)

label_name2 = Label(text='Компьютер ', fg='white', bg='blue2', width=14, height=2)
label_name2.place(relx=0.33, rely=0.15, anchor=NW)

#count1 = Label(text=f'Счет: ', font=32, fg='white', bg='green', width=10, height=2)
#count1.place(relx=0.337, rely=0.57)
#count2 = Label(text=f'Счет: ', font=32, fg='white', bg='green', width=10, height=2)
#count2.place(relx=0.54, rely=0.57)


button = Button(width=20, height=2,fg='white', font=32, bg='blue', text='Сделай бросок!')
button.place(relx=0.5,  rely=0.78, anchor=CENTER )


root.bind('<1>', get_img)
get_img('event')


root.mainloop()




# pip install pyinstaller
# pyinstaller -w dice.py
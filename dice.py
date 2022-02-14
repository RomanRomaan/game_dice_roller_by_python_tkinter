from tkinter import *
import random, time


root = Tk()
root.geometry('800x500')
root.title('Игра в кости.')
root.resizable(height=False, width=False)                   
root.iconphoto(True, PhotoImage(file=('dice/img/icon.png')))  
font = PhotoImage(file=('dice/img/bg.png'))
Label(root, image=font).pack()                         
count1 = count2 = 0

def get_img(event):
    global b1, b2, count1, count2
    dice_img = ['dice/img/one.png', 'dice/img/two.png', 'dice/img/three.png', \
        'dice/img/four.png', 'dice/img/five.png', 'dice/img/six.png']

    for i in range(3):    
        x = random.choice(dice_img)
        x2 = random.choice(dice_img)    
        print(x, x2)  
    
        b1 = PhotoImage(file=x)
        b2 = PhotoImage(file=x2)
        lab1['image'] = b1
        lab2['image'] = b2 
        
        num_x = get_count(x)
        num_x2 = get_count(x2)

        sub_dice_labal1.config(text=f'тек.счет: {num_x}')
        sub_dice_labal2.config(text=f'тек.счет: {num_x2}')            

    count1 += num_x
    count2 += num_x2
    print(count1)


    total_count1.config(text=f'общ.сч:{count1}')
    total_count2.config(text=f'общ.сч:{count2}')
    if count1 > 50 and count1 > count2:
        total_count1.config(text=f'Вы выиграли! общ.сч:{count1}.')
        
    elif count2 > 50 and count2 > count1:
        total_count2.config(text=f'Вы выиграли! общ.сч:{count2}')
        


    
    root.update()
    time.sleep(0.12)


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
            

lab1 = Label(root)
lab1.place(relx=0.4, rely=0.4, anchor=CENTER)
sub_dice_labal1 = Label(fg='white', bg='green', width=14, height=2)
sub_dice_labal1.place(relx=0.34, rely=0.57)
total_count1 = Label(fg='white', bg='blue', width=14, height=2)
total_count1.place(relx=0.34, rely=0.68)

lab2 = Label(root)
lab2.place(relx=0.6, rely=0.4, anchor=CENTER)
sub_dice_labal2 = Label(fg='white', bg='green', width=14, height=2)
sub_dice_labal2.place(relx=0.54, rely=0.57)
total_count2 = Label(fg='white', bg='blue', width=14, height=2)
total_count2.place(relx=0.54, rely=0.68)


label_name1 = Label(text='Игрок ', fg='white', bg='blue2', width=14, height=2)
label_name1.place(relx=0.54, rely=0.15, anchor=NW)

label_name2 = Label(text='Компьютер ', fg='white', bg='blue2', width=14, height=2)
label_name2.place(relx=0.33, rely=0.15, anchor=NW)

button = Button(width=20, height=2,fg='white', font=32, bg='blue', text='Сделай бросок!')
button.place(relx=0.5,  rely=0.88, anchor=CENTER )


root.bind('<1>', get_img)
get_img('event')

root.mainloop()


# pip install pyinstaller
# pyinstaller -w dice.py

import tkinter
from tkinter import *
import random , string

root = Tk()
root.geometry('400x280')
root.title('Password Generator')
root.configure(background='black')
root.iconphoto(False,tkinter.PhotoImage(file="padlock_icon.png"))
# intro text
title = StringVar()
label = Label(root,textvariable=title).pack()
title.set('THE STRENGTH PASSWORD')

def selection():
    selection = choice.get()

choice = IntVar()
R1 = Radiobutton(root,text='Poor',variable=choice,value=1,command=selection).pack(anchor=CENTER)
R2 = Radiobutton(root,text='Average',variable=choice,value=2,command=selection).pack(anchor=CENTER)
R3 = Radiobutton(root,text='Advanced',variable=choice,value=3,command=selection).pack(anchor=CENTER)
labchoice = Label(root)

lenlabel = StringVar()
lenlabel.set("password length")
lentitle=Label(root,textvariable=lenlabel).pack()

Val=IntVar()
spinlength=Spinbox(root,from_=8,to=24,textvariable=Val,width=13).pack()

def callback():
    sum.config(text=passgen())

passgenButton=Button(root,text="Generate password",bd=6,height=1,command=callback,pady=5)
passgenButton.pack()

sum=Label(root,text='')
sum.pack(side=BOTTOM)

# logic
poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """''`!@$#%^&*()_-+:;,.<>?=[]{}|/\?''"""
advance = poor + average + symbols

def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor,Val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average,Val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance,Val.get()))

root.mainloop()

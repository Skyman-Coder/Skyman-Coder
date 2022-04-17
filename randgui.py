#GUI Random Password Maker By Tel:@Amir_Synt
from tkinter import *
import random

root = Tk()

#Style Settings
root.title("Random Password")
root.geometry("300x210")
root.iconbitmap('blueic.ico')

#case variables
lower_case = "abcdefghijklmnupqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNUPQRSTUVWXYZ"
nums = "0123456789"

result = upper_case+lower_case+nums

#GUI CODES
top = Label(root, text="Password Input")
top.pack()

e = Entry(root, borderwidth=5, width=40)
e.pack()

def submit():
    e.delete(0, END)
    sampled = "".join(random.sample(result, random.randint(4,18)))
    e.insert(0, sampled)

mybtn = Button(root, text="Create Password", command=submit)
mybtn.pack()

root.mainloop()

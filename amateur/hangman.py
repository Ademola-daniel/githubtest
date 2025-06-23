import tkinter as tk
from tkinter import ttk
import _random
import random
tries=0
no_tries=3
def delete():
    data=entry.get()
    da=len(data)
    entry.delete(0,da)

def game():
    tries=0
    no_tries=3
    list=['pascal','ezeugo','faladz','destiny','ademola','victor','shanfar']
    rand=random.choice(list)


    while tries!=no_tries:
        data=entry.get()
        data2=len(data)
        tries+=1
        if data==rand:
            entry.delete(0,data2)
            entry.insert(0,'Correct answer')
            break
        elif data!=rand:
            entry.delete(0,data2)

            entry.insert(0,'try again')

        else:

            entry.delete(0,data2)
            label.config(text='out of chances',font=('ALGERIAN',11,'bold'))
            break




root=tk.Tk()
root.title('H🔼NGM🔼N')
root.configure(bg='light blue')
style =ttk.Style()
style.theme_use('clam')
entry=ttk.Entry(root)
entry.pack()
button=ttk.Button(root,text='Guess',command=game)
button.pack()
button=ttk.Button(root,text='delete',command=delete)
button.pack()
label=ttk.Label(root,text='[pascal,ezeugo,faladz,destiny,ademola,victor,shanfar]',font=('ALGERIAN',11,'bold'))
label.pack()


root.mainloop()

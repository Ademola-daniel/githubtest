from tkinter import *
root = Tk()
root.title('Calculator')
i = 0
def display(num):
    global i
    entry.insert(i,num)
    i+=1


def clear():

    entry.delete(0,END)


def deli():
    string = entry.get()
    if string:
        newstring= string[:-1]
        clear()
        entry.insert(0,newstring)
    else:
        entry.insert(0,' ')

def operation(operator):
    global i
    result=len(operator)
    entry.insert(i,operator)
    i+= result


def compute():

    computation = entry.get()
    new =eval(computation)
    clear()
    entry.insert(0,str(new))

def fact():
    result = 1
    data= entry.get()
    data2=int(data)
    if data2 == 1:
        entry.insert(0,'1')
    else:
        for i in range(1,data2+1):
            result*= i
            ans = str(result)
            clear()
            entry.insert(0,ans)

entry=Entry(root)
entry.grid(row=1,columnspan=6,sticky =W+E)

Button(root,text='1',padx =2,pady=2,bg='Black',fg='White',command=lambda:display(1)).grid(row=2,column=0)
Button(root,text='2',padx =2,pady=2,bg='Black',fg='White',command=lambda:display(2)).grid(row=2,column=1)
Button(root,text='3',padx =2,pady=2,bg='Black',fg='White',command=lambda:display(3)).grid(row=2,column=2)

Button(root,text='4',padx =2,pady=2,bg='Black',fg='White',command=lambda:display(4)).grid(row=3,column=0)
Button(root,text='5',padx =2,pady=2,bg='Black',fg='White',command=lambda:display(5)).grid(row=3,column=1)
Button(root,text='6',padx =2,pady=2,bg='Black',fg='White',command=lambda:display(6)).grid(row=3,column=2)

Button(root,text='7',padx =2,pady=2,bg='Black',fg='White',command=lambda:display(7)).grid(row=4,column=0)
Button(root,text='8',padx =2,pady=2,bg='Black',fg='White',command=lambda:display(8)).grid(row=4,column=1)
Button(root,text='9',padx =2,pady=2,bg='Black',fg='White',command=lambda:display(9)).grid(row=4,column=2)

Button(root,text='Ac',padx =2,pady=2,bg='Black',fg='White',command= lambda:clear()).grid(row=5,column=0)
Button(root,text='0',padx =2,pady=2,bg='Black',fg='White',command=lambda:display(0)).grid(row=5,column=1)
Button(root,text='=',padx =2,pady=2,bg='Black',fg='White',command=lambda:compute()).grid(row=5,column=2)

Button(root,text='+',padx =2,pady=2,bg='Black',fg='White',command=lambda:operation('+')).grid(row=2,column=3)
Button(root,text='-',padx =2,pady=2,bg='Black',fg='White',command=lambda:operation('-')).grid(row=3,column=3)
Button(root,text='*',padx =2,pady=2,bg='Black',fg='White',command=lambda:operation('*')).grid(row=4,column=3)
Button(root,text='/',padx =2,pady=2,bg='Black',fg='White',command=lambda:operation('/')).grid(row=5,column=3)

Button(root,text='<-',padx =2,pady=2,bg='Black',fg='White',command=lambda:deli()).grid(row=2,column=4)
Button(root,text='!',padx =2,pady=2,bg='Black',fg='White',command=lambda:fact()).grid(row=3,column=4)
Button(root,text='^',padx =2,pady=2,bg='Black',fg='White',command=lambda:operation('**')).grid(row=4,column=4)
Button(root,text='',padx =2,pady=2,bg='Black',fg='White').grid(row=5,column=4)


root.mainloop()

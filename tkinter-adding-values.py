from tkinter import*
def add():
    num1 = number1.get()
    num2 = number2.get()
    num3 = number3.get()
    result = num1+num2+num3
    resultlabel.config(text='Result:%d' %result)

obj = Tk()
obj.geometry('500x500')
obj.title('operations')
obj.configure(bg='lightblue')

Label(obj,text='Enter value A:', font=('calibri',20),bg='lightblue').grid(row=1,column=1)
Label(obj,text='Enter value B:', font=('calibri',20),bg='lightblue').grid(row=2,column=1)
Label(obj,text='Enter value C:', font=('calibri',20),bg='lightblue').grid(row=3,column=1)

number1 = IntVar()
number2 = IntVar()
number3 = IntVar()

Entry(obj, textvariable=number1, font=('calibri',17)).grid(row=1,column=2)
Entry(obj, textvariable=number2, font=('calibri',17)).grid(row=2,column=2)
Entry(obj, textvariable=number3, font=('calibri',17)).grid(row=3,column=2)

Button(obj, text='ADD',command=add,font=('calibri',20),bg='gray',fg='white',width='10',height='1').grid(row=4,column=2)

resultlabel = Label(obj,font=('calibri',20,'bold'),bg='lightblue',fg='red')
resultlabel.grid(row=5,column=2)

obj.mainloop()
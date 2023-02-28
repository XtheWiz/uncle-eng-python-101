from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')

B1 = ttk.Button(GUI, text='เงินมีอยู่กี่บาท')
B1.pack(ipadx=20, ipady=20)

L1 = Label(GUI, text='โปรแกรมบันทึกฟามรู้', font=('Sarabun TH', 30), fg='lime')
L1.place(x=50, y=100)

#############################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showerror('เงินในบัญชี', text)

FB1 = LabelFrame(GUI, text='Money')
FB1.place(x=100, y=300)

B2 = ttk.Button(FB1, text='เงินมีอยู่กี่บาท', command=Button2)
B2.pack(padx=10, pady=10)
# B2.place(x=50, y=200)

#############################
def Button3():
    text = 'ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showerror('เงินในบัญชี', text)

FB2 = LabelFrame(GUI, text='Money')
FB2.place(x=300, y=300)

B3 = ttk.Button(FB2, text='เงินมีอยู่กี่บาท', command=Button2)
B3.pack(padx=10, pady=10)

GUI.mainloop()

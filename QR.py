from tkinter import *
import pyqrcode
from tkinter import ttk
window= Tk()
window.title("qrcode generator")
l=Label(window,text="        ").pack()
l1=Label(window,text="enter text here:",font=("Verdana",15)).pack()
e=Entry(window,width=45,borderwidth=10)
e.pack()
l2=Label(window,text="              ").pack()
def gen():
    url = pyqrcode.create(str(e.get()))
    url.png("qr.png", scale=10)
    quit()

b1=Button(window,text="Generate",command=gen).pack()
window.geometry('300x150')
window.mainloop()
import tkinter as tk
m=tk.Tk()
m.title('counting seconds')
button=tk.Button(m,text='stop',width=25,command=m.destroy)
button.pack()
m.mainloop()

from tkinter import *
master=Tk()
w=Canvas(master,width=40,height=60)
w.pack()
canvas_height=200
canvas_width=200
y=int(canvas_height/2)
w.create_line(0,y,canvas_width,y)
mainloop()

from tkinter import *
master=Tk()
var1=IntVar()
Checkbutton(master,text='male',variable=var1).grid(row=0,sticky=W)
var2=IntVar()
Checkbutton(master,text='female',variable=var2).grid(row=1,sticky=W)
mainloop()


from tkinter import *
master=Tk()
Label(master,text='first name').grid(row=0)
Label(master,text='Last name').grid(row=1)
e1=E

#question1
import tkinter as tk
from tkinter import *
kav=tk.Tk()
kav.title("info")
dict={'name':'kavya','mobile_number':9915661563}
scrollbar=Scrollbar(kav)
scrollbar.pack(side=LEFT,fill=Y)
mylist=Listbox(kav,yscrollcommand= scrollbar.set)
for key in dict.__iter__():
        mylist.insert(END,key)
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)
def kavy():
    kav.quit()
b=Button(kav,text="enter",command=kavy)
b.pack()
kav.mainloop()


#question2

def kavya():
    dict.update({"age":21})
    print(dict)
button1=Button(kav,text='good',command=kavya())
button1.pack()
kav.mainloop()
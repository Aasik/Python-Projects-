# import library
from tkinter import *

# Intializing window
root = Tk()
root.geometry('400x400')
root.config(bg='SlateGray3')
root.title('DataFlair-AddressBook')
root.resizable(0,0)

contactList = [
    ['Mohamed Aasik','0775082936'],
    ['Mohamed', '133456987'],
    ['Prisha','789654123'],
    ['Rahul', '456987123'],
    ['Suleiman Shah', '123789654'],
    ['Parv', '963258741'],
]

Name = StringVar()
Number = StringVar()

# create frame
frame = Frame(root)
frame.pack(side= RIGHT)


scroll = Scrollbar(frame, orient = VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12)
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
scroll.pack(side=LEFT, fill=BOTH, expand=1)

# Define functions
def selected():
    return int(select.curselection()[0])

def AddContact():
    contactList.append([Name.get(), Number.get()])
    select_set()

def EDIT():
    contactList[selected()] = [Name.get(), Number.get()]
    select_set()

def DELETE():
    del contactList[selected()]
    select_set()

def VIEW():
    NAME, PHONE = contactList[selected()]
    Name.set(NAME)
    Number.set(PHONE)

def EXIT():
    root.destroy()

def RESET():
    Name.set('')
    Number.set('')

def select_set():
    contactList.sort()
    select.delete(0,END)
    for name,phone in contactList:
        select.insert(END,name)
select_set()

# define buttons and labels and entry widgets

Label(root, text='NAME', font='arial 12 bold', bg='SlateGray3').place(x=30, y=20)
Entry(root, textvariable=Name).place(x=100, y=20)

Label(root, text='PHONE NO.', font='arial 12 bold', bg='SlateGray3').place(x=30, y=70)
Entry(root, textvariable=Number).place(x=130, y=70)

Button(root, text='ADD', font='arial 12 bold', bg='SlateGray4', command=AddContact).place(x=50, y=110)

Button(root, text='EDIT', font='arial 12 bold', bg='SlateGray4', command=EDIT).place(x=50, y=260)

Button(root, text='DELETE', font='arial 12 bold', bg='SlateGray4', command=DELETE).place(x=50, y=210)

Button(root,text='VIEW', font='arial 12 bold', bg='SlateGray4', command=VIEW).place(x=50, y=160)

Button(root, text='EXIT', font='arial 12 bold', bg='tomato', command=EXIT).place(x=300, y=320)

Button(root, text='RESET', font='arial 12 bold', bg='SlateGray4', command=RESET).place(x=50, y=310)

root.mainloop()






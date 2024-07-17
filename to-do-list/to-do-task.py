from tkinter import *

def addtsk():
    add_tsk = label_input.get()
    list_box.insert(END, add_tsk)
    label_input.delete(0, END)

def deltsk():
    for i in list_box.curselection():
        list_box.get(i)
        list_box.delete(i)

def upd_tsk():
    for item in list_box.curselection():
        list_box.delete(item)
        list_box.insert("end", addtsk())

def clr_task():
    list_box.delete(0, END)

root = Tk()
root.geometry("700x700")

root.title("TO-DO LIST")
root.configure(background="#0096DC")
root.iconbitmap("to-do-list.ico")


title = Label(root, text="TO-DO LIST", font='Sans 18 bold', background="#0096DC", fg="white")
title.pack(pady=(20, 10))

label = Label(root, text="Enter Your Task Here: ", font='Sans 14', background='#0096DC')
label.pack()

label_input = Entry(root, background="white", width=50, font="sans 13")
label_input.pack(ipady=5)

add_btn = Button(root, text="ADD TASK", font="Sans 10 bold", command=addtsk)
add_btn.pack(pady=(10, 1))

del_btn = Button(root, text="DELETE TASK", font="Sans 10 bold", command=deltsk)
del_btn.pack(pady=(10, 1))

upd_btn = Button(root, text="UPDATE TASK", font="Sans 10 bold", command=upd_tsk)
upd_btn.pack(pady=(10, 1))

clr_btn = Button(root, text="CLEAR ALL TASK", font="Sans 10 bold", command=clr_task)
clr_btn.pack(pady=(10, 10))

label2 = Label(root, text="TASKS :", font="Sans 14 bold", background="#0096DC")
label2.pack(pady=(20, 10))

list_box = Listbox(root, width=40, font="sans 16")
list_box.pack(ipady=50)

root.mainloop()

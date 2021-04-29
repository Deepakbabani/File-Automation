import shutil
import pyautogui as p
import os
import tkinter
from tkinter import *
win = Tk()
win.title("File Automation")
win.configure(bg="#17202A")
win.geometry("800x400")
win.resizable(width=False, height=False)


def automate():
    folder_path = x.get()
    try:
        try:
            for i in os.listdir(folder_path):
                name = os.path.splitext(i)[1]
                name = name.split(".")
                if(len(name) > 1):
                    moving_path = os.path.join(folder_path, name[1])
                    if name[1] in os.listdir(folder_path):
                        shutil.move(folder_path+i, moving_path)
                    else:
                        os.mkdir(moving_path)
                        shutil.move(folder_path+i, moving_path)
            if(p.alert("Automation Completed Successfully") == "OK"):
                exit()
        except shutil.Error:
            os.remove(folder_path + i)
            p.alert("A file already exist")

    except FileNotFoundError:
        con = p.confirm("Enter the correct path")
        if con != "OK":
            exit()


def stop():
    o = p.confirm("Are you sure?", buttons={'Yes', "Cancel"})
    if o == "Yes":
        exit()


x = tkinter.StringVar()
b1 = Button(win, text="Start", fg="white", bg="#3b5998", command=automate)
b2 = Button(win, text="Stop", fg="white", bg="#3b5998", command=stop)
b1.place(x=305, y=170, width=80, height=30)
b2.place(x=405, y=170, width=80, height=30)
e = Entry(win, textvariable=x)
e.place(x=250, y=120, width=300, height=30)
l = Label(win, text="Enter Path", font=80)
l.place(x=345, y=80)
win.mainloop()

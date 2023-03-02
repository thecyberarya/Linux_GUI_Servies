from tkinter import *
from PIL import Image, ImageTk
import os

def startdocker():
    os.popen('systemctl start nessusd.service ')
    exit()

def stopdocker():
    os.popen('systemctl stop nessusd.service ')
    exit()

win = Tk()
win.title("Nessus Servies")
win.geometry("400x190")
win.resizable(FALSE,FALSE)
p1 = PhotoImage(file = '/home/dhirajarya/Softwares/nessus/icon.png')   
win.iconphoto(False, p1)

image=Image.open('/home/dhirajarya/Softwares/nessus/img.png')
img=image.resize((400, 130))
my_img=ImageTk.PhotoImage(img)
label=Label(win, image=my_img)
label.pack()

btn = Button(win, text="Start",command=startdocker,width=10,height=2)
btn.place(x=50,y=130)

btn2 = Button(win, text="Stop",command=stopdocker,width=10,height=2)
btn2.place(x=250,y=130)

win.mainloop()

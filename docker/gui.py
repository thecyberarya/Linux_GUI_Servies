from tkinter import *
from PIL import Image, ImageTk
import os

def startdocker():
    os.popen('systemctl start docker.socket')
    exit()

def stopdocker():
    os.popen('systemctl stop docker.socket')
    exit()

win = Tk()
win.title("Docker Servies")
win.geometry("400x190")
win.resizable(FALSE,FALSE)
p1 = PhotoImage(file = '/home/dhirajarya/Softwares/docker/icon.png')   
win.iconphoto(False, p1)

image=Image.open('/home/dhirajarya/Softwares/docker/img.png')
img=image.resize((380, 120))
my_img=ImageTk.PhotoImage(img)
label=Label(win, image=my_img)
label.pack()

btn = Button(win, text="Start",command=startdocker,width=10,height=2)
btn.place(x=50,y=130)

btn2 = Button(win, text="Stop",command=stopdocker,width=10,height=2)
btn2.place(x=250,y=130)

win.mainloop()

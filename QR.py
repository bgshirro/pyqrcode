from tkinter import *
from tkinter import messagebox
import pyqrcode
import os
window = Tk()
window.title("QR Code Generator")
def generate():
    if len(subject.get()) != 0:
        global myQr
        myQr = pyqrcode.create(subject.get())
        qrImage = myQr.xbm(Scale=6)
        global photo
        photo = BitmapImage(data=qrImage)
    else:
        messagebox.showinfo("Error!," "Please Enter The Subject")
    try:
        showCode()
    except:
        pass
def showCode():
    global photo
    notificationLabel.config(image=photo)
    subLabel.config(text="showing QR Code for:" + subject.get())
def save():
    dir = path1 = os.getcwd() + "\\QR Codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get()) != 0:
            qrImage = myQr.png(os.path.join(dir, name.get() + ".png"), Scale=6)
        else:
            messagebox.showinfo("Error!", "File name can be empty!")
    except:
        messagebox.showinfo("Error!", "Please generate the code first")

lab1 = Label(window, text="Enter Subject", font=("Halvetica", 12))
lab1.grid(row=0, column=0, sticky=N + S + E + W)

lab2 = Label(window, text="Enter Subject", font=("Halvetica", 12))
lab2.grid(row=1, column=0, sticky=N + S + E + W)

subject = StringVar()
subjectEntry = Entry(window, textvariable=subject, font=("Halvetica", 12))
subjectEntry.grid(row=0, column=1, sticky=N + S + E + W)

name = StringVar()
nameEntry = Entry(window, textvariable=subject, font=("Halvetica", 12))
nameEntry.grid(row=1, column=1, sticky=N + S + E + W)

createButton = Button(window, text="Crate QR Code", font=("Havlvetica", 12), width=15, command=generate)
createButton.grid(row=0, column=3, sticky=N + S + E + W)

notificationLabel = Label(window)
notificationLabel.grid(row=2, column=1, sticky=N + S + E + W)

subLabel = Label(window, text="")
subLabel.grid(row=3, column=1, sticky=N + S + E + W)

showButton = Button(window, text="Save PNG", font=("Halvetica", 12), width=15, command=save)
showButton.grid(row=1, column=3, sticky=N + S + E + W)

totalRows = 3
totalCols = 3
for row in range(totalRows + 1):
    window.grid_rowconfigure(row, weight = 1)
for col in range(totalCols + 1):
    window.grid_rowconfigure(col, weight = 1)
window.mainloop()
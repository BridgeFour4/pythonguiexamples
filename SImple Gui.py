#simple GUI
#demonstrates creating a widow

from tkinter import *

root = Tk()
#modify window
root.title("Simple Gui")
root.geometry("500x400")
root.configure(bg = "green")
root.iconbitmap("MineCraft.ico")
#root.attributes('-alpha', 0.5)

app = Frame(root,bg="blue")
app.grid(rows=3,columns=3)

l = Label(app, text="this is the top label", bg="#00ffff", font=("Times", "24", "bold italic"), fg="green" )
l.grid(row=1,column=3)
label = Label(app, text="this is a fancy label", bg="red", font=("wingdings", "16"), fg="green")
label.grid(row=2,column=2)
lb = Label(app, text="this is a lame label", bg="yellow", font=("Helvetica", "16","bold"), fg="green")
lb.grid(row=1,column=1)
#kick off window's event loop
root.mainloop()


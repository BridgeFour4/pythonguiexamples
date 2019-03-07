from tkinter import *

root = Tk()
root.title("Lazy Buttons")
root.geometry("200x85")
root.configure(bg="cornflowerblue")

app=Frame(root)
app.grid()
app.configure(bg="cornflowerblue")


bttn= Button(app,text="I do nothing",bg="green")
bttn.grid()
bttn2= Button(app,bg="blue")
bttn2.configure(text="Don't click me",fg="red")
font1=("wingdings")
bttn2.configure(font=font1)
bttn2.grid()
bttn3= Button(app,text="I do nothing",bg="red")
bttn3.grid()
bttn3["text"]="Same here"


root.mainloop()
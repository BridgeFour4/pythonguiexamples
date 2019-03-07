from tkinter import *

class Application(Frame):
    def __init__(self,master):

        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.bttn = Button(self, text="I do nothing", bg="green")
        self.bttn.grid()

        self.bttn2 = Button(self, bg="blue")
        self.bttn2.configure(text="Don't click me", fg="red")
        self.font1 = ("wingdings")
        self.bttn2.configure(font=self.font1)
        self.bttn2.grid()

        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "Same here"
        self.bttn3["bg"] = "red"
        self.bttn3["fg"] = "green"


root = Tk()
root.title("Lazy Buttons 2")
root.geometry("200x85")
app = Application(root)

root.mainloop()
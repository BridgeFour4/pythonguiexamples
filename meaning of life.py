from tkinter import *

class Application(Frame):
    def __init__(self,master):

        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.configure(bg="silver")
        self.labelone = Label(self,text= "Enter password for the secret life")
        self.labelone.grid(row=0, column=0,columnspan=2,sticky=W)
        self.labeltwo= Label(self, text="password:")
        self.labeltwo.grid(row=1, column=0, sticky=W)
        self.pw_ent =Entry(self,bg="black")
        self.pw_ent.grid(row=2, column=0, columnspan=2, sticky=W)

        self.buttonsubmit = Button(self, text="Submit", command=self.reveal)
        self.buttonsubmit.grid(row=2, column=1,columnspan=2, sticky=EW)

        self.secret_txt = Text(self, width=35, height=5, wrap=WORD,bg='orange',fg="white")
        self.secret_txt.grid(row=4, column=0, columnspan=3, sticky=E)


    def reveal(self):
        contents = self.pw_ent.get()
        if contents =="secret":
            message="42"
        else:
            message="That's not the correct password so I can't share the secret with you"
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)



root=Tk()
root.title("Click Counter")
root.geometry("300x200")
root.configure(bg="black")
app=Application(root)

root.mainloop()
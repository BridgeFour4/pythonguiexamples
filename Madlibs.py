from tkinter import *

class Application(Frame):
    def __init__(self,master):

        super(Application,self).__init__(master)
        self.grid()
        self.color=""
        self.create_widgets()
    def create_widgets(self):
        Label(self,text="LBL").grid(row=0,column=0)
        Label(self, text="name 1:").grid(row=1, column=0, sticky=W)
        self.entry_one =Entry(self)
        self.entry_one.grid(row=1, column=1, sticky=W)

        self.labeltwo = Label(self, text="gender 1")
        self.labeltwo.grid(row=2, column=0, sticky=W)
        self.entry_two = Entry(self)
        self.entry_two.grid(row=2, column=1, sticky=W)

        self.labelthree = Label(self, text="animal 1 plural")
        self.labelthree.grid(row=3, column=0, sticky=W)
        self.entry_three = Entry(self)
        self.entry_three.grid(row=3, column=1,sticky=W)

        self.labelfour = Label(self, text="Color")
        self.labelfour.grid(row=4, column=0, sticky=W)
        self.favorite_color = StringVar()
        self.favorite_color.set(None)
        Radiobutton(self, text="Red", variable=self.favorite_color,
                    value="Red").grid(row=4, column=1, sticky=W)
        Radiobutton(self, text="Green", variable=self.favorite_color,
                    value="Green").grid(row=4, column=2, sticky=W)
        Radiobutton(self, text="Blue", variable=self.favorite_color,
                    value="Blue").grid(row=4, column=3, sticky=W)

        self.labelfive = Label(self, text="Animal two plural")
        self.labelfive.grid(row=5, column=0, sticky=W)
        self.entry_five = Entry(self)
        self.entry_five.grid(row=5, column=1, sticky=W)

        self.labelsix = Label(self, text="first name 2")
        self.labelsix.grid(row=6, column=0, sticky=W)
        self.entry_six= Entry(self)
        self.entry_six.grid(row=6, column=1, sticky=W)

        self.labelseven = Label(self, text="gender 2")
        self.labelseven.grid(row=7, column=0, sticky=W)
        self.entry_seven = Entry(self)
        self.entry_seven.grid(row=7, column=1, sticky=W)

        self.labeleight = Label(self, text="emotion")
        self.labeleight.grid(row=8, column=0, sticky=W)

        self.angry=BooleanVar()
        Checkbutton(self, text="Angry",var=self.angry,
                   ).grid(row=8,column=1, sticky=W)

        self.Sad = BooleanVar()
        Checkbutton(self, text="Sad", var=self.Sad,
                    ).grid(row=8, column=2,sticky=W)

        self.Happy = BooleanVar()
        Checkbutton(self, text="Happy", var=self.Happy,
                    ).grid(row=8, column=3, sticky=W)


        self.buttonsubmit = Button(self, text="Submit story",command=self.tell_story)
        self.buttonsubmit.grid(row=9, column=0,columnspan=2, sticky=EW)

        self.secret_txt = Text(self, width=35, height=5, wrap=WORD)
        self.secret_txt.grid(row=10, column=0, columnspan=3, sticky=E)
    def tell_story(self):
        person1=self.entry_one.get()
        gender1 = self.entry_two.get()
        animal1 = self.entry_three.get()
        color = self.favorite_color.get()
        animal2 = self.entry_five.get()
        name2 = self.entry_six.get()
        animal1 = self.entry_six.get()
        gender2= self.entry_seven.get()
        emotions=""
        if self.angry.get():
            emotions+="angry,"
        if self.Sad.get():
            emotions+="Sad,"
        if self.Happy.get():
            emotions+="Happy"
        story=""+person1+" was walking in the park one day, humming to "+gender1,"self. the day was bright the sun was shining, and the"+animal1+"were singing"+"Suddenly, two "+color+animal2+" ran by.\n"+"Run! Run! they cried "+name2+'is coming and'+gender2+"'s really "+emotions

        self.secret_txt.delete(0.0,END)
        self.secret_txt.insert(0.0, story)








root=Tk()
root.title("Click Counter")
root.geometry("400x300")
app=Application(root)

root.mainloop()
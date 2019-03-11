from tkinter import *

class Application(Frame):
    def __init__(self,master):

        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,text= "Choose your favorite movie types").grid(row=0, column=0,sticky=W)
        Label(self, text="Select all that apply").grid(row=1, column=0, sticky=W)
        #self.likes_comedy=BooleanVar()
        #Checkbutton(self, text="Comedy",var=self.likes_comedy,
        #            command =self.update_text).grid(row=2,column=0, sticky=W)

        #self.likes_Romance = BooleanVar()
        #Checkbutton(self, text="Romance", var=self.likes_Romance,
        #            command=self.update_text).grid(row=3, column=0,sticky=W)

        #self.likes_drama = BooleanVar()
        #Checkbutton(self, text="Drama", var=self.likes_drama,
        #            command=self.update_text).grid(row=4, column=0, sticky=W)
        self.favorite = StringVar()
        self.favorite.set(None)
        Radiobutton(self,text="Comedy",variable=self.favorite,
                    value="Comedy",command=self.update_text).grid(row=2,column=0, sticky=W)
        Radiobutton(self, text="Romance", variable=self.favorite,
                    value="Romance", command=self.update_text).grid(row=3, column=0, sticky=W)
        Radiobutton(self, text="Drama", variable=self.favorite,
                    value="Drama", command=self.update_text).grid(row=4, column=0, sticky=W)

        self.movie_txt = Text(self, width=35, height=5, wrap=WORD)
        self.movie_txt.grid(row=5, column=0, columnspan=2, sticky=W)
    def update_text(self):
        message= "Your favorite movie type is  "
        message+=self.favorite.get()
        self.movie_txt.delete(0.0,END)
        self.movie_txt.insert(0.0, message)

        #likes=""
        #if self.likes_comedy.get():
        #    likes+="You like Comedic movies.\n"
        #if self.likes_Romance.get():
         #   likes+="You like Romantic movies.\n"
        #if self.likes_drama.get():
        #    likes+="You like Dramatic movies."
        #self.movie_txt.delete(0.0,END)
        #self.movie_txt.insert(0.0, likes)





root=Tk()
root.title("Movie picker")
root.geometry("300x200")
app=Application(root)

root.mainloop()
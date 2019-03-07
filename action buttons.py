from tkinter import *

class Application(Frame):
    def __init__(self,master):

        super(Application,self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widgets()

    def create_widgets(self):
        self.bttn = Button(self)
        self.bttn["text"]="Total Clicks 0"
        self.bttn["command"]=self.update_count
        self.bttn.grid()

    def update_count(self):
        self.bttn_clicks+=1
        self.bttn["text"]="Total Clicks: "+str(self.bttn_clicks)

root=Tk()
root.title("Click Counter")
root.geometry("200x50")
app=Application(root)

root.mainloop()
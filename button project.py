from tkinter import *
import random
class Application(Frame):
    def __init__(self,master):

        super(Application,self).__init__(master)
        self.grid()
        self.total = 0
        self.master=master
        self.colors=("green","red",'blue','yellow')
        self.create_widgets()

    def create_widgets(self):
        self.labeldisplay= Label(self,text="Count")
        self.labeldisplay.grid()
        self.labelcount= Label(self,text="0")
        self.labelcount.grid()
        self.bttnadd = Button(self,text="+",command=self.add_count)
        self.bttnadd.grid()
        self.bttnsub = Button(self, text="-", command=self.subtract_count)
        self.bttnsub.grid()
        self.bttntimes = Button(self, text="*", command=self.times_count)
        self.bttntimes.grid()
        self.bttndiv = Button(self, text="/", command=self.divide_count)
        self.bttndiv.grid()

    def add_count(self):
        self.total += 1
        self.labelcount["text"]= self.total
        randnum=random.randint(0,3)
        self.bttnadd['bg']=self.colors[randnum]
        self.master['bg']=self.colors[randnum]

    def subtract_count(self):
        self.total -= 1
        self.labelcount["text"] = self.total
        randnum = random.randint(0, 3)
        self.bttnsub['bg'] = self.colors[randnum]
        self.master['bg'] = self.colors[randnum]

    def times_count(self):
        self.total *= 2
        self.labelcount["text"] = self.total
        randnum = random.randint(0, 3)
        self.bttntimes['bg'] = self.colors[randnum]
        self.master['bg'] = self.colors[randnum]

    def divide_count(self):
        self.total=self.total // 2
        self.labelcount["text"]= self.total
        randnum = random.randint(0, 3)
        self.bttndiv['bg'] = self.colors[randnum]
        self.master['bg'] = self.colors[randnum]


root=Tk()
root.title("Click Counter")
root.geometry("100x200")
app=Application(root)

root.mainloop()
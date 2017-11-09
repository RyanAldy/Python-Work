from tkinter import *

class Application(Frame):

    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):

        self.textbox = Entry(self)
        self.textbox.delete(0, END)
        self.textbox.insert(0, "Hello there")
        self.textbox.pack()

        self.textbox_two = Entry(self)
        self.textbox_two.delete(0, END)
        self.textbox_two.insert(0, "Another text box!")
        self.textbox_two.pack()


        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]  = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack()

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack()


        self.labelone = Label(self, text="This is a label")
        self.labelone.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
root.geometry('300x300')
app.mainloop()
#root.destroy()

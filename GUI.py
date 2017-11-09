# TKinter to create a GUI application

from Tkinter import *

class application:

    def __init__(self, main_frame):

        main_frame = Frame(main_frame)
        main_frame.pack()

        self.button = Button(main_frame, text = "this is a button", fg = "red,",
        command=frame.quit)
        self.button.pack(side=CENTER)

        #self.


        #e = Entry(main_frame)
        #e.pack()

        #e2 = Entry(main_frame)
        #e2.pack()

        #btn = Button(main_frame, text="Hello", width=10, command=callback)
        #btn.pack()

        #lbl = Label(main_frame, text = "This is a label")


root = tk()

app = application(root)

root.mainloop()

import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()

        self.frame = tkinter.LabelFrame()
        self.frame.configure(text = "This is a label frame")
        self.frame.pack(fill="both", expand = 1)

        for i in range(1, 11):
            checkbutton = tkinter.Checkbutton(self.frame)
            checkbutton.configure(text = i)
            checkbutton.pack()

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()

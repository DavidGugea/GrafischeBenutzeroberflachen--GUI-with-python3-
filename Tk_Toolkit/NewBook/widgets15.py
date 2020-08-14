import tkinter


class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()

        s = tkinter.Spinbox(master)
        s.values = ("A", "B", "C")
        s.pack()


root = tkinter.Tk()
app = MyApp(root)
app.mainloop()

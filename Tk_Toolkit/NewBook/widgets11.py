import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__()
        self.pack()

        self.mb = tkinter.Menubutton(self, text = "Hello World")
        self.menu = tkinter.Menu(self.mb, tearoff = False)
        self.menu.add_checkbutton(label = "A")
        self.menu.add_checkbutton(label = "B")
        self.menu.add_checkbutton(label = "C")

        self.mb.configure(menu = self.menu)
        self.mb.pack()

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()

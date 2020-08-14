import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        
        self.mb = tkinter.Menubutton(master, text = "Text A")
        self.menu = tkinter.Menu(self.mb, tearoff=True)
        
        self.menu.add_checkbutton(label = "Text B")
        self.menu.add_checkbutton(label = "Text C")
        self.menu.add_checkbutton(label = "Text D")

        self.mb.configure(menu = self.menu)
        self.mb.pack()

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()

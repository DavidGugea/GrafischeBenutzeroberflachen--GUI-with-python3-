import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()

        self.entryVar = tkinter.StringVar()
        self.entryVar.set("Hallo Welt")
        
        self.entry = tkinter.Entry(self)
        self.entry.configure(textvariable = self.entryVar)
        self.entry.bind("<Return>", self.handler)
        self.entry.pack()

        self.label = tkinter.Label()
        self.label.configure(text = self.entryVar.get())
        self.label.pack()

    def handler(self, e):
        self.label.configure(self.entryVar.get())

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()

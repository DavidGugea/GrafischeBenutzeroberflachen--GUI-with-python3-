import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__()
        self.pack()

        self.lst = ["Linux", "macOS", "Windows"]

        self.var = tkinter.StringVar()
        self.var.set("Linux")
    
        self.op = tkinter.OptionMenu(self, self.var, *self.lst, command=self.handler)
        self.op.pack()

    def handler(self, text):
        print(text, self.var.get())

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()

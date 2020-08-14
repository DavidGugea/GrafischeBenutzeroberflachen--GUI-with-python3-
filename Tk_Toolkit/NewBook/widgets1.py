import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()

        self.ok = tkinter.Button(self)
        self.ok.configure(text = "Beschriftung", command = self.handler)
        self.ok.pack()

    def handler(self):
        print("Button gedrückt")

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()

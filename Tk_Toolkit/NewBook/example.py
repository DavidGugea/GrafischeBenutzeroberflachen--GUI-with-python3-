import tkinter


class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master=None)

        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameEntry = tkinter.Entry(self)

        self.nameEntry.pack()

        self.name = tkinter.StringVar()
        self.name.set("Ihr Name ... ")

        self.nameEntry.configure(textvariable=self.name)

        self.ok = tkinter.Button(self)
        self.ok.configure(text = "Ok", command = self.quit)
        self.ok.pack(side = "right")

        self.rev = tkinter.Button(self)
        self.rev.configure(text="Umdrehen", command=self.onReverse)
        self.rev.pack(side="right")
    def onReverse(self):
        self.name.set(self.name.get()[::-1])

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
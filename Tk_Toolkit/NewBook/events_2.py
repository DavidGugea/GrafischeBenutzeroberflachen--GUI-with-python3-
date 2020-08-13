import tkinter

class app(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack()
        self.makeEntryAndLabel()
        self.addCharBindings()

    def makeEntryAndLabel(self):
        self.entry = tkinter.Entry(self)
        self.entry.pack(fill="x", expand = 1)

        self.label = tkinter.Label(self)
        self.label.configure(text = "You pressed : ")
        self.label.pack()

    def addCharBindings(self):
        self.entry.bind("<KeyPress>", self.keypressed)

    def keypressed(self, e):
        self.label.configure(text = "You've pressed : {0} ( {1} - {2} )".format(
            e.char,
            e.keycode,
            e.keysym
        ))

root = tkinter.Tk()
App = app(root)
App.mainloop()

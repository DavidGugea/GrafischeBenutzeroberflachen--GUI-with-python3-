import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack()
        self.createWidgets()
        self.createBindings()

    def createWidgets(self):
        self.label = tkinter.Label(self)
        self.label.configure(text = "Bitte sende ein Event")
        self.label.pack()
        
        self.entry = tkinter.Entry(self)
        self.entry.pack()

        self.ok = tkinter.Button(self)
        self.ok.configure(text = "Beenden", command = self.quit)
        self.ok.pack()

    def createBindings(self):
        self.entry.bind("Entenhausen", self.eventEntenhausen)
        self.entry.bind("<ButtonPress-1>", self.eventMouseClick)
        self.entry.bind("<MouseWheel>", self.eventMouseWheel)

    def eventEntenhausen(self, event):
        self.label.configure(text = "Passwort erkannt")

    def eventMouseClick(self, event):
        self.label.configure(text = "Mausklick an Position ( {0} {1} )".format(event.x, event.y))

    def eventMouseWheel(self, event):
        if event.delta < 0:
            self.label.configure(text = "Bitte bewegen Sie das Mausrad in die richtige Richtung.")
        else:
            self.label.configure(text = "Vielen Dank.")

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()

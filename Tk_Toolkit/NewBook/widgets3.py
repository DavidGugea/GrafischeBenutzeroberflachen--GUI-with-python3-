import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()

        self.auswahl = [
                "Berlin", "London", "Moskau", "Ottawa",
                "Paris", "Rom", "Tokio", "Washington DC"
        ]

        self.stadt = tkinter.StringVar()
        self.stadt.set("Moskau")
        
        self.label = tkinter.Label() 
        self.label.configure(text = self.stadt.get())
        self.label.pack()
       
        for a in self.auswahl:
            b = tkinter.Radiobutton(self)
            b.configure(text = a, value = a, variable = self.stadt, command = self.handler)
            b.pack(anchor = "w")

    def handler(self):
        self.label.configure(text = self.stadt.get())

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()

import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()

        self.eintraege = [
                "Berlin", "London", "Moskau", "Ottawa",
                "Paris", "Rom", "Tokio", "Washington DC"
        ]

        self.lb = tkinter.Listbox(master)
        self.lb.insert("end", *self.eintraege)
        self.lb.pack()

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()

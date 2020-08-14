import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__()
        self.pack()

        self.names = ("Donald Duck", "Dagobert Duck", "Gustav Gans")

        self.group = tkinter.LabelFrame(self)
        self.group.configure(text = "Entenhausen")
        self.group.pack()

        self.checks = list()
        self.vars = list()

        for name in self.names:
            var = tkinter.BooleanVar()
            var.set(False)
            
            check = tkinter.Checkbutton(self.group)
            check.configure(text = name, command = self.handler, variable = var)
            check.pack(anchor = "w")
            
            self.checks.append(check)
            self.vars.append(var)
    
        self.label = tkinter.Label()
        self.label.pack()

    def handler(self):
        self.label.configure(text = " und ".join([name for name, var in zip(self.names, self.vars) if var.get()]))

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()

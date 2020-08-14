import tkinter


class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__()
        self.pack()

        self.listbox = tkinter.Listbox(self)
        self.listbox.pack(side="left")

        self.scrollbar = tkinter.Scrollbar(self)
        self.scrollbar.pack(fill = "y", side="left")

        self.listbox.insert("end", *[pow(i, 2) for i in range(50)])

        self.listbox.configure(yscrollcommand = self.scrollbar) 
        self.scrollbar.configure(command = self.listbox.yview)

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()

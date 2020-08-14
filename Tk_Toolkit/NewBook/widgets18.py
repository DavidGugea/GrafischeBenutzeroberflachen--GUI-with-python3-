import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        
        self.text = tkinter.Text(master)
        self.scrollbar = tkinter.Scrollbar(master)
        
        self.scrollbar.configure(command = self.text.yview)
        self.text.configure(yscrollcommand = self.scrollbar) 

        self.text.tag_config("b", foreground = "blue")
        self.text.tag_config("u", underline = True)

        self.text.pack(side="left")
        self.scrollbar.pack(side="left", fill="y")

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        
        self.text = tkinter.Text(master)
        self.text.pack()

        self.text.tag_config("o", foreground = "orange")
        self.text.tag_config("u", underline = True)

        self.text.insert("end", "Hello world\n")
        self.text.insert("end", "This is a long, orange text, hopefully\n", "o")
        self.text.insert("end", "This is hopefully underlined.\n", "u")

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
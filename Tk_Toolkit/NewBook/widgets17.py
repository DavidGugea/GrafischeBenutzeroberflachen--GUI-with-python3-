import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack() 

        self.text = tkinter.Text(master)
        
        self.text.tag_config("r", foreground = "red")
        self.text.tag_config("u", underline = True)

        self.text.insert("end", "This is a normal piece of text.\n")
        self.text.insert("end", "This is hopefully a red piece of text.\n", "r")
        self.text.insert("end", "This is hopefully an underlined piece of text.\n", "u")

        self.text.bind("<KeyRelease>", self.keyrelease)

        self.text.pack()

    def keyrelease(self, event):
        print("Text : {0}".format(self.text.get("1.0", "end")))

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__()
        self.pack()
        self.master = master

        self.fullMenuBar = tkinter.Menu(master)
        master.configure(menu = self.fullMenuBar)

        self.frame = tkinter.Frame(master, width=200, height = 200)
        self.frame.pack()

        self.addMenus()

    def addMenus(self):
        self.fileMenu = tkinter.Menu(self.fullMenuBar)

        self.fileMenu.add_command(label = "Button 1")
        self.fileMenu.add_command(label = "Button 2")
        self.fileMenu.add_command(label = "Button 3")

        self.fileMenu.add_separator()

        self.color_var = tkinter.StringVar()

        self.fileMenu.add_radiobutton(label="Red", command = self.color_handler, variable = self.color_var, value="red")
        self.fileMenu.add_radiobutton(label="Yellow", command = self.color_handler, variable = self.color_var, value= "yellow")
        self.fileMenu.add_radiobutton(label="Blue", command = self.color_handler, variable = self.color_var, value="blue")

        self.fullMenuBar.add_cascade(label = "File", menu=self.fileMenu)

    def color_handler(self):
        self.frame.configure(bg=self.color_var.get())

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()

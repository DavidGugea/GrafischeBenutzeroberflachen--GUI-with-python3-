import tkinter 

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        
        self.canvas = tkinter.Canvas(master, width = 200, height = 200)
        self.canvas.pack()
        
        self.canvas.create_oval(10, 10, 190, 90, fill="red", width=3)

        self.b = tkinter.Button(None, text = "Selbstzerstörung", background = "red", activebackground = "red", foreground = "white", activeforeground = "white")

        self.canvas.create_window(100, 50, window = self.b)

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
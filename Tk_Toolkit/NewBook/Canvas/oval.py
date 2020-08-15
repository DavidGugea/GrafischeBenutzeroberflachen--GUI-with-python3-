import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__()
        self.pack()
        
        self.canvas = tkinter.Canvas(master, width = 300, height = 300)
        self.canvas.pack()
        
        self.canvas.create_oval(100, 30, 200, 80, width = 3)

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        
        self.canvas = tkinter.Canvas(master, width = 300, height = 300)
        self.canvas.pack()
        
        self.canvas.create_rectangle(50, 50, 200, 100)

        
root = tkinter.Tk()
app = MyApp(root)
app.mainloop()

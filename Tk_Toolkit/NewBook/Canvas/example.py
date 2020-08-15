import tkinter


class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        
        self.canvas = tkinter.Canvas(self, width = 200, height = 200)
        self.canvas.pack()
        
        self.canvas.create_oval(50, 50, 150, 150, fill="orange", width=3)
        self.canvas.create_line(50, 150, 150, 50, width = 3) 

        self.canvas.create_line(50, 50, 150, 150, width = 3) 

        
root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
import tkinter 

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        
        self.canvas = tkinter.Canvas(self, width = 300, height = 300) 
        self.canvas.pack()
        
        points = (10, 10,
                  90, 50,
                  10, 90
        )

        self.canvas.create_polygon(*points, width = 3, fill = "orange", outline = "black")

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
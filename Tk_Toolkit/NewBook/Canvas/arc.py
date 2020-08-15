import tkinter 

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        
        self.canvas = tkinter.Canvas(master)
        self.canvas.create_arc(
            20, 100,
            40, 300
        )
        self.canvas.create_arc(
            20, 100,
            40, 200
        )

        self.canvas.pack()

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
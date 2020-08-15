import tkinter 

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        
        self.canvas = tkinter.Canvas(self, width = 200, height = 200)
        self.canvas.pack()
        
        self.font1 = ("Arial", 12, "italic")
        self.font2 = ("Courier New", 12, "bold italic")
        self.font3 = ("Comic Sans MS", 12, "bold")

        self.canvas.create_text(55, 30, text = "Python ", font = self.font1)
        self.canvas.create_text(55, 50, text = "Python ", font = self.font2)
        self.canvas.create_text(55, 70, text = "Python ", font = self.font3)
        
root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
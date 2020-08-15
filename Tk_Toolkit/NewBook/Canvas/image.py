import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        
        self.cv = tkinter.Canvas(self, width = 200, height = 200)
        self.cv.pack()
        
        self.img = tkinter.PhotoImage(file="tiny_icon.png")
        self.cv.create_image(50, 50, image = self.img)

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
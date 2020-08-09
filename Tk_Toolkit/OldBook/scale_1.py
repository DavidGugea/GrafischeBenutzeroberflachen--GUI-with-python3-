import tkinter

def end(): main.destroy()
def show(self): lb.configure(text = "Speed : {0} km/h".format(scale_value.get()))

main = tkinter.Tk()

lb = tkinter.Label(main, text = "Speed: 0 km/h", width = 25)
lb.pack()

scale_value = tkinter.IntVar()
scale_value.set(0)

scale = tkinter.Scale(main, width = 20, length = 200, orient="vertical", from_ = 0, to = 200, tickinterval = 20, resolution = 5, label = "km/h", command = show, variable = scale_value)
scale.pack()

tkinter.Button(main, text = "Close", command = end).pack()

main.mainloop()

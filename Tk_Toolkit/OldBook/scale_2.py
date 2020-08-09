import tkinter

main = tkinter.Tk()

def end(): main.destroy()
def show(self): lb.configure(text = "Speed : {0} km/h".format(scale_value.get()))

scale_value = tkinter.IntVar()
scale_value.set(0)

lb = tkinter.Label(main, text = "Speed : 0 km/h", width = 25)
lb.pack()

scale = tkinter.Scale(
        main,
        from_ = 0,
        to = 200,
        resolution = 5,
        tickinterval = 20,
        width = 20, length = 200,
        label = "km/h",
        variable = scale_value, orient="vertical",
        command = show
)
scale.pack()

tkinter.Button(main, text = "Close", command = end).pack()

main.mainloop()

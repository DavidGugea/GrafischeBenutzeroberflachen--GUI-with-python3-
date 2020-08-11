import tkinter

main = tkinter.Tk()

def end():
    main.destroy()

def change_color():
    fr["bg"] = color.get()

def change_relief():
    if relief.get():
        fr["relief"] = "ridge"
    else:
        fr["relief"] = "flat"

fr = tkinter.Frame(main, height = 100, width = 300, bg = "#FFFFFF", bd = 10)
fr.pack()

mBar = tkinter.Menu(main)
mFile = tkinter.Menu(mBar)
mFile.add_command(label = "New")
mFile.add_command(label = "Load")
mFile.add_command(label = "Save")
mFile.add_separator()
mFile.add_command(label = "Close", command = end)

color = tkinter.StringVar()
color.set("#FFFFFF")
relief = tkinter.IntVar()
relief.set(0)

mView = tkinter.Menu(mBar)
mView.configure(tearoff = 0)

mView.add_radiobutton(label = "Red", variable = color, value = "#FF0000", underline = 0, command = change_color)
mView.add_radiobutton(label = "Yellow", variable = color, value = "#FFFF00", underline = 0, command = change_color)
mView.add_radiobutton(label = "Blue", variable = color, value = "#0000FF", underline = 0, command = change_color)
mView.add_radiobutton(label = "Magenta", variable = color, value = "#FF00FF", underline = 0, command = change_color)
mView.add_separator()
mView.add_checkbutton(label = "See relief", variable = relief, onvalue = 1, offvalue = 0, underline = 5, command = change_relief)

mBar.add_cascade(label="File", menu = mFile)
mBar.add_cascade(label="View", menu = mView)
main.configure(menu = mBar)

main.mainloop()

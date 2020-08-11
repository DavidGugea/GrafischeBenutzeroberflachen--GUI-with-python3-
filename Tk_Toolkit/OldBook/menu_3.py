import tkinter

main = tkinter.Tk()

def end():
    main.destroy()

def change_bg():
    frame.configure(bg = color.get())

def change_relief():
    if relief.get():
        frame.configure(relief = "ridge")
    else:
        frame.configure(relief = "flat")

frame = tkinter.Frame(main, width = 200, height = 200, bg = "#FFFFFF", bd = 10)
frame.pack(fill="both", expand = 1)

menu = tkinter.Menu(main)

fileMenu = tkinter.Menu(menu)
fileMenu.add_command(label = "New")
fileMenu.add_command(label = "Save")
fileMenu.add_command(label = "Load")
fileMenu.add_separator()
fileMenu.add_command(label = "Close", command=end)

color = tkinter.StringVar()
color.set("#FFFFFF")
relief = tkinter.IntVar()
relief.set(0)

viewMenu = tkinter.Menu(menu)
viewMenu.configure(tearoff = 0)
viewMenu.add_radiobutton(label = "Red", variable = color, value = "red", command = change_bg)
viewMenu.add_radiobutton(label = "Yellow", variable = color, value = "yellow", command = change_bg)
viewMenu.add_radiobutton(label = "Blue", variable = color, value = "blue", command = change_bg)
viewMenu.add_separator()
viewMenu.add_checkbutton(label = "Relief visible", variable = relief, onvalue = 1, offvalue = 0, command = change_relief)

menu.add_cascade(label="File", menu = fileMenu)
menu.add_cascade(label="View", menu = viewMenu)

main.configure(menu = menu)

main.mainloop()

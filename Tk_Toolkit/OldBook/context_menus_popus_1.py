import tkinter

main = tkinter.Tk()

def end(): main.destroy()

def lbpop(e):
    mpop.tk_popup(e.x_root, e.y_root)

def change_color():
    lb.configure(bg = color.get())

frame = tkinter.Frame(main, height = 200, width = 300)
frame.pack()

im = tkinter.PhotoImage(file = "tiny_icon.png")
lb = tkinter.Label(main, image = im, relief="ridge", bd=5, bg="#000000")
lb.bind("<Button 3>", lbpop)
lb.place(relx = 0, rely = 0, anchor = "nw")

color = tkinter.StringVar()
color.set("#000000")

mpop = tkinter.Menu(main)
mpop.configure(tearoff = 0)
mpop.add_radiobutton(label = "red", variable = color, value = "red", command = change_color)
mpop.add_radiobutton(label = "blue", variable = color, value = "blue", command = change_color)
mpop.add_radiobutton(label = "yellow", variable = color, value = "yellow", command = change_color)

tkinter.Button(main, text = "Close", command = end).pack()

main.mainloop()

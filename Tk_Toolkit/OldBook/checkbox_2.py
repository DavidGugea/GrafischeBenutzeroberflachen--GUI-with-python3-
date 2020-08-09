import tkinter

main = tkinter.Tk()

def end(): main.destroy()
def show_option(): lb.configure(text = "Room {0} {1}".format(shower.get(), desk.get()))

lb = tkinter.Label(main, text = "Room ")
lb.pack()

shower = tkinter.StringVar()
shower.set("with shower")
desk = tkinter.StringVar()
desk.set("with desk")

shower_checkbutton = tkinter.Checkbutton(main, variable = shower, text = "Shower", onvalue = "with shower", offvalue = "without shower", command = show_option)
shower_checkbutton.pack()
desk_checkbutton = tkinter.Checkbutton(main, variable = desk, text = "Desk", onvalue = "with desk", offvalue = "without desk", command = show_option)
desk_checkbutton.pack()

tkinter.Button(main, text = "Close", command = end).pack()

main.mainloop()

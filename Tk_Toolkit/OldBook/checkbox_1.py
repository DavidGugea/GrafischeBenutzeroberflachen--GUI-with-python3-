import tkinter

main = tkinter.Tk()

def end(): main.destroy()
def show(): lb.configure(text = "Room {0} {1}".format(desk.get(), shower.get()))

lb = tkinter.Label(main, text = "Room ", width = 40)
lb.pack()

desk = tkinter.StringVar()
desk.set("no desk")
shower = tkinter.StringVar()
shower.set("no shower")

shower_checkbutton = tkinter.Checkbutton(main, text = "Shower", variable = shower, onvalue = "with shower", offvalue = "without shower", command = show)
shower_checkbutton.pack()
desk_checkbutton = tkinter.Checkbutton(main, text = "Desk", variable = desk, onvalue = "with desk", offvalue = "without desk", command = show)
desk_checkbutton.pack()

close_button = tkinter.Button(main, text = "End", command = end)
close_button.pack()

main.mainloop()

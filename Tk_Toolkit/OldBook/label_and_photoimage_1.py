import tkinter

main = tkinter.Tk()

def end():
    main.destroy()

lb1 = tkinter.Label(main, text = "groove")
lb1["font"] = "Courier 16 italic"
lb1["height"] = 2
lb1["width"] = 10
lb1["borderwidth"] = 5
lb1["relief"] = "groove",
lb1["bg"] = "#FFFFFF",
lb1["fg"] = "#000000",
lb1["anchor"] = "w"
lb1.pack()

b = tkinter.Button(main, text = "End", command = end)
b.pack()

lb2 = tkinter.Label(main, text = "ridge")
lb2["font"] = "Arial 11 bold"
lb2["height"] = 2
lb2["width"] = 20
lb2["borderwidth"] = 5
lb2["relief"] = "ridge"
lb2["bg"] = "#FFFFFF"
lb2["fg"] = "#000000"
lb2["anchor"] = "e"
lb2.pack()

lb3 = tkinter.Label(main)
im = tkinter.PhotoImage(file="tiny_icon.png")
lb3["image"] = im
lb3.pack()

main.mainloop()

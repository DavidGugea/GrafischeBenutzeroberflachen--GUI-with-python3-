import tkinter

main = tkinter.Tk()

def end():
    main.destroy()

lb1 = tkinter.Label(main, text="Text 1")
lb1["font"] = "Courier 16 italic"
lb1.pack()

lb2 = tkinter.Label(main)
im = tkinter.PhotoImage(file="tiny_icon.png")
lb2["image"] = im
lb2.pack()

main.mainloop()

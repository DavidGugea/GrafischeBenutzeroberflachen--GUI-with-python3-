import tkinter

def window():
    global new
    new = tkinter.Toplevel(main)
    tkinter.Button(new, text = "End new", command = endnew).pack()

def endnew():
    new.destroy()

def end():
    main.destroy()

main = tkinter.Tk()
tkinter.Button(main, text = "New", command = window).pack()
tkinter.Button(main, text = "End", command = end).pack()

main.mainloop()

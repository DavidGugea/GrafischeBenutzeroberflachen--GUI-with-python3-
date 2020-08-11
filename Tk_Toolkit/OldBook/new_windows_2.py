import tkinter
main = tkinter.Tk()

def close():
    main.destroy()

def create_new_window():
    global new_window
    new_window = tkinter.Toplevel(main)

    tkinter.Button(new_window, text = "Close this window", command = close_new_window).pack()

def close_new_window():
    new_window.destroy()

tkinter.Button(main, text = "New window", command = create_new_window).pack()
tkinter.Button(main, text = "Close", command = close).pack()

main.mainloop()

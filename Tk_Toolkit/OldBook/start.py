import tkinter

main = tkinter.Tk()

def ende():
    main.destroy()

b = tkinter.Button(main, text = "Ende", command = ende)
b.pack()

main.mainloop()

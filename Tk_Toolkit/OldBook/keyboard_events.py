import tkinter

main = tkinter.Tk()

def end(): main.destroy()
def kev(e):
    lb.configure(text = "Sign: {0} | Description : {1} | Code : {2}".format(e.char, e.keysym, e.keycode))

e = tkinter.Entry(main)
e.bind("<p>", kev)
e.bind("<+>", kev)
e.bind("<%>", kev)
e.bind("<,>", kev)
e.pack()

lbhlp = tkinter.Label(main, text = "Key: p or + or % or ,", width = 40)
lbhlp.pack()

lb = tkinter.Label(main)
lb.pack()
tkinter.Button(main, text = "Close", command = end).pack()

main.mainloop()

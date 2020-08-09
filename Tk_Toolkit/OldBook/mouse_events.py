import tkinter

main = tkinter.Tk()

def end(): main.destroy()

def mleft(e):
    lb.configure(text = "Left Mouseclick")

def mright(e):
    lb.configure(text = "Right Mouseclick")

def mctrlleft(e):
    lb.configure(text = "Ctrl & left mouseclick")
    
def maltleft(e):
    lb.configure(text = "Alt & left mouseclick")

def mshiftleft(e):
    lb.configure(text = "Shift & left mouseclick")

def mleftclicklet(e):
    lb.configure(text = "Let go of left click")

def menter(e):
    lb.configure(text = "Entered")

def mleave(e):
    lb.configure(text = "Left")

def mmove(e):
    lb.configure(text = "Coords : x = {0} | y = {1}".format(e.x, e.y))

im = tkinter.PhotoImage(file = "tiny_icon.png")
lbm = tkinter.Label(main, image = im)
lbm.bind("<Button 1>", mleft)
lbm.bind("<Button 3>", mright)
lbm.bind("<Control-Button 1>", mctrlleft)
lbm.bind("<Alt-Button 1>", maltleft)
lbm.bind("<Shift-Button 1>", mshiftleft)
lbm.bind("<ButtonRelease 1>",  mleftclicklet)
lbm.bind("<Motion>", mmove)
lbm.pack()

lb = tkinter.Label(main, width = 35)
lb.pack()

close = tkinter.Button(main, text = "Close", command = end)
close.bind("<Enter>", menter)
close.bind("<Leave>", mleave)
close.pack()

main.mainloop()

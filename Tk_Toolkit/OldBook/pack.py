import tkinter

main = tkinter.Tk()

def end(): main.destroy()

fr1 = tkinter.Frame(main, width = 200, height = 100, relief="sunken", bd=1)
fr1.pack(side="left")

b1a = tkinter.Button(fr1, text = "Button 1a")
b1a.pack(padx = 5, pady = 5)
b2a = tkinter.Button(fr1, text = "Button 2a")
b2a.pack(padx = 5, pady = 5)

fr2 = tkinter.Frame(main, width = 200, height = 100, relief = "sunken", bd = 1)
fr2.pack(side="right")
b2a = tkinter.Button(fr2, text = "Button 2a")
b2a.pack(ipadx=25, ipady=25)
b2b =  tkinter.Button(fr2, text = "Button 2b")
b2b.pack(fill = "x")

fr3 = tkinter.Frame(main, width = 200, height = 100, relief = "sunken", bd = 1)
fr3.pack(side = "bottom", expand = 1, fill = "both")

close_button = tkinter.Button(main, text = "End", command = end)
close_button.pack()

main.mainloop()

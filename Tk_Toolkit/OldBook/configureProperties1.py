import tkinter 

main = tkinter.Tk()

def end():
    main.destroy()

# First type of configuring properties
b1 = tkinter.Button(main, text = "End", command = end)

# Second type
b2 = tkinter.Button(main)
b2["text"] = "Also end"
b2["command"] = end

# Third type
b3 = tkinter.Button(main)
b3.configure(text = "Also also end", command = end)

# Pack all of the buttons
b1.pack()
b2.pack()
b3.pack()

# Auto-pack buttons
b4 = tkinter.Button(main, text="Also*3 end", command = end).pack()
tkinter.Button(main, text="Also*4 end", command = end).pack()

main.mainloop()

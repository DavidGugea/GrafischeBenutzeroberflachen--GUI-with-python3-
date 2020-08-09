import tkinter

main = tkinter.Tk()

tkinter.Label(main, text = "<label 1>").grid(row = 0, column = 0)
tkinter.Label(main, text = "<label 1>").grid(row = 1, column = 0)

entry_1 = tkinter.Entry(main)
entry_1.insert("end", "<entry 1>")
entry_1.grid(row = 0, column = 1)

entry_2 = tkinter.Entry(main)
entry_2.insert("end", "<entry 2>")
entry_2.grid(row = 1, column = 1)

tkinter.Checkbutton(main, text = "<checkbutton>").grid(row=2, column=0, columnspan=2)

im = tkinter.PhotoImage(file = "tiny_icon.png")
tkinter.Label(main, image = im).grid(row=0, column = 2, columnspan=2, rowspan = 2)

tkinter.Button(main, text = "<button 1>").grid(row = 2, column = 2)
tkinter.Button(main, text = "<button 2>").grid(row = 2, column = 3)

main.mainloop()

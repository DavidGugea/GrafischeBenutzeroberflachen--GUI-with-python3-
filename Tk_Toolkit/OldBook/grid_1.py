import tkinter

main = tkinter.Tk()

tkinter.Label(main, text = "Height: ").grid(row = 0, column = 0)
tkinter.Label(main, text = "Width: ").grid(row = 1, column = 0)

tkinter.Entry(main).grid(row = 0, column = 1)
tkinter.Entry(main).grid(row = 1, column = 1)

tkinter.Checkbutton(main, text = "Test Checkbox Tkinter").grid(row=2, column=0, columnspan=2)

im = tkinter.PhotoImage(file = "tiny_icon.png")
tkinter.Label(main, image=im).grid(row=0, column=2, columnspan = 2, rowspan=2)

tkinter.Button(main, text = "Zoom in").grid(row=2, column = 2)
tkinter.Button(main, text = "Zoom out").grid(row=2, column = 3)

main.mainloop()

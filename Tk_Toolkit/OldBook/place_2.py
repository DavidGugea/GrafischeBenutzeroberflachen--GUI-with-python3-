import tkinter

main = tkinter.Tk()

tkinter.Button(main, text = "b1").place(relx=0.5, rely = 0)
tkinter.Button(main, text = "b2").place(relx=0, rely = 0.25)
tkinter.Button(main, text = "b3").place(relx=0, rely = 0.5)
tkinter.Button(main, text = "b4").place(relx=0, rely = 0.75)
tkinter.Button(main, text = "b5").place(relx=0.5, rely = 1, anchor="s")

main.mainloop()

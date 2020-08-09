import tkinter

main = tkinter.Tk()

def end(): main.destroy()
def show_option(): lb.configure(text = "Option : {0}".format(color.get()))

color = tkinter.StringVar()
color.set("red")

radioButton_1 = tkinter.Radiobutton(main, variable=color, command = show_option, text = "Red", value = "red")
radioButton_2 = tkinter.Radiobutton(main, variable=color, command = show_option, text = "Blue", value = "blue")
radioButton_3 = tkinter.Radiobutton(main, variable=color, command = show_option, text = "Yellow", value = "yellow")

radioButton_1.pack()
radioButton_2.pack()
radioButton_3.pack()

lb = tkinter.Label(main, text = "Option: ")
lb.pack()

tkinter.Button(main, text = "Close", command = end).pack()

main.mainloop()

import tkinter

main = tkinter.Tk()

def end(): main.destroy()
def show_option(): lb.configure(text = "Option : {0}".format(color.get()))

color = tkinter.StringVar()
color.set("color")

radioButton_1 = tkinter.Radiobutton(main, variable = color, text = "Red", value = "red")
radioButton_2 = tkinter.Radiobutton(main, variable = color, text = "Blue", value = "blue")
radioButton_3 = tkinter.Radiobutton(main, variable = color, text = "Yellow", value = "yellow")

radioButton_1.pack()
radioButton_2.pack()
radioButton_3.pack()

lb = tkinter.Label(main, text = "Option : ")
lb.pack()

show_button = tkinter.Button(main)
show_button.configure(text = "Show", command = show_option)
show_button.pack()

tkinter.Button(main, text = "Close", command = end).pack()

main.mainloop()

import tkinter

main = tkinter.Tk()

def end(): main.destroy()
def show_option(): lb.configure(text = "Option : {0}".format(color.get()))

color = tkinter.StringVar()
color.set("red")

radioButton_1 = tkinter.Radiobutton(main, text="red", variable=color, value = "red")
radioButton_1.pack()

radioButton_2 = tkinter.Radiobutton(main, text="yellow", variable = color, value = "yellow")
radioButton_2.pack()

radioButton_3 = tkinter.Radiobutton(main, text="blue", variable = color, value = "blue")
radioButton_3.pack()

show_button = tkinter.Button(main, text = "Show", command = show_option)
show_button.pack()

lb = tkinter.Label(main, text = "Option : ")
lb.pack()

tkinter.Button(main, text = "Close", command = end).pack()

main.mainloop()

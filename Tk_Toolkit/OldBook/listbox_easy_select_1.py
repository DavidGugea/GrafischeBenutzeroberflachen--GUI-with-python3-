import tkinter

main = tkinter.Tk()

def end():
    main.destroy()

def show_selection():
    lb.configure(text = "Selected option : {0}".format(li.get("active")))

li = tkinter.Listbox(main, height=0)
li.insert("end", "Hamburg")
li.insert("end", "Stuttgart")
li.insert("end", "Berlin")
li.insert("end", "Dortmund")
li.pack()

show_selection_button = tkinter.Button(main, text="Show selection", command=show_selection)
show_selection_button.pack()

lb = tkinter.Label(main, text="Selected option :")
lb.pack()

close_button = tkinter.Button(main, text="Close", command=end)
close_button.pack()

main.mainloop()

import tkinter

main = tkinter.Tk()

def end():
    main.destroy()

def show_options():
    lb.configure(text = "Selected options: ")
    for selected_option_index in li.curselection():
        lb["text"] += "{0} ".format(li.get(selected_option_index))

li = tkinter.Listbox(main, height = 0, selectmode = "multiple")
li.insert("end", "Hamburg")
li.insert("end", "Stuttgart")
li.insert("end", "Berlin")
li.insert("end", "Dortmund")
li.pack()

lb = tkinter.Label(main)
lb.configure(text = "Selected options: ")
lb.pack()

show_options_button = tkinter.Button(main)
show_options_button.configure(text = "Show options", command = show_options)
show_options_button.pack()

close_button = tkinter.Button(main)
close_button.configure(text = "Close", command = end)
close_button.pack()

main.mainloop()

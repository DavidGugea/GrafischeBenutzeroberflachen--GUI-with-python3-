import tkinter

main = tkinter.Tk()

def end():
    main.destroy()

def show_option():
    selected_option_label.configure(text = "Selected option : {0}".format(li.get("active")))

li = tkinter.Listbox(main, height = 0)
li.insert("end", "Hamburg")
li.insert("end", "Stuttgart")
li.insert("end", "Dortmund")
li.insert("end", "Berlin")
li.pack()

selected_option_label = tkinter.Label(main)
selected_option_label.configure(text = "Selected option: ")
selected_option_label.pack()

selected_option_button = tkinter.Button(main)
selected_option_button.configure(text = "Selected option", command = show_option)
selected_option_button.pack()

close_button = tkinter.Button(main)
close_button.configure(text = "Close", command = end)
close_button.pack()

main.mainloop()

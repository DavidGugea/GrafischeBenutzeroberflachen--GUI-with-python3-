import tkinter
import tkinter.scrolledtext

main = tkinter.Tk()

def end():
    main.destroy()

def pow_2():
    number = entry.get()
    try:
        number = eval(number)
        entry_result_label.configure(text = "Result: {0}".format(pow(number, 2)))
    except:
        entry_result_label.configure(text = "You must give a number")

def read_text():
    f = open("gui_text.txt", "r")
    line = f.readline()
    while line:
        scrolled_text.insert("end", line)
        normal_text.insert("end", line)
        line = f.readline()
    
    f.close()

def listbox_single_function():
    listbox_single_label.configure(text = "Your choice -- > {0}".format(listbox_single.get("active")))

def listbox_multiple_function():
    listbox_multiple_label.configure(text = "Your choices -- > ")
    for selection_index in listbox_multiple.curselection():
        listbox_multiple_label["text"] += "{0} - ".format(listbox_multiple.get(selection_index))

entry = tkinter.Entry(main)
entry.pack()

entry_result_label = tkinter.Label(main)
entry_result_label.configure(text = "Result: ", fg = "#ffffff", bg="#000000", width=70, height=15, font="Courier 16 bold")
entry_result_label.pack()

pow_2_button = tkinter.Button(main)
pow_2_button.configure(text = "Pow with 2", command = pow_2)
pow_2_button.pack()

scrolled_text = tkinter.scrolledtext.ScrolledText(main)
scrolled_text.configure(width = 35, height=10,fg="#ffffff", bg="#000000")
scrolled_text.pack()

normal_text = tkinter.Text(main)
normal_text.configure(width = 40, height=10,fg="#000000", bg="#ffffff")
normal_text.pack()

read_text_button = tkinter.Button(main)
read_text_button.configure(text = "Read text", command = read_text)
read_text_button.pack()

listbox_single = tkinter.Listbox(main, height=0)
listbox_single.insert(0, "Hamburg")
listbox_single.insert(0, "Stuttgart")
listbox_single.insert(0, "Dortmund")
listbox_single.insert(0, "Berlin")
listbox_single.pack()

listbox_single_label = tkinter.Label(main)
listbox_single_label.configure(text = "Your choice -- > ")
listbox_single_label.pack()
listbox_single_button = tkinter.Button(main)
listbox_single_button.configure(text = "See choice", command = listbox_single_function)
listbox_single_button.pack()

listbox_multiple = tkinter.Listbox(main, height=0, selectmode = "multiple")
listbox_multiple.insert(0, "Hamburg")
listbox_multiple.insert(0, "Stuttgart")
listbox_multiple.insert(0, "Dortmund")
listbox_multiple.insert(0, "Berlin")
listbox_multiple.pack()

listbox_multiple_label = tkinter.Label(main)
listbox_multiple_label.configure(text = "Your choices -- > ")
listbox_multiple_label.pack()
listbox_multiple_button = tkinter.Button(main)
listbox_multiple_button.configure(text = "See choices", command = listbox_multiple_function)
listbox_multiple_button.pack()

close_button = tkinter.Button(main)
close_button.configure(text = "Close", command = end)
close_button.pack()

main.mainloop()

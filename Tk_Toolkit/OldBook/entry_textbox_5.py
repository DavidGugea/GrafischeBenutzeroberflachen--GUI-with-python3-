import tkinter

main = tkinter.Tk()

def end():
    main.destroy()
    
def pow_2():
    number = entry.get()
    try:
        number = eval(number)
        entry_label.configure(text = "Result: {0}".format(pow(number, 2)))
    except:
        entry_label.configure(text = "You have to give a number")

def get_text():
    file_ = open("text_for_textbox.txt", "r")
    while True:
        line = file_.readline()
        if line:
            textbox.insert("end", line)
            continue
        else:
            break

entry = tkinter.Entry(main)
entry.pack()
entry_label = tkinter.Label(main)
entry_label.configure(font="Courier 16 bold", bg="#000000", fg="#ffffff", width=70, height = 10, text="Result: ")
entry_label.pack()

textbox = tkinter.Text(main, width=70, height=15)
textbox.pack()
textbox_label = tkinter.Label(main)
textbox_label.configure(font="Courier 16 bold", bg="#000000", fg="#ffffff", width=70, height = 10)
textbox_label.pack()

entry_button = tkinter.Button(main)
entry_button.configure(text = "Pow with 2", command = pow_2)
entry_button.pack()

textbox_button = tkinter.Button(main)
textbox_button.configure(text = "Get text", command = get_text)
textbox_button.pack()

close_button = tkinter.Button(main)
close_button.configure(text="Close program", command = end)
close_button.pack()

main.mainloop()

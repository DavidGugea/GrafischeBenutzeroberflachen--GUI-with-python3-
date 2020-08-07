import tkinter, tkinter.scrolledtext

main = tkinter.Tk()

def end():
    main.destroy()

def show_text():
    f = open("gui_text.txt", "r")
    line = f.readline()
    while line:
        scrolledtext_textbox.insert("end", line)
        line = f.readline()

    f.close()

scrolledtext_textbox = tkinter.scrolledtext.ScrolledText(main, width=70, height=3)
scrolledtext_textbox.pack()

show_button = tkinter.Button(main)
show_button.configure(text="Show", command = show_text)
show_button.pack()

close_button = tkinter.Button(main)
close_button.configure(text="Close", command = end)
close_button.pack()

main.mainloop()

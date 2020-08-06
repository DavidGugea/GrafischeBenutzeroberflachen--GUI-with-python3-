import tkinter

main = tkinter.Tk()

def end():
    main.destroy()

def show():
    text_file = open("text_for_textbox.txt")

    while True:
        line = text_file.readline()
        if line != str():
            t.insert("end", line)
        else:
            break
    
    text_file.close()

t = tkinter.Text(main, width=70, height = 10 )
t.pack()

show_button = tkinter.Button(main)
show_button.configure(text = "Show text", command = show)
show_button.pack()

close_button = tkinter.Button(main)
close_button.configure(text = "Close the program", command = end)
close_button.pack()

main.mainloop()

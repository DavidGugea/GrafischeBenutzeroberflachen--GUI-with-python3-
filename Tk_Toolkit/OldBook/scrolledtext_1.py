import tkinter, tkinter.scrolledtext

main = tkinter.Tk()

def end():
    main.destroy()

def show_text():
    f = open("gui_text.txt", "r")
    line = f.readline()
    while line:
        t.insert("end", line)
        line = f.readline()
        
    f.close()

t = tkinter.scrolledtext.ScrolledText(main, width=40, height=3)
t.pack()

show_button = tkinter.Button(main, text="Show", command=show_text)
show_button.pack()

close_button = tkinter.Button(main, text="Close", command=end)
close_button.pack()

main.mainloop()

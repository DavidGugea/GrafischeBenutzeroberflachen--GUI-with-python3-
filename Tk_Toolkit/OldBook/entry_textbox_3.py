import tkinter

main = tkinter.Tk()

def end():
    main.destroy()

def transform():
    textbox_text = t.get("1.0", "end")
    p.configure(text = textbox_text)

t = tkinter.Text(main, width=70, height=10)
t.pack()

show_button = tkinter.Button(main)
show_button.configure(text="Transform", command = transform)
show_button.pack()

p = tkinter.Label(main)
p.pack()

close_button = tkinter.Button(main)
close_button.configure(text = "Close the program", command = end)
close_button.pack()

main.mainloop()

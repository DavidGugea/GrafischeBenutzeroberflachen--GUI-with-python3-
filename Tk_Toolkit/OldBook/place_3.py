import tkinter

main = tkinter.Tk()

def move_left():
    lb.place(relx = 0, rely = 0, anchor="nw")

def move_right():
    lb.place(relx = 1, rely = 0, anchor="ne")

def close():
    main.destroy()

lb = tkinter.Label(main, text = "Label")
lb.place(relx=0.5, rely=0)

move_left_button = tkinter.Button(main, text = "Move left", command = move_left)
move_left_button.place(relx = 0, rely = 1, anchor="sw")

close_button = tkinter.Button(main, text = "Close", command = close)
close_button.place(relx = 0.5, rely = 1, anchor="s")

move_right_button = tkinter.Button(main, text = "Move right", command = move_right)
move_right_button.place(relx = 1, rely = 1, anchor="se")

main.mainloop()

import tkinter

main = tkinter.Tk()

global_relx = 0.5 
global_rely = 0

def move_left():
    global global_rely, global_relx

    if global_relx > 0 and global_relx - 0.05 >= 0:
        global_relx -= 0.05

        if global_relx == 0:
            lb.configure(anchor = "w")

        lb.place(rely = global_rely, relx = global_relx)

def move_right():
    global global_rely, global_relx

    if global_relx < 1 and global_relx + 0.05 <= 1:
        global_relx += 0.05

        if global_relx == 1:
            lb.configure(anchor = "e")

        lb.place(rely = global_rely, relx = global_relx)

def move_down():
    global global_rely, global_relx

    if global_rely < 1 and global_rely + 0.05 <= 1:
        global_rely += 0.05;

        if global_rely == 0 and global_relx != 0 and global_relx != 1:
            lb.configure(anchor = "s")
        elif global_rely == 0 and global_relx == 0:
            lb.configure(anchor = "sw")
        elif global_rely == 0 and global_relx == 1:
            lb.configure(anchor = "se")

    lb.place(rely = global_rely, relx = global_relx) 

def move_up():
    global global_rely, global_relx

    if global_rely > 0 and global_rely - 0.05 >= 0:
        global_rely -= 0.05
        if global_rely == 0 and global_relx != 0 and global_relx != 1:
            lb.configure(anchor = "n")
        elif global_rely == 0 and global_relx == 0:
            lb.configure(anchor = "nw")
        elif global_rely == 0 and global_relx == 1:
            lb.configure(anchor = "ne")

    lb.place(rely = global_rely, relx = global_relx) 


def start():
    lb.place(relx = 0, rely = 0, anchor = "nw")

def close():
    main.destroy()

display_frame = tkinter.Frame(main, relief="sunken", width = 500, height = 500).pack(side="top")
control_frame = tkinter.Frame(main, bg="#333", width = 500, height = 200).pack(side="bottom")

lb = tkinter.Label(display_frame, text = "<label>")
lb.configure(bg="#333", fg="#999", font = "Courier 16 bold")
lb.place(relx = global_relx, rely = global_rely, anchor = "n")

move_left_button = tkinter.Button(control_frame, text = "Move left", command = move_left)
move_left_button.place(relx = 0.25, rely = 0.85)

move_right_button = tkinter.Button(control_frame, text = "Move right", command = move_right)
move_right_button.place(relx = 0.60, rely = 0.85)

move_up_button = tkinter.Button(control_frame, text = "Move up", command = move_up)
move_up_button.place(relx = 0.435, rely = 0.75)

move_bottom_button = tkinter.Button(control_frame, text = "Move down", command = move_down)
move_bottom_button.place(relx = 0.415, rely = 0.95)

start_button = tkinter.Button(control_frame, text = "Start", command = start)
start_button.place(relx=0.450, rely=0.85)

close_button = tkinter.Button(control_frame, text = "Close", command = close)
close_button.place(relx=1, rely=1, anchor="se")

main.mainloop()

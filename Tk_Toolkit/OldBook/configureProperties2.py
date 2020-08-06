import tkinter

main = tkinter.Tk()

def end():
    main.destroy()

button1 = tkinter.Button(main, text="Button 1", command=end)
button1.pack()

button2 = tkinter.Button(main)
button2["text"] = "Button 2"
button2["command"] = "end"

button2.pack()

button3 = tkinter.Button(main)
button3.configure(text = "Button 3", command = end)
button3.pack()

button4 = tkinter.Button(main, text = "Button 4", command = end).pack()
tkinter.Button(main, text="Button 5", command = end).pack()

main.mainloop()

import tkinter

main = tkinter.Tk()

def end():
    main.destroy()

def pow_2():
    user_input = e.get()
    try:
        user_input = eval(user_input)
        lb["text"] = "Result: {0}".format(pow(user_input, 2))
    except:
        lb["text"] = "You must give a number"

e = tkinter.Entry(main, show="*")
e.pack()

button_pow_2 = tkinter.Button(main, text = "Pow number with 2", command = pow_2)
button_pow_2.pack()

lb = tkinter.Label(main, text = "Result: ")
lb["font"] = "Courier 16 bold"
lb["width"] = 50 
lb["borderwidth"] = 5
lb["height"] = 5 
lb["fg"] = "#FFFFFF"
lb["bg"] = "#000000"
lb.pack()

end_button = tkinter.Button(main, text = "Close the program")
end_button.configure(command = end)
end_button.pack()

main.mainloop()

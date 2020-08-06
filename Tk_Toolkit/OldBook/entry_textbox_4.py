import tkinter

main = tkinter.Tk()

def end():
    main.destroy()
    
def pow_2():
    number = e.get()

    try:
        number = eval(number)
        label.configure(text = "Result: {0}".format(pow(number, 2)))
    except:
        label.configure(text = "You must insert a number")


e = tkinter.Entry(main)
e.pack()

pow_2_button = tkinter.Button(main)
pow_2_button.configure(text = "Pow with 2", command = pow_2)
pow_2_button.pack()

close_button = tkinter.Button(main)
close_button.configure(text = "Close the program", command = end)
close_button.pack()

label = tkinter.Label(main)
label.configure(text = "Result:", font = "Courier 16 bold", width = 70, height = 10, fg="#ffffff", bg="#000000")
label.pack()

main.mainloop()

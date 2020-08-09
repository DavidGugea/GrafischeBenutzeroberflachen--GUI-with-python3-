import tkinter

calculator_frame = tkinter.Tk()

calculator_entry = tkinter.Entry(calculator_frame, width = 50)
calculator_entry.pack(fill = "x")
calculator_entry.pack()

def close():
    calculator_frame.destroy()

def add_to_entry(x):
    calculator_entry.insert("end", str(x))

def pow_with(num):
    result = None
    try:
        result = str(pow(eval(str(calculator_entry.get())), 2))
    except Exception as _e_:
        print(_e_)
        result = "Invalid input"
    
    calculator_entry.delete(0, "end")
    calculator_entry.insert("end", result)

def calculate():
    result = None
    try:
        result = str(eval(str(calculator_entry.get())))
    except Exception as _e_:
        print(_e_)
        result = "Invalid input."
    
    calculator_entry.delete(0, "end")
    calculator_entry.insert("end", result)

# Put the "close" "Pow with 2" & "Pow with 3" buttons inside this frame
options_frame = tkinter.Frame(calculator_frame, height = 5, relief = "sunken")

close_button = tkinter.Button(options_frame, text = "Close", width = 16, command = close)
pow_with_2_button = tkinter.Button(options_frame, text = "Pow with 2", width = 16, command = lambda : pow_with(2))
pow_with_3_button = tkinter.Button(options_frame, text = "Pow with 3", width = 16, command = lambda : pow_with(3))

close_button.pack(side="left")
pow_with_2_button.pack(side="left")
pow_with_3_button.pack(side="left")

options_frame.pack(fill = "x")

# Add numbers & symbols ( n_s_1 = number & symbols section 1 )

# 1-2-3 & +- ( width = 11.25 )
n_s_1 = tkinter.Frame(calculator_frame, height = 5, relief = "sunken")

# for loop doesn't work, you have to do it manually
tkinter.Button(n_s_1, text = 1, command = lambda: add_to_entry(1), width = 11).pack(side="left")
tkinter.Button(n_s_1, text = 2, command = lambda: add_to_entry(2), width = 11).pack(side="left")
tkinter.Button(n_s_1, text = 3, command = lambda: add_to_entry(3), width = 11).pack(side="left")

plus_minus_frame = tkinter.Frame(n_s_1, height = 5)
plus = tkinter.Button(plus_minus_frame, text = "+",  command = lambda : add_to_entry("+"), width = 6)
plus.pack(side="left", fill="x")
minus = tkinter.Button(plus_minus_frame, text = "-", command = lambda : add_to_entry("-"), width = 6)
minus.pack(side="right", fill="x")

plus_minus_frame.pack(fill="x")
n_s_1.pack(fill="x")
# 1-2-3 & +- ( width = 11.25 )

# 4-5-6 & */ ( width = 11.25 )
n_s_2 = tkinter.Frame(calculator_frame, height = 5, relief = "sunken")

tkinter.Button(n_s_2, text = 4, command = lambda: add_to_entry(4), width = 11).pack(side="left")
tkinter.Button(n_s_2, text = 5, command = lambda: add_to_entry(5), width = 11).pack(side="left")
tkinter.Button(n_s_2, text = 6, command = lambda: add_to_entry(6), width = 11).pack(side="left")

multiply_divide_frame = tkinter.Frame(n_s_2, height = 5)
multiply = tkinter.Button(multiply_divide_frame, text = "*",  command = lambda : add_to_entry("*"), width = 6)
multiply.pack(side="left", fill="x")
divide= tkinter.Button(multiply_divide_frame, text = "/", command = lambda : add_to_entry("/"), width = 6)
divide.pack(side="right", fill="x")

multiply_divide_frame.pack(fill="x")
n_s_2.pack(fill="x")
# 4-5-6 & */ ( width = 11.25 )

# 7-8-9 & = ( width = 11.25 )
n_s_3 = tkinter.Frame(calculator_frame, height = 5, relief = "sunken")

tkinter.Button(n_s_3, text = 7, command = lambda: add_to_entry(7), width = 11).pack(side="left")
tkinter.Button(n_s_3, text = 8, command = lambda: add_to_entry(8), width = 11).pack(side="left")
tkinter.Button(n_s_3, text = 9, command = lambda: add_to_entry(9), width = 11).pack(side="left")
equal_button = tkinter.Button(n_s_3, text = "=", command = calculate, width = 13, padx = 3).pack(side="left")

n_s_3.pack(fill="x")
# 7-8-9 & = ( width = 11.25 )

calculator_frame.mainloop()

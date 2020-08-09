import tkinter

main = tkinter.Tk()

def end(): main.destroy()
tkinter.Button(main, text = "Close", command = end).pack()

scrollbar = tkinter.Scrollbar(main, orient="vertical")
li = tkinter.Listbox(main, height = 3)

li.configure(yscrollcommand= scrollbar.set)
scrollbar.configure(command = li.yview)

cities = [
        "Hamburg",
        "Stuttgart",
        "Berlin",
        "Dortmund",
        "Duisburg",
        "Potsdam",
        "Halle"
]

for city in cities:
    li.insert("end", city)

li.pack(side = "left")
scrollbar.pack(side="left", fill = "y")

main.mainloop()

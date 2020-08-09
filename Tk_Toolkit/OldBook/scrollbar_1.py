import tkinter

main = tkinter.Tk()

def end():
    main.destroy()

button = tkinter.Button(main, text = "End", command = end)
button.pack()

scrollbar = tkinter.Scrollbar(main, orient="vertical")
li = tkinter.Listbox(main, height = 4, yscrollcommand = scrollbar.set)
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

li.pack(side="left")
scrollbar.pack(side="left", fill = "y")

main.mainloop()

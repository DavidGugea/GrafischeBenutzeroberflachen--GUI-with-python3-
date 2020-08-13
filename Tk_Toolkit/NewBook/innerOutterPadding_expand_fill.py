import tkinter


class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master=None)

        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameEntry = tkinter.Entry(self)
        self.nameEntry.pack(expand=1, fill="x")

        self.name = tkinter.StringVar()
        self.name.set("Your name ... ")

        self.nameEntry.configure(textvariable=self.name)

        self.ok = tkinter.Button(self)
        self.ok.configure(text = "Ok", command = self.quit)
        self.ok.pack(side = "right", ipadx = 20)

        self.rev = tkinter.Button(self)
        self.rev.configure(text = "Reverse", command = self.reverse)
        self.rev.pack(side="right", ipadx=20)

    def reverse(self):
        reversed_word_list = list()
        for word in self.name.get().split(" "):
            reversed_word_list.append("{0} ".format(word[::-1]))

        self.name.set("".join(reversed_word_list))
    
root = tkinter.Tk()
app = MyApp(root)
app.mainloop()

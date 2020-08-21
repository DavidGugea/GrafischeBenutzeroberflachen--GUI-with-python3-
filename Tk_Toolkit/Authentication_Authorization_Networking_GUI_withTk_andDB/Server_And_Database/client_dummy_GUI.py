import socket 
import tkinter, tkinter.scrolledtext
from concurrent import futures

class GUI(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__()
        self.master = master
        self.pack()

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((socket.gethostname(), 1337))
        self.client.settimeout(0.2)
        self.BUF_SIZE = 4096

        self.chat_text = tkinter.scrolledtext.ScrolledText(self.master)
        self.chat_text.insert(tkinter.END, "insert text first")
        self.chat_text.pack()

        self.entry_text = tkinter.StringVar()
        self.entry = tkinter.Entry(master, textvariable = self.entry_text)
        self.entry.pack()
        self.entry.bind("<Return>", self.send_message)

    def send_message(self, e):
        message_to_server = self.entry_text.get()
        self.client.send(message_to_server.encode("utf-8"))

    def check_for_messages(self):
        try:
            message_from_server = self.client.recv(self.BUF_SIZE) 
            self.chat_text.insert(tkinter.END, "{0}\n".format(message_from_server.decode("utf-8")))
        except socket.timeout as _e_:
            print(str(_e_))

        self.master.after(1000, self.check_for_messages)

x = tkinter.Tk()
gui = GUI(x)
gui.after(1000, gui.check_for_messages)
gui.mainloop()
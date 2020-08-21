import tkinter, tkinter.scrolledtext, tkinter.messagebox
import socket

class ClientGUI(tkinter.Frame):
    def __init__(self, master = None):
        # Configure the master frame
        self.ClientAuthentification_Frame = master
        self.ClientAuthentification_Frame.resizable(0, 0)
        self.ClientAuthentification_Frame.geometry("550x400")
        self.ClientAuthentification_Frame.title("Client Authentification")

        # Pack the master
        super().__init__(self.ClientAuthentification_Frame)
        self.pack()

        # Create the for the client authentification frame
        self.create



tk = tkinter.Tk()

clientGUI = ClientGUI(tk)
clientGUI.mainloop()
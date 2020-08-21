import tkinter, tkinter.scrolledtext, tkinter.messagebox
import socket

class ClientGUI(tkinter.Frame):
    def __init__(self, master = None):
        # Configure the master frame
        self.ClientAuthentication_Frame = master
        self.ClientAuthentication_Frame.resizable(0, 0)
        self.ClientAuthentication_Frame.geometry("550x400")
        self.ClientAuthentication_Frame.title("Client Authentification")

        # Pack the master
        super().__init__(self.ClientAuthentication_Frame)
        self.pack()

        # Create the for the client authentication frame
        self.createAuthenticationWidgets()

    def createAuthenticationWidgets(self):
        pass



tk = tkinter.Tk()

clientGUI = ClientGUI(tk)
clientGUI.mainloop()
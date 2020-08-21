import tkinter, tkinter.scrolledtext, tkinter.messagebox, tkinter.font
import socket

class ClientGUI(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        '''
        Colors used for the client - GUI:
        #FF896A -- > orange-like
        #F5D1C3 -- > pale
        #F7F3F0 -- > white with a little yellow
        #B3D9E3 -- > light blue
        #5B7594 -- > dark blue 

        Source: https://color.adobe.com/explore?page=2 ( it changes all the time, it's a low chance that the exact colors will still be on second page )
        '''

        # Configure the master frame
        self.ClientAuthentication_Frame = master
        self.ClientAuthentication_Frame.resizable(0, 0)
        self.ClientAuthentication_Frame.geometry("550x400")
        self.ClientAuthentication_Frame.title("Client Authentification")
        
        self.ClientAuthentication_Frame.configure(
            bg = "#F7F3F0",
            borderwidth = 0,
        )

        # Create the for the client authentication frame
        self.createAuthenticationWidgets()

    def createAuthenticationWidgets(self):
        # Welcome message
        welcome_message = tkinter.Label(master=self.ClientAuthentication_Frame, text = "Welcome !")
        welcome_message.configure(
            bg = "#F7F4F0",
            fg = "#FF896A",
            font = "Cursive 35"
        )
        welcome_message.pack(pady = (0, 50))

        # Login entries
        self.ClientAuthentication_Username = tkinter.StringVar()
        self.ClientAuthentication_Username.set("Username")

        self.ClientAuthentication_Password = tkinter.StringVar()
        self.ClientAuthentication_Password.set("Password")

        self.ClientAuthentication_UEC = tkinter.StringVar()
        self.ClientAuthentication_UEC.set("UEC")

        ClientAuthentication_Username_EntryWidget = tkinter.Entry(self.ClientAuthentication_Frame, textvariable = self.ClientAuthentication_Username)

        ClientAuthentication_Password_EntryWidget = tkinter.Entry(self.ClientAuthentication_Frame, textvariable = self.ClientAuthentication_Password)

        ClientAuthentication_UEC_EntryWidget = tkinter.Entry(self.ClientAuthentication_Frame, textvariable = self.ClientAuthentication_UEC)

        for EntryWidget in [ClientAuthentication_Username_EntryWidget, ClientAuthentication_Password_EntryWidget, ClientAuthentication_UEC_EntryWidget]:
            EntryWidget.configure(
                bg = "#5B7594",
                fg = "#F5D1C3",
                borderwidth = 0,
                width = 30,
                font = "Cursive 16 bold" 
            ) 

            EntryWidget.pack(ipadx = 15, ipady = 5, padx = 10, pady = 10)

        # Register & Log-In buttons
        ClientAuthentication_Register_Button = tkinter.Button(self.ClientAuthentication_Frame, text = "Register")
        ClientAuthentication_Login_Button = tkinter.Button(self.ClientAuthentication_Frame, text = "Login     ")

        for button in [ClientAuthentication_Register_Button, ClientAuthentication_Login_Button]:
            button.configure(
                bg = "#5B7594",
                fg = "#F5D1C3",
                borderwidth = 0,
                font = "Cursive 12 bold"
            )

        ClientAuthentication_Register_Button.place(relx = 0, rely = 1, anchor = tkinter.SW)
        ClientAuthentication_Login_Button.place(relx = 1, rely = 1, anchor = tkinter.SE)


tk = tkinter.Tk()

clientGUI = ClientGUI(tk)
clientGUI.mainloop()
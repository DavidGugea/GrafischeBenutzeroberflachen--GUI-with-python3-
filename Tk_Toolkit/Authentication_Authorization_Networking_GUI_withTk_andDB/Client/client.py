import tkinter, tkinter.scrolledtext, tkinter.messagebox, tkinter.font
import socket
import sys

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
        self.ClientAuthentication_Frame.title("Client Authentication")
        
        self.ClientAuthentication_Frame.configure(
            bg = "#F7F3F0",
            borderwidth = 0,
        )

        # Create the for the client authentication frame
        self.createAuthenticationWidgets()

    def error_message(self, title, message):
        # Show the error message popup
        tkinter.messagebox.showerror(title, message)
    
    def error_message_close(self, title, message):
        # Show the error message popup AND close the entire program
        tkinter.messagebox.showerror(title, message)
        sys.exit(0)

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

        ClientAuthentication_Login_Button.configure(command = self.login)
        ClientAuthentication_Register_Button.configure(command = self.build_register_toplevel)

    def login(self):
        pass
    
    def build_register_toplevel(self):
        # Build a new toplevel for registering with all the needed inputs
        register_toplevel = tkinter.Toplevel(self.ClientAuthentication_Frame)
        register_toplevel.configure(
            bg = "#5B7594",
            borderwidth = 0 
        )
        register_toplevel.resizable(0, 0)
        register_toplevel.title("Register")
        register_toplevel.geometry("350x600")

        # Title
        register_title = tkinter.Label(register_toplevel, text = "Register form")
        register_title.configure(
            bg = "#5B7594",
            fg = "#F5D1C3",
            font = "Cursiv 25 bold"
        )
        register_title.pack(pady=(5, 15))

        # Register entries & stringvars
        # ~ Variables 
        self.register_username = tkinter.StringVar()
        self.register_username.set("Username")

        self.register_password = tkinter.StringVar()
        self.register_password.set("Password") 

        self.register_UEC = tkinter.StringVar()
        self.register_UEC.set("UEC")

        self.register_FirstName = tkinter.StringVar()
        self.register_FirstName.set("First Name")

        self.register_SecondName = tkinter.StringVar()
        self.register_SecondName.set("Second Name")

        self.register_StreetNameStreetNumber = tkinter.StringVar()
        self.register_StreetNameStreetNumber.set("Street name & street number")

        self.register_PostalCode = tkinter.StringVar()
        self.register_PostalCode.set("Postal Code")

        self.register_CityName = tkinter.StringVar()
        self.register_CityName.set("City Name")

        self.register_UserType = tkinter.StringVar()
        self.register_UserType.set("Worker")

        # ~ Widgets        
        register_username_widget = tkinter.Entry(register_toplevel, textvariable = self.register_username)
        register_password_widget = tkinter.Entry(register_toplevel, textvariable = self.register_password)
        register_UEC_widget = tkinter.Entry(register_toplevel, textvariable = self.register_UEC)
        register_FirstName_widget = tkinter.Entry(register_toplevel, textvariable = self.register_FirstName)
        register_SecondName_widget = tkinter.Entry(register_toplevel, textvariable = self.register_SecondName)
        register_StreetNameStreetNumber_widget = tkinter.Entry(register_toplevel, textvariable = self.register_StreetNameStreetNumber)
        register_PostalCode_widget = tkinter.Entry(register_toplevel, textvariable = self.register_PostalCode)
        register_CityName_widget = tkinter.Entry(register_toplevel, textvariable = self.register_CityName)
        register_UserType_widget = tkinter.OptionMenu(register_toplevel, self.register_UserType, *["Worker", "Administrator"])

        for register_widget in [register_username_widget, register_password_widget, register_UEC_widget, register_FirstName_widget, register_SecondName_widget, register_StreetNameStreetNumber_widget, register_PostalCode_widget, register_CityName_widget, register_UserType_widget]:
            register_widget.configure(
                bg = "#F7F3F0",
                fg = "#000000",
                borderwidth = 0,
                font = "Cursive 10 bold",
                width = 35 
            )

            register_widget.pack(pady = 10, ipady = 5, ipadx = 15)

        
        # Register button
        register_button = tkinter.Button(register_toplevel, text = "Register")
        register_button.configure(
            bg = "#333",
            fg = "#ffffff",
            borderwidth = 0,
            font = "Cursive 10 bold",
            width = 35,
            command = self.register
        )

        register_button.pack(ipadx = 15, ipady = 5)

    def register(self):
        # Get all the user information needed for registering 
        username = self.register_username.get()
        password = self.register_password.get()
        uec = self.register_UEC.get()
        first_name = self.register_FirstName.get()
        second_name = self.register_SecondName.get()
        streetname_streetnumber = self.register_StreetNameStreetNumber.get()
        postal_code = self.register_PostalCode.get()
        city_name = self.register_CityName.get()
        user_type = self.register_UserType.get()

        # Keep track to see if every input is valid or not
        all_inputs_valid = True

        # Build the lists with all the accepted chars for the password ( no special chars. )
        lower_case = [chr(i) for i in range(ord("a"), ord("z") + 1, 1)]
        upper_case = [chr(i) for i in range(ord("A"), ord("Z") + 1, 1)]
        digits = [str(i) for i in list(range(1, 10))] 

        # Check the password ( close the program if the password is not valid )
        for char in password:
            if char not in lower_case and char not in upper_case and char not in digits:
                tkinter.messagebox.showerror("Password error", "The password can't contain any special characters, only numbers from 1 to 9 (inclusive) and all letters, uppercase or lowercase of the standard alphabet. One of the characters in your password was : '{0}'".format(char))
                all_inputs_valid = False
                break
        
        if len(password) <= 8:
            tkinter.messagebox.showerror("Password error", "The given password must have more than 8 chars. Your password has {0} ( '{1}' ) chars".format(len(password), password))

            all_inputs_valid = False

        # Check the postal code
        if all_inputs_valid:
            try:
                postal_code = eval(postal_code)

                if postal_code not in list(range(10000, 99999)):
                    tkinter.messagebox.showerror("Postal code error", "The postal code must be a 5-digit number. Your given postal code was '{0}' and had {1} digits".format(postal_code, len(list(str(postal_code)))))

                    all_inputs_valid = False
            except:
                tkinter.messagebox.showerror("Postal code error", "The postal code must be a 5-digit number. You wrote '{0}' at the postal code".format(postal_code))

                all_inputs_valid = False

        if all_inputs_valid:
            # Build the dictionary with all the needed data for the client to send to the server
            user_dict = {
                "Username" : username,
                "Password" : password,
                "UEC" : uec,
                "FirstName" : first_name,
                "SecondName" : second_name,
                "StreetNameStreetNumber" : streetname_streetnumber,
                "PostalCode" : str(postal_code),
                "CityName" : city_name,
                "UserType" : user_type
            }

            # Build the client that will send all the information back to the user and wait for a validation answer
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((socket.gethostname(), 1337))
            client.setblocking(True)
            client_BUFFER_SIZE = 2048

            # Send the user register data information to the server
            client.send("[USER-REGISTER-DATA]{0}".format(user_dict).encode("utf-8"))

            while True:
                try:
                    message_back = client.recv(client_BUFFER_SIZE)
                    message_back = message_back.decode("utf-8")
                
                    if message_back == "[USER-REGISTER-SUCCESS]":
                        tkinter.messagebox.showinfo("Register success", "You have been successfully registered. Welcome !")
                    elif message_back == "[USER-REGISTER-ERROR]":
                        tkinter.messagebox.showerror("Register error", "There were problems when trying to register you, make sure that the password & uec code are unique")

                    # Close the client
                    client.close()
                    break
                except:
                    pass
                    
tk = tkinter.Tk()

clientGUI = ClientGUI(tk)
clientGUI.mainloop()
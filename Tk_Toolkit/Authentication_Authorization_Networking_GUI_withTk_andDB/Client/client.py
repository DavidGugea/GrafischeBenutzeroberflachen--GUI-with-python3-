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
        self.ClientAuthentication_Frame.title("Client Authentication")
        
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
        ClientAuthentication_Username_EntryWidget.bind("<Return>", self.login)

        ClientAuthentication_Password_EntryWidget = tkinter.Entry(self.ClientAuthentication_Frame, textvariable = self.ClientAuthentication_Password)
        ClientAuthentication_Password_EntryWidget.bind("<Return>", self.login)

        ClientAuthentication_UEC_EntryWidget = tkinter.Entry(self.ClientAuthentication_Frame, textvariable = self.ClientAuthentication_UEC)
        ClientAuthentication_UEC_EntryWidget.bind("<Return>", self.login)

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
    
    def build_register_toplevel(self):
        # Build a new toplevel for registering with all the needed inputs
        register_toplevel = tkinter.Toplevel(self.ClientAuthentication_Frame)
        register_toplevel.configure(
            bg = "#5B7594",
            borderwidth = 0 
        )
        register_toplevel.resizable(0, 0)
        register_toplevel.title("Register")
        register_toplevel.geometry("350x575")

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

        register_button.pack(ipadx = 15, ipady = 5, pady = (15, 0))

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
                    
    def login(self, e=None):
        # Build the string with the dictionary that we will send to the server 
        login_dict = {
            "Username" : self.ClientAuthentication_Username.get(),
            "Password" : self.ClientAuthentication_Password.get(),
            "UEC" : self.ClientAuthentication_UEC.get()
        }
        login_string = "[USER-LOGIN-DATA]{0}".format(login_dict)
        login_string = login_string.encode("utf-8")

        # Build the client and connect it to the server 
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((socket.gethostname(), 1337))
        client.setblocking(True)
        client_BUFFER_SIZE = 2048

        # Send login data to the server 
        client.send(login_string)

        # Wait for server response & build the new toplevel frame in case that the user has successfully logged in
        logged_in = False
        while True:
            try:
                login_validation_message  = client.recv(client_BUFFER_SIZE)
                login_validation_message = login_validation_message.decode("utf-8")

                if login_validation_message.startswith("[USER-LOGIN-ERROR]"):
                    tkinter.messagebox.showerror("Login error", "There was an error when trying to log in. Make sure that your username, password and UEC are valid ( they are case sensitive ).")
                else:
                    tkinter.messagebox.showinfo("Login success", "You have been successfully logged in. Welcome !")
                    logged_in = True
                        
                # Close the client connection with the server
                client.close()

                # Stop listening to the server
                break
            except:
                pass

        if logged_in:
            self.buildLoginToplevelBasedOnUserType(eval(login_validation_message.split("]")[1]))

    def buildLoginToplevelBasedOnUserType(self, USER_DATA_DICT):
        # Build the toplevel frame & configure it
        self.Login_Toplevel = tkinter.Toplevel(self.ClientAuthentication_Frame)
        self.Login_Toplevel.configure(
            bg = "#F7F3F0",
            borderwidth = 0
        )

        self.Login_Toplevel.resizable(0, 0)
        self.Login_Toplevel.title("Welcome, {0} !".format(USER_DATA_DICT.get("FirstName")))

        # Modify the geometry of the toplevel login frame based on the user type ( the worker doesn't need a control frame ) and also based on the user type, build the needed frames

        user_type = USER_DATA_DICT.get("UserType")
        if user_type == "Worker":
            self.BuildLogin_InfoFrame(USER_DATA_DICT)
            self.BuildLogin_ChatFrame(USER_DATA_DICT)

            self.Login_Toplevel.geometry("1000x1000")
        elif user_type == "Administrator" or user_type == "Owner":
            self.BuildLogin_InfoFrame(USER_DATA_DICT)
            self.BuildLogin_ControlFrame(USER_DATA_DICT)
            self.BuildLogin_ChatFrame(USER_DATA_DICT)

            self.Login_Toplevel.geometry("1000x1025")

    def BuildLogin_InfoFrame(self, USER_DATA_DICT):
        info_frame = tkinter.Frame(self.Login_Toplevel, height = 200)
        info_frame.configure(
            bg = "#F7F3F0",
            borderwidth = 0
        )

        info_frame_title = tkinter.Label(info_frame, text = "User info")
        info_frame_title.configure(
            fg = "#FF896A",
            bg = "#F7F3F0",
            font = "Cursive 25 bold",
            borderwidth = 0
        )
        info_frame_title.place(relx=0, rely=0, anchor=tkinter.NW)

        for key, value in USER_DATA_DICT.items():
            info_label = tkinter.Label(info_frame)
            info_label.configure(text = "{0} : {1}".format(key, value))

            info_label.configure(
                bg = "#F7F3F0",
                fg = "#B3D9E3",
                font = "Cursive 13 bold",
                borderwidth = 0
            )

            info_label.pack()

        info_frame.pack(fill = "x")

    def BuildLogin_ControlFrame(self, USER_DATA_DICT):
        control_frame = tkinter.Frame(self.Login_Toplevel)
        control_frame.configure(
            bg = "#F7F3F0",
            borderwidth = 0
        )

        # CONTROL FRAME TITLE
        control_frame_title = tkinter.Label(control_frame, text = "Control frame")
        control_frame_title.configure(
            fg = "#FF896A",
            bg = "#F7F3F0",
            font = "Cursive 25 bold",
            borderwidth = 0
        )
        control_frame_title.place(relx=0, rely=0, anchor=tkinter.NW)
        # CONTROL FRAME TITLE

        ##### Delete frame #####
        delete_frame = tkinter.Frame(control_frame)
        delete_frame.configure(
            bg = "#F7F3F0",
            borderwidth = 0
        )

        # Title
        delete_frame_title = tkinter.Label(delete_frame, text = "Delete User")
        delete_frame_title.configure(
            bg = "#F7F3F0",
            fg = "#333",
            font = "Cursive 13 bold",
            borderwidth = 0
        )
        delete_frame_title.pack()

        # Entries, vars and button
        self.delete_username = tkinter.StringVar()
        self.delete_username.set("Username")

        self.delete_password = tkinter.StringVar()
        self.delete_password.set("Password")

        self.delete_UEC = tkinter.StringVar()
        self.delete_UEC.set("UEC")

        delete_username_entry = tkinter.Entry(delete_frame, textvariable = self.delete_username)
        delete_password_entry = tkinter.Entry(delete_frame, textvariable = self.delete_password)
        delete_UEC_entry = tkinter.Entry(delete_frame, textvariable = self.delete_UEC)

        for entry in [delete_username_entry, delete_password_entry, delete_UEC_entry]:
            entry.configure(
                bg = "#5B7594",
                fg = "#F7F3F0",
                font = "Cursive 12 bold",
                borderwidth = 0
            )

            entry.pack(pady = 10, ipady=3, ipadx=3)

        delete_button = tkinter.Button(delete_frame, text = "Delete user")
        delete_button.configure(
            bg = "#333",
            fg = "#fff",
            font = "Cursive 14 bold",
            borderwidth = 0
        )
        delete_button.pack(pady=(88, 10), ipadx=2, ipady=2)
        ##### Delete frame #####

        ##### Info frame #####
        info_frame = tkinter.Frame(control_frame)
        info_frame.configure(
            bg = "#F7F3F0",
            borderwidth = 0
        )
        
        # Title 
        info_frame_title = tkinter.Label(info_frame, text = "Get info")
        info_frame_title.configure(
            bg = "#F7F3F0",
            fg = "#333",
            font = "Cursive 13 bold",
            borderwidth = 0
        )
        info_frame_title.pack()

        # Entries, vars and button
        self.info_username = tkinter.StringVar()
        self.info_username.set("Username")

        self.info_password = tkinter.StringVar()
        self.info_password.set("Password")

        info_username_entry = tkinter.Entry(info_frame, textvariable = self.info_username)
        info_password_entry = tkinter.Entry(info_frame, textvariable = self.info_password)

        for entry in [info_username_entry, info_password_entry]:
            entry.configure(
                bg = "#5B7594",
                fg = "#F7F3F0",
                font = "Cursive 12 bold",
                borderwidth = 0
            )

            entry.pack(pady = 10, ipady=3, ipadx=3)

        info_button = tkinter.Button(info_frame, text = "Get info")
        info_button.configure(
            bg = "#333",
            fg = "#fff",
            font = "Cursive 14 bold",
            borderwidth = 0
        )
        info_button.pack(pady=(137, 10), ipadx=2, ipady=2)
        ##### Info frame #####

        ##### Update frame ####
        update_frame = tkinter.Frame(control_frame)
        update_frame.configure(
            bg = "#F7F3F0",
            borderwidth = 0
        )

        # Title
        update_frame_title = tkinter.Label(update_frame, text = "Update user")
        update_frame_title.configure(
            bg = "#F7F3F0",
            fg = "#333",
            font = "Cursive 13 bold",
            borderwidth = 0
        )
        update_frame_title.pack()

        # Entries, vars and button
        self.update_username = tkinter.StringVar()
        self.update_username.set("Username")

        self.update_password = tkinter.StringVar()
        self.update_password.set("Password")

        self.update_UpdateProperty = tkinter.StringVar()
        self.update_UpdateProperty.set("Update property")

        self.update_Value = tkinter.StringVar()
        self.update_Value.set("Value")

        update_username_entry = tkinter.Entry(update_frame, textvariable = self.update_username)
        update_password_entry = tkinter.Entry(update_frame, textvariable = self.update_password)
        update_UpdateProperty_entry = tkinter.Entry(update_frame, textvariable = self.update_UpdateProperty)
        update_Value_entry = tkinter.Entry(update_frame, textvariable = self.update_Value)

        for entry in [update_username_entry, update_password_entry, update_UpdateProperty_entry, update_Value_entry]:
            entry.configure(
                bg = "#5B7594",
                fg = "#F7F3F0",
                font = "Cursive 12 bold",
                borderwidth = 0
            )

            entry.pack(pady = 10, ipady=5, ipadx=3)

        update_button = tkinter.Button(update_frame, text = "Update")
        update_button.configure(
            bg = "#333",
            fg = "#fff",
            font = "Cursive 14 bold",
            borderwidth = 0
        )
        update_button.pack(pady=(25, 10), ipadx=2, ipady=2)
        ##### Update frame ####

        # Pack all the control frames & the master of the control frames
        delete_frame.pack(side="left", padx=(50, 0), pady=(75, 0), anchor = tkinter.NW)
        info_frame.pack(side="left", padx=(150, 0), pady = (75, 0), anchor=tkinter.N)
        update_frame.pack(side="right", padx=(0, 50), pady=(75, 0), anchor = tkinter.NW)

        control_frame.pack(fill="x", pady=(50, 0))
     
    def BuildLogin_ChatFrame(self, USER_DATA_DICT):
        # Build the frame
        chat_frame = tkinter.Frame(self.Login_Toplevel)
        chat_frame.configure(
            bg = "#F7F3F0",
            borderwidth = 0
        )

        # Title
        chat_frame_title = tkinter.Label(chat_frame, text = "Chat")
        chat_frame_title.configure(
            fg = "#FF896A",
            bg = "#F7F3F0",
            font = "Cursive 25 bold",
            borderwidth = 0
        )
        chat_frame_title.place(relx=0, rely=0, anchor=tkinter.NW)

        # Chat scrolledtext
        self.CHAT_SCROLLEDTEXT = tkinter.scrolledtext.ScrolledText(chat_frame)

        # Configure the scrolled text widget
        self.CHAT_SCROLLEDTEXT.configure(
            width = 100, 
            height = 10, 
            borderwidth = 1 
        )
        self.CHAT_SCROLLEDTEXT.pack(pady = (50, 0))

        # Build the entry
        self.chat_entry_message = tkinter.StringVar()
        self.chat_entry_message.set("Write your message here and press the <Enter>-key to send it")

        chat_entry = tkinter.Entry(chat_frame)
        chat_entry.configure(
            bg = "#333",
            fg = "#ffffff",
            font = "Cursive 12 bold",
            width = 100,
            borderwidth = 0 
        )
        chat_entry.pack(pady=(20, 0), ipady=3, ipadx=3)

        chat_frame.pack(fill = "x", pady = (50, 0)) 

tk = tkinter.Tk()

clientGUI = ClientGUI(tk)
clientGUI.mainloop()
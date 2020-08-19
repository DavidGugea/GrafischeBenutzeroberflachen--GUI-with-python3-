import socket  # We could have built the socket-server with the socketserver module & socketserver.BaseRequestHandler, but I decided to go with selectors
import selectors
import sqlite3

class Server(object):
    def __init__(self):
        # Port and hostname ( Port is 1337, read the README.md )
        self.PORT = 1337
        self.HOSTNAME = socket.gethostname()

        # Build up the server & the default selector to register the clients. The server must be of type TCP, not UDP
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server.bind((self.HOSTNAME, self.PORT))
        self.server.listen(5)
        self.server.setblocking(False)

        # Build up the connection & cursor with the database & read the users data
        self.db_connection = sqlite3.connect("users_database.db")
        self.db_cursor = self.db_connection.cursor()
        self.db_cursor.execute("SELECT * FROM users_table")
        self.USERS = self.db_cursor.fetchall()
        print(self.USERS)
        
        # Create the default selector to register all the coming clients
        self.DEFAULT_SELECTOR = selectors.DefaultSelector()

        # Register the server listening for client connections and creating communication-sockets
        self.DEFAULT_SELECTOR.register(self.server, selectors.EVENT_READ, self.accept_clientSocket)

    def run(self):
        while True:
            for key, mask in self.DEFAULT_SELECTOR.select():
                key.data(self.DEFAULT_SELECTOR, key.fileobj)

    # Create the handlers for the selector-events
    def accept_clientSocket(self, selector, server):
        # Get the communication socket & the communication socket address info
        communication_socket, communication_socket_addr_info = self.server.accept()
        communication_socket.setblocking(False) 

        # Register the communication socket to the selector to handle the messages from the different clients
        selector.register(communication_socket, selectors.EVENT_READ, self.handleCommunicationSocket)

    def handleCommunicationSocket(self, selector, communication_socket):
        # Get communication socket address 
        communication_socket_addr_info = communication_socket.getpeername()

        try:
            # Read the message of the socket and decode it directly
            client_message = communication_socket.recv(1024).decode("utf-8")

            if not client_message:
                raise ConnectionResetError

            '''
            From the README.md file, the received messages from the client should be used as followed :
            
            -- > If the server gets the [USER-REGISTER-DATA] we must eval the dict after the [USER-REGISTER-DATA] to have a real dictionary and use it.
            -- > If the server gets the [USER-LOGIN-DATA] we must eval again the dict after the [USER-LOGIN-DATA] to have a real dictionary. After that we will check the username-password-UEC code. If the user was found, we will create a string with a dict inside and send the string back to the client in the form [USER-LOGIN-SUCCESS] through the communication socket ( because we use TCP ).
            -- > If the server gets none of the strings that begin with [USER-REGISTER-DATA] or [USER-LOGIN-DATA] we will just send the message from the user, which would be in the string-style "{first-name}{second-name} : {message}" to all the clients 
            '''    

            if client_message == "hello":
                communication_socket.send("hello from the server".encode("utf-8"))
            
            if client_message.startswith("[USER-REGISTER-DATA]"):
                REGISTER_DATA_DICT = eval(client_message.split("]")[1])
                self.database_register(communication_socket, REGISTER_DATA_DICT)
            elif client_message.startswith("[USER-LOGIN-DATA]"):
                LOGIN_DATA_DICT = eval(client_message.split("]")[1])
                self.database_login(communication_socket, LOGIN_DATA_DICT)
                print("LOGIN DATA -- > {0}".format(LOGIN_DATA_DICT))
            else:
                print("USER CHAT MESSAGE -- > {0}".format(client_message))
        except ConnectionResetError:
            print("Communication with {0} has stopped. We will unregister the client-socket.".format(communication_socket_addr_info))
            selector.unregister(communication_socket)
            communication_socket.close()

    def database_register(self, communication_socket, REGISTER_DATA_DICT):
        # Check the type of the given REGISTER_DATA_DICT
        if type(REGISTER_DATA_DICT) != dict:
            raise TypeError("The given REGISTER_DATA_DICT must be of type dict, not {0}".format(type(REGISTER_DATA_DICT))) 
        
        # Check if the given user data has been already used ( password AND UEC-code MUST be unique ). This action will take O(n) time.
        user_in_use = False
        for user in self.USERS:
            if user[1] == REGISTER_DATA_DICT.get("Password") or user[2] == REGISTER_DATA_DICT.get("UEC"):
                user_in_use = True
                break
            else:
                continue
        
        '''
        From README.md:
        If the server gets the [USER-REGISTER-DATA] we must eval the dict after the [USER-REGISTER-DATA] to have a real dictionary and then check if the UEC code and password haven't been used before in the database. 
        If they haven't, then add the new user in the database and send the client the [USER-REGISTER-SUCCESS] message back. 
        If the UEC code or the Password properties have already been used, don't add anything new to the database, and send the [USER-REGISTER-ERROR] to the client. 
        '''
        
        print("USER IN USE -- > {0}".format(user_in_use))
        if not user_in_use:
            # Create the query and insert the new user in the database
            query = "INSERT INTO users_table VALUES (:Username, :Password, :UEC, :FirstName, :SecondName, :StreetNameStreetNumber, :PostalCode, :CityName, :Salary, :UserType)"
            self.db_cursor.execute(query, REGISTER_DATA_DICT)

            # Commit the changes
            self.db_connection.commit()

            # Update the new users for the database
            self.db_cursor.execute("SELECT * FROM users_table")
            self.USERS = db_cursor.fetchall()

            # Send the success message to the client 
            communication_socket.send("[USER-REGISTER-SUCCESS]".encode("utf-8"))
        else:
            # Send the error message to the client
            communication_socket.send("[USER-REGISTER-ERROR]".encode("utf-8"))
    def database_login(self, communication_socket, LOGIN_DATA_DICT):
        # Check the type of the given REGISTER_DATA_DICT
        if type(LOGIN_DATA_DICT) != dict:
            raise TypeError("The given LOGIN_DATA_DICT must be of type dict, not {0}".format(type(LOGIN_DATA_DICT))) 

        '''
        From README.md:
        If the server gets the [USER-LOGIN-DATA] we must eval again the dict after the [USER-LOGIN-DATA] to have a real dictionary. After that we will check the username-password-UEC code. 
        If the user was found, we will create a string with a dict inside that will contain all the data from the user and send the string back to the client in the form "[USER-LOGIN-SUCCESS]{"Username" : x ... }" through the communication socket ( because we use TCP ). 
        In the case that the login data wasn't good and we couldn't find the user in the database, we will have to send a [USER-LOGIN-ERROR] message back to the client. 
        '''

        # Check to see if the user is in the database or not 
        user_found = False 
        
        for user in self.USERS:
            if user[0] == LOGIN_DATA_DICT.get("Username") and user[1] == LOGIN_DATA_DICT.get("Password") and user[2] == LOGIN_DATA_DICT.get("UEC"):
                login_user = {
                    "Username" : user[0],
                    "Password" : user[1],
                    "UEC" : user[2],
                    "FirstName" : user[3],
                    "SecondName" : user[4],
                    "StreetNameStreetNumber" : user[5],
                    "PostalCode" : user[6],
                    "CityName" : user[7],
                    "Salary" : user[8],
                    "UserType" : user[9]
                }

                success_login_message = "[USER-LOGIN-SUCCESS]{0}".format(login_user)
                success_login_message = success_login_message.encode("utf-8")

                communication_socket.send(success_login_message)

                user_found = True 
                break
            else:
                continue 

        if not user_found:
            communication_socket.send("[USER-LOGIN-ERROR]".encode("utf-8"))
            
server = Server()
server.run()
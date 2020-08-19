import socket  # We could have built the socket-server with the socketserver module & socketserver.BaseRequestHandler, but I decided to go with selectors
import selectors
import math

# Port and hostname ( Port is 1337, read the README.md )
PORT = 1337
HOSTNAME = socket.gethostname()

# Build up the server & the default selector to register the clients. The server must be of type TCP, not UDP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOSTNAME, PORT))
server.listen(5)
server.setblocking(False)

# Create the default selector to register all the coming clients
DEFAULT_SELECTOR = selectors.DefaultSelector()

# Create the handlers for the selector-events
def accept_clientSocket(selector, server):
    # Get the communication socket & the communication socket address info
    communication_socket, communication_socket_addr_info = server.accept()
    communication_socket.setblocking(False) 

    # Register the communication socket to the selector to handle the messages from the different clients
    selector.register(communication_socket, selectors.EVENT_READ, handleCommunicationSocket)

def handleCommunicationSocket(selector, communication_socket):
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
            print("REGISTER DATA -- > {0}".format(REGISTER_DATA_DICT)) 
        elif client_message.startswith("[USER-LOGIN-DATA]"):
            LOGIN_DATA_DICT = eval(client_message.split("]")[1])
            print("LOGIN DATA -- > {0}".format(LOGIN_DATA_DICT))
        else:
            print("USER CHAT MESSAGE -- > {0}".format(client_message))
    except ConnectionResetError:
        print("Communication with {0} has stopped. We will unregister the client-socket.".format(communication_socket_addr_info))
        selector.unregister(communication_socket)
        communication_socket.close()

# Register the server listening for client connections and creating communication-sockets
DEFAULT_SELECTOR.register(server, selectors.EVENT_READ, accept_clientSocket)

while True:
    for key, mask in DEFAULT_SELECTOR.select():
        key.data(DEFAULT_SELECTOR, key.fileobj)
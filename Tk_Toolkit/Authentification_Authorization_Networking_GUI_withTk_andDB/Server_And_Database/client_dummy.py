import socket
 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 1337))
client.settimeout(0.2)
# client.setblocking(False)
BUF_SIZE = 4096

while True:
    try:
        message_to_server = input("Message to server -- > ")
        client.send(message_to_server.encode("utf-8"))
            
        message_from_server = client.recv(BUF_SIZE)
        print("Message from server -- > {0}".format(message_from_server.decode("utf-8")))
    except socket.timeout as e:
        print(str(e))
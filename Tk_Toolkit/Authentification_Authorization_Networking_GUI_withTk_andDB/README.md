## Authentification and Authorization project with python 3 networking & GUI using python 3 tkinter module ( Tk ) & python 3 sqlite3 module for db
### Description about Authorization:
There are three types of users that can to different things once they log in :
1. Worker ( Can only see the information about his/her account ) 
2. Administrator ( Can see the information about his/her account and delete, update and see information about **all workers** )
3. Owner ( Can see the information about his/her account and delete, update and see information about **all the workers and administrators** ) 
But all of them will be able to use the chat room

### Information stored about the users in the database:
For every user ( including owner ) we will store the following information:
1. Username
2. Password ( Must be bigger than 8 chars. ( no special characters are allowed, like @ or / ) ) 
3. UEC ( User-Entry-Code, will be a randomly generated 10-characters long string containing letters and numbers )
4. First name
5. Last name
6. Street Name & Street Number
7. Postal Code ( 5-digit long number )
8. City name
9. Salary
10. User type ( Worker / Administrator / Owner )

### Information about the client
The client will be at the start a normal tkinter.Tk() frame with the username, password & UEC log in entries. We will have 2 additional buttons:

- Register
- Log In 

If the user chooses to click on log in we will send the login-data to the server
If the user chooses to click on register we will build a top-level window frame with all the needed user-data for registration and send it to the server.

### Authorization in detail
If the user type is :
1. Worker
- He will only be allowed to see the information about his account 
- He will be allowed to use the chat
- The worker frame will include an info-frame & chat-frame

2. Administrator or Owner
- He will be able to see the information about his account 
- He will be able to delete a user ( the username and password are needed )
- He will be able to get information about a user ( the username of the user is needed ))
- He will be able to update user-account data by choosing the property that he wants to update from the option menu & add the new value in the entry below. The properties that he will be allowed to update will be : street name & street number, Postal Code, City name, Salary & Type ( only Worker or Administrator can be set at the type, there can only be one single owner )
- The administrator & owner frame will include an info-frame, control-frame & chat-frame

### Server & Client configuration
#### Server-Client communication
Client :
- When the client will want to send register data to the server, he will have to send it in this string-style : "[USER-REGISTER-DATA]{Username : 'x' ... }"
- When the client will want to send login data to the server, he will have to send it in this string-style : "[USER-LOGIN-DATA]{Username : 'x' ... }"
- When the client wants to send a message through the chat, he will have to send it in this string-style : "{first-name}{second-name} : {message}"

Server : 
- If the server gets the [USER-REGISTER-DATA] we must eval the dict after the [USER-REGISTER-DATA] to have a real dictionary and then check if the UEC code and password haven't been used before in the database. If they haven't, then add the new user in the database and send the client the [USER-REGISTER-SUCCESS] message back. If the UEC code or the Password properties have already been used, don't add anything new to the database, and send the [USER-REGISTER-ERROR] to the client.
- If the server gets the [USER-LOGIN-DATA] we must eval again the dict after the [USER-LOGIN-DATA] to have a real dictionary. After that we will check the username-password-UEC code. If the user was found, we will create a string with a dict inside that will contain all the data from the user and send the string back to the client in the form "[USER-LOGIN-SUCCESS]{"Username" : x ... }" through the communication socket ( because we use TCP ). In the case that the login data wasn't good and we couldn't find the user in the database, we will have to send a [USER-LOGIN-ERROR] message back to the client.
- If the server gets none of the strings that begin with [USER-REGISTER-DATA] or [USER-LOGIN-DATA] we will just send the message from the user, which would be in the string-style "{first-name}{second-name} : {message}" to all the clients
#### Communication setup
The server and the communication sockets in the default selector in the server file will be non-blocking socket (socket.setblocking(False)). The clients on the other side, will be blocking sockets with a timeout for the recv method of 0.1 seconds.

### Port & Hostname
* The used port will be 1337
* The used hostname will be socket.gethostname()

### Other information about the project 
The project is made so that you can use it on different computers that share the same host name.
As soon as you use the port 1337 & the hostname socket.gethostname(), you are free to use the project on different computers. You can also modify the source code and bind the server & clients to another hostname if you wish to do so.

You can send feedback at : davidgugea@yahoo.com
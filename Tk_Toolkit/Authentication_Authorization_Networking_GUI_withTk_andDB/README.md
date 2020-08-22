## Authentication and Authorization project with python 3 networking & GUI using python 3 tkinter module ( Tk ) & python 3 sqlite3 module for db
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
3. UEC ( User-Entry-Code, will be a randomly generated string containing letters and numbers )
4. First name
5. Second name
6. Street Name & Street Number
7. Postal Code ( 5-digit long number )
8. City name
9. Salary
10. User type ( Types & Salaries : Worker (1000, 3000 ) / Administrator (3000, 8000) / Owner (8000, 10000) )

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
<br><br>
- When the client user type is "Administrator" or "Owner" and wants to delete something, it will have to send a string to the server that will look like this : "[USER-DELETE-DATA]{Username : "...", Password : "...", UEC : "...", TYPE: "..."} 
- For update : "[USER-UPDATE-DATA]{Username: "...", Password : "...", UpdateProperty : "...", Value: "...", TYPE: "..."}
- For information about the user : "[USER-INFO-DATA]{Username:"...", Password: "..."}

<br>
the TYPE property is not the type of the user that we want to delete, it is the type of the user that wants to delete another user ( read the authorization again for more details )

Server : 
- If the server gets the [USER-REGISTER-DATA] we must eval the dict after the [USER-REGISTER-DATA] to have a real dictionary and then check if the UEC code and password haven't been used before in the database. If they haven't, then add the new user in the database and send the client the [USER-REGISTER-SUCCESS] message back. If the UEC code or the Password properties have already been used, don't add anything new to the database, and send the [USER-REGISTER-ERROR] to the client.
- If the server gets the [USER-LOGIN-DATA] we must eval again the dict after the [USER-LOGIN-DATA] to have a real dictionary. After that we will check the username-password-UEC code. If the user was found, we will create a string with a dict inside that will contain all the data from the user and send the string back to the client in the form "[USER-LOGIN-SUCCESS]{"Username" : x ... }" through the communication socket ( because we use TCP ). In the case that the login data wasn't good and we couldn't find the user in the database, we will have to send a [USER-LOGIN-ERROR] message back to the client.
- If the server gets none of the strings that begin with [USER-REGISTER-DATA], [USER-LOGIN-DATA], etc. we will just send the message from the user, which would be in the string-style "{first-name}{second-name} : {message}" to all the clients
<br><br>
- If the server gets "[USER-DELETE-DATA]{Username : "...", Password : "...", UEC : "..."}" then check the username, password and uec code and see if the given user info was found in the database. If the user was found, delete him from the database ( check if the user is allowed to delete the given user ), if the user was found and he is allowed to be deleted by the user in the client, then delete the user from the database and send the [USER-DELETE-SUCCESS] back to the client. Otherwise, return [USER-DELETE-ERROR] back to the client.
- If the server gets "[USER-UPDATE-DATA]{Username: "...", Password: "...", UpdateProperty : "...", Value: " ", TYPE: "..."}" type of format ( so if it starts with [USER-UPDATE-DATA], we will eval the dict after checking that ), check if the given username and password are valid. If they are valid, update the property if the client-user is allowed to delete the user and then send the [USER-UPDATE-SUCCESS] back to the client. If the user wasn't found or is not allowed to be deleted by the client-user, then don't update anything and send [USER-UPDATE-ERROR] back to the client.
- If the server gets "[USER-INFO-DATA]{Username:"...", Password: "..."} back, then check if the user was found in the database, if it was found then send back [USER-INFO-SUCCESS]{Username: "...", ...}. If the user wasn't found in the database, then send back an [USER-INFO-ERROR]

#### Communication setup
The server and the communication sockets in the default selector in the server file will be non-blocking socket (socket.setblocking(False)). The clients on the other side, will be blocking sockets with a timeout for the recv method of 0.2 seconds.

Note: The client will have one main socket from which the chat-communication will work with a blocking socket, but for logging in, registering, deleting and the other actions that users can do, we will have separate blocking sockets that will close after. We will open one socket for example to delete a user, send the information needed to the server and wait for the server to respond, after that we will close that socket because we got the response from the server. In case that we want to delete another user, the delete button function will open another socket again and so on. The 0.2 timeout second non blocking socket will only work for the chat, it will wait to see what it gets from the server ( because this chat-client-socket will be opened forever ) and if the message from the server is not a login, register, update etc. type of message, then it will add it in the chat-frame scrolledtext-widget.

### Port & Hostname
* The used port will be 1337
* The used hostname will be socket.gethostname()

### Other information about the project 
The project is made so that you can use it on different computers that share the same host name.
As soon as you use the port 1337 & the hostname socket.gethostname(), you are free to use the project on different computers. You can also modify the source code and bind the server & clients to another hostname if you wish to do so.

You can send feedback at : davidgugea@yahoo.com
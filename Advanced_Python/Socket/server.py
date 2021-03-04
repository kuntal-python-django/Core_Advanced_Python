import socket                                 

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# get local machine name
host = socket.gethostname()                      
# port
port = 9999

# bind to the port
serversocket.bind((host, port))


# queue up to 5 requests
serversocket.listen(4)                                           

# clientsocket,addr = serversocket.accept()      
# print("Got a connection from %s" % str(addr))
# msg = "You Are Connected : Yo"
# clientsocket.send(msg.encode('ascii'))
# clientsocket.close()

while True:
   # establish a connection
   clientsocket,addr = serversocket.accept()  
   print("Got a connection from %s" % str(addr))
   
   while True:
         msg = input("Enter a Message for Client : ")
         if msg == 0:
               exit()
         clientsocket.send(msg.encode('ascii'))

   clientsocket.close()

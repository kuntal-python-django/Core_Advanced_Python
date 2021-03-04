import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# get local machine name
host = socket.gethostname()                           
# port
port = 9999

# connection to hostname on the port.
s.connect((host, port))                               

while True:
    # Receive no more than 4024 bytes
    msg = s.recv(4024)
    print(msg.decode('ascii'))

s.close()
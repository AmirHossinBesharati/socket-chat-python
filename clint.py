import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 , tcp
s.connect(("127.0.0.1",4458))
serverMessage = s.recv(123456789)
print(serverMessage.decode("utf8"))
message=input('Enter A Message Server: ')
s.sendall(message.encode("utf8"))
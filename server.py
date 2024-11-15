import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 , tcp
s.bind(("127.0.0.1",4458)) # آدرس و پورت 
s.listen((1)) # سه نفر فقط می توانند متصل شن
client , address = s.accept() #نمایش آدرس کلاینت و پورت آن
print(f"conneted to => {address} ")

message = input('ENTER A MESSAGE Clint: ')
client.sendall(message.encode('utf8'))
clientMessage = client.recv(123457)
print(clientMessage.decode('utf-8'))


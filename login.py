import base64, sys
from socket import *

Server=('127.0.0.1',9090)
try: 
    data=input('Username: ').encode()+b'-'+base64.b64encode(input('Passwd: ').encode())
    sender_sock=socket(AF_INET,SOCK_DGRAM)
    sender_sock.connect(Server)
    sender_sock.send(data)
    Auth=sender_sock.recvfrom(5)
    if bool(Auth[0]) == True:
        print("Authenticated")
    else:
        print("failed")
    try:
        while True:
            input()
    except KeyboardInterrupt:
        sender_sock.send(b'')
        sender_sock.shutdown(1)
        sender_sock.close()

except Exception as identifier:
    print("Exception Occured, see the log file")
    with open("error.log",'a+') as file:
        file.writelines(identifier)
        file.close()
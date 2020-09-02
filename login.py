import base64
from socket import *

Server=('xxx.xxx.xxx.xxx',9090)
try: 
    data=input('Username: ').encode()+b'-'+base64.b64encode(input('Passwd: ').encode())
    sender_sock=socket(AF_INET,SOCK_DGRAM)
    sender_sock.sendto(data,Server)
    Auth=sender_sock.recvfrom(5)
except Exception as identifier:
    print("Exception Occured, see the log file")
    with open("error.log",'a+') as file:
        file.writelines(identifier)
        file.close()

if Auth == "True":
    print("Authenticated")
else:
    print("failed")

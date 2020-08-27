import hashlib, os, base64, broadcast

local_address='xxx.xxx.xxx.xxx' # change this according to the IP on your network 

def auth(passwd):
    if hashlib.sha256(passwd.encode('utf-8')).hexdigest() == hashlib.sha256("Password<@A2s4d6f8#>".encode('utf-8')).hexdigest():
        return True
 
def table(ip):
    os.system('iptables -I INPUT 2 -s '+ip+' -j ACCEPT')


os.system('iptables -P INPUT DROP')
os.system('iptables -A INPUT -p udp --dport 9090 -j ACCEPT')
os.system('iptables -A INPUT -p udp -s '+local_address+' -j ACCEPT')

with broadcast.BroadCastReceiver() as Receiver:
    for data, address in Receiver:
        passwd = base64.b64decode(data.decode().split('-')[-1])
        if auth(passwd):
            table(address[0])
            Receiver.sender(address,"True")
        else:
            Receiver.sender(address,"False")
import hashlib, base64, broadcast, platform, shlex
import subprocess as sp

local_address='xxx.xxx.xxx.xxx' # change this according to the IP on your network 

def auth(passwd):
    if hashlib.sha256(passwd).hexdigest() == hashlib.sha256("Password<@A2s4d6f8#>".encode('utf-8')).hexdigest():
        return True

def run(command):
    Cmd = shlex.split(command)
    sp.run(Cmd,stdout=sp.PIPE)

def table(ip):
    if platform.system() == "Linux":
        run('iptables -I INPUT 2 -s '+ip+' -j ACCEPT')
    elif platform.system() == "Darwin":
        run("/usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on")

        run("sudo launchctl load /System/Library/LaunchDaemons/com.apple.alf.agent.plist") # loading default config
        run("sudo launchctl load /System/Library/LaunchAgents/com.apple.alf.useragent.plist")

        run("sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setstealthmode on") #to start setstealthmode
        run("sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setallowsigned on") # to stop automatic whitelisting
        run("sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setallowsignedapp on")
        run("sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setloggingmode on") # to start logging

        run("sudo pkill -HUP socketfilterfw") # to reset the firewall to apply the changes 


def rules():
    if platform.system() == "Linux":
        run('iptables -P INPUT DROP')
        run('iptables -A INPUT -p udp --dport 9090 -j ACCEPT')
        run('iptables -A INPUT -p udp -s '+local_address+' -j ACCEPT')
    elif platform.system() == "Darwin":
        run("/usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on")

        run("sudo launchctl load /System/Library/LaunchDaemons/com.apple.alf.agent.plist") 
        run("sudo launchctl load /System/Library/LaunchAgents/com.apple.alf.useragent.plist")

        run("sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setstealthmode on") 
        run("sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setallowsigned off") 
        run("sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setallowsignedapp off")
        run("sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setloggingmode on")

        run("sudo pkill -HUP socketfilterfw") # to reset the firewall to apply the changes 


def main():
    rules()
    with broadcast.BroadCastReceiver() as Receiver:
        for data, address in Receiver:
            passwd = base64.b64decode(data.decode().split('-')[-1])
            if auth(passwd) == True:
                table(address[0])
                Receiver.sender(address,b"True")
                if Receiver.CloseConnection():
                    print("resetting the firewall!")
                    rules()
            else:
                Receiver.sender(address,b"False")


if __name__ == "__main__":
    main()
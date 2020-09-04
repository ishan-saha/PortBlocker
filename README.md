
# PortBlocker 
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)



### To enhance the security of your nix device
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


This script basically creates iptable rules for blocking any incoming traffic/connection so that the applicaiton port is not discovered even by the means of port knocking. :bangbang: Run this script with sudo!

#### In the script you have to change the `local_address = xxx.xxx.xxx.xxx` with the IP address that shows on your NAC or tunnel in case of a VPN.
To find the ip address of your device over a network you can simply use the `ifconfig <adapter> | grep inet` command by replacing the adapter with suitable value like `en0`. 

The output will look something similar to the following:

>inet6 fe80::106f:596b:b1e2:1579%en0 prefixlen 64 secured scopeid 0x4
>
>inet 172.20.10.6 netmask 0xfffffff0 broadcast 172.20.10.15
>
>inet6 2401:4900:b94:2576:43d:373a:8ece:90d2 prefixlen 64 autoconf secured
>
>inet6 2401:4900:b94:2576:b08e:1faf:58bf:a9ba prefixlen 64 autoconf temporary

## Usage
Find the IP address using the above mentioned process and then update the `portblock.py` and `auth.py` accordingly and keep the port 9090 open or change according to your need.
Run the `portblock.py` wtih python 3.7 in the machine to protect and keep the `broadcast.py` in the same directory as it is required library.
In the Aunthenticating machine install the necessary libraries with `sudo pip3 install -r requirments.txt` and simply run the `auth.py` in python 3.7 interpreter. Authenticate in GUI. Done!
For non GUI simply use the file `login.py` and change the `Server` variable.

### For Mac:
Start by running the srcipt after changes then open `/etc/pf.conf` using nano or vim and add the following line:
>
> pass in proto tcp from any to any port 9090
>
After that simply restart the pf service by running the following command: 
>
>sudo pfctl -f /etc/pf.conf
>

### Future Changes:
- [x] Ship for all linux version
- [x] Add UDP listner 
- [x] Use Hashing for Auth
- [x] Added GUI for client auth
- [x] Ship for MacOS
- [ ] Add TLS on UDP
- [ ] API integration for Auth


# PortBlocker

##To enhance the security of your nix device

This script basically creates iptable rules for blocking any incoming traffic/connection so that the applicaiton port is not discovered even by the means of port knocking. :bangbang: Run this script with sudo!

## In the script you have to change the `local_address = xxx.xxx.xxx.xxx` with the IP address that shows on your NAC or tunnel in case of a VPN.
To find the ip address of your device over a network you can simply use the `ifconfig <adapter> | grep inet` command by replacing the adapter with suitable value like en0. 
The output will look something similar to the following:

>inet6 fe80::106f:596b:b1e2:1579%en0 prefixlen 64 secured scopeid 0x4 
>inet 172.20.10.6 netmask 0xfffffff0 broadcast 172.20.10.15
>inet6 2401:4900:b94:2576:43d:373a:8ece:90d2 prefixlen 64 autoconf secured 
>inet6 2401:4900:b94:2576:b08e:1faf:58bf:a9ba prefixlen 64 autoconf temporary 

### Future Changes:
- [x] Ship for all linux version
- [x] Add UDP listner 
- [x] Use Hashing for Auth
- [] Use TLS for UDP
- [] Ship for MacOS
- [] API integration for Auth

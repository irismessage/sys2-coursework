# Answers and Notes

For associated files i.e. screenshots, fortune.py, see the corresponding directories e.g. question1/ for Question 1.


## Lab Index
- 2: gns3 config
- 3: http, telnet, python, wireshark, fortune server
- 4: dns, whois, dig, dhcp, ntp
- 5: ftp, telnet, python, wireshark, netcat, bob.jpg
- 6: cowsay protocol cwsp, cowsay server, telnet, python, wireshark, tcp, adding latency
- 7: cowsay server, cowsaybigtest, tcp mss maximum segment size, wireshark
- 8: routing, tun device, wireshark, ip route, netcat, router config
- 9: rip routing, quagga, router config,


## Question 1

jm3017
3 + 0 + 1 + 7
sum 11

### PC1
```
ip 192.168.1.11/24 192.168.1.1
```

### PC2
```
ip 192.168.2.12/24 192.168.2.1
```

### R1
```
configure terminal
interface f0/0
ip address 192.168.1.1 255.255.255.0
no shutdown
exit
interface f0/1
ip address 192.168.2.1 255.255.255.0
no shutdown
exit
router ospf 1
network 0.0.0.0 255.255.255.255 area 0
end
```

### PC1
```
ping 192.168.2.12
```


## Question 2

### i
```python
>>> b = bin(134743044)
>>> b
'0b1000000010000000010000000100'
>>> b = b.removeprefix("0b")
>>> b
'1000000010000000010000000100'
>>> b = b.zfill(32)
>>> b
'00001000000010000000010000000100'
>>> int(b[0:8], 2)
8
>>> int(b[8:16], 2)
8
>>> int(b[16:24], 2)
4
>>> int(b[24:32], 2)
4
```
Answer: 8.8.4.4

### ii
```python
>>> s = "00001010.10000000.00010001.00001100"
>>> b = s.replace(".", "")
>>> b
'00001010100000000001000100001100'
>>> len(b)
32
>>> int(b[0:8], 2)
10
>>> int(b[8:16], 2)
128
>>> int(b[16:24], 2)
17
>>> int(b[24:32], 2)
12
```
Answer: 10.128.17.12


## Question 3
TODO
```
tracert 137.229.113.44
```


# Question 4
```
OPTIONS / HTTP/1.1
Host: Ubuntu1
```


## Question 7
- Domain name: google.com
- Top-level domain: com
- Subdomain: www
- The IANA *registrar* ID is 292. IANA does not provide "registrant IDs".
- The "Registry Domain ID" is 2138514_DOMAIN_COM-VRSN.


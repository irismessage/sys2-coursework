# Answers and Notes

For associated files i.e. screenshots, fortune.py, see the corresponding directories e.g. question1/ for Question 1.


## Lab Index
- 1: ip addresses, traceroute / tracert, latency bandwidth propagation delay
- 2: gns3 config
- 3: http, telnet, python, wireshark, fortune server, mail, mutt mail client, maildir
- 4: dns, whois, dig, dhcp, ntp
- 5: ftp, telnet, python, wireshark, netcat, bob.jpg
- 6: cowsay protocol cwsp, cowsay server, telnet, python, wireshark, tcp, adding latency
- 7: cowsay server, cowsaybigtest, tcp mss maximum segment size, wireshark
- 8: routing, tun device, wireshark, ip route, netcat, router config
- 9: rip routing, quagga, router config
- 10: icmp, mac addresses, crc checksums, arp routing, ethernet, cat5 rj45 cables, electronics and waves


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


## Question 4
```
OPTIONS / HTTP/1.1
Host: Ubuntu1
```


## Question 5
telnetlib fortune

no notes, see directory


## Question 6
- vnc set up wireshark captures on u1 and u2, filter: smtp
- ssh to u2
- mutt, m for new mail, addr `student@192.168.100.1`, y to send
    - Ubuntu1.local loops back to u2 for some 
doesn't work

- wireshark on windows, loopback, filter smtp
- vnc wireshark u1, eth0 or any, filter smtp
- telnet from windows `telnet 192.168.100.1 25`
```
mail from:student@Ubuntu1.local
rcpt to:student@Ubuntu1.local
data
Subject: test message
this is a test email for jm3017 coursework
<enter>.<enter>
```


## Question 7
- Domain name: google.com
- Top-level domain: com
- Subdomain: www
- The IANA *registrar* ID is 292. IANA does not provide "registrant IDs".
- The "Registry Domain ID" is 2138514_DOMAIN_COM-VRSN.


## Question 8
Closest root server to Aberdeen is in Dundee, operated by ICANN, address 199.7.83.42, ASN 20144.

Others are shown on the same location on root-servers.org but clicking them reveals all four to be in Edinburgh which is further from Aberdeen.

TTL values:
- york 300s
- google 132s

They differ because they are both constantly decreasing to 0 before being reset, and they aren't in sync because they have different operators.


## Question 9
dhcp release and request capture

no notes, see directory


## Question 10
wireshark windows loopback
```
telnet 192.168.100.1 21

user student
pass 12345
pasv

python question10/ftp_port.py <output>
telnet from result

list
```
filter wireshark by ftp or ftp-data

port used: 20313

### Answer
- Client ports: control 53000, data 53005
- Server ports: control 21, data 20313
- pasv mode is more commonly used because it allwos the server to assign a port then you can use the full range of operations


## Question 11

Bob transfer: neither username nor password nor data are encrypted. You can see the credentials sent in plaintext clearly highlighted in the screenshot. You can also see in the wikipedia screenshot that ftp is unencrypted.

To show that the data is also unencrypted, I compare the bytes transferred to the hex dump of the file. Also note the jfif metadata viewable in wireshark.


# Question 12

from lab6:
`sudo tc qdisc add dev eth1 root netem delay 2500ms`
10s delay:
`sudo tc qdisc add dev eth1 root netem delay 10000ms`

capture u1, eth1, tcp.port == 1234

connect from u1:
`telnet 172.16.100.9 1234`

finally remove the latency from u2
`sudo tc qdisc del dev eth1 root`

### Answer
The RTO varies by doubling each time, starting at the standard one second (1s), then waiting 2s, then 4s. Finally the connection succeeds. In this case the client does not give up, and I successfully ran helo, text, and quit, albeit with the excpected delay. I then disconnected manually.

However I had some inconsistent behaivour, in one case I got some ICMP destination unreachable packets, in another the connection retried unsu
ccessfuly ad infinitum, although the same thing continued after I removed the delay until I restarted the cowsay server. So it was probably due to the specific order I did things in.


## Question 13
The server knows this is a new connection because the initial absolute sequence number is randomly selected, and therefore will be different from the initial sequence number used in the first SYN packet from the previous connection.


## Question 14
In an UDP packet, the size of the data can be determined solely from the value of the "length" section header. Subtract the size of the header, which is always 8 bytes, to get the size of the data.

Conversely, in TCP the size of the header itself is stored in the header. To get the size of the data, you need to subtract the size of the header from the total size of the TCP segment. This can't be found from the header of a sole random TCP packet, you have to get it from either the packet length in the IP header, from which you also need to subtract the size of the IP header, or from the Maximum Segment Size sent during link negotation, assuming conformance with the MSS.


# Question 15
The final step in the checksum algorithm is the bitwise NOT / one's-complement. Therefore, for a final result of 0xFFFF (1111111111111111), the value prior to the final step must be 0x0000.

The value prior to the final step is calculated by the sum of all the other values in the header and data, as represent by 16-bit one's-complement binary. For the result of a one's-complement sum to be exactly zero (0x0000), the inputs must all be zero.[1] This is not possible for a valid TCP packet since the data offset (tcp header size) must be between 5 and 15. 

Therefore, a correctly generated checksum of a valid TCP packet will never have a checksum of 0xFFFF.

[1] todo

import os
import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 8080
# BUF_SIZE = 1024
BUF_SIZE = 9000

sock_tx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

read_file_name = "bob.jpg"
write_file_name = "bob-copy.jpg"
file_size = os.path.getsize(read_file_name)
number_of_segments = -(-file_size // BUF_SIZE)

sock_tx.sendto(write_file_name.encode("ascii"), (UDP_IP, UDP_PORT))
time.sleep(0.1)
sock_tx.sendto(str(number_of_segments).encode("ascii"), (UDP_IP, UDP_PORT))
time.sleep(0.1)

print("Sending: " + read_file_name + ":" + str(number_of_segments))

f = open(read_file_name, "rb")
data = f.read(BUF_SIZE)

for i in range(0, number_of_segments):
    sock_tx.sendto(data, (UDP_IP, UDP_PORT))
    time.sleep(0.1)
    print("tx segment: " + str(i) + " len: " + str(len(data)))
    data = f.read(BUF_SIZE)

sock_tx.close()
f.close()

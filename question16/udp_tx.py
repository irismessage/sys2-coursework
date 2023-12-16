import socket
from os.path import getsize
from time import sleep

# UDP_IP = "127.0.0.1"
UDP_IP = "192.168.100.1"
# UDP_PORT = 8080
UDP_PORT = 8083
# BUF_SIZE = 1024
BUF_SIZE = 9000


read_file_name = "bob.jpg"
write_file_name = "bob-copy.jpg"
file_size = getsize(read_file_name)
number_of_segments = -(-file_size // BUF_SIZE)


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock_tx:
    sock_tx.sendto(write_file_name.encode("ascii"), (UDP_IP, UDP_PORT))
    sleep(0.1)
    sock_tx.sendto(str(number_of_segments).encode("ascii"), (UDP_IP, UDP_PORT))
    sleep(0.1)

    print(f"Sending: {read_file_name}:{number_of_segments}")

    with open(read_file_name, "rb") as f:
        data = f.read(BUF_SIZE)

        for i in range(0, number_of_segments):
            sock_tx.sendto(data, (UDP_IP, UDP_PORT))
            sleep(0.1)
            print(f"tx segment: {i} len: {len(data)}")
            data = f.read(BUF_SIZE)

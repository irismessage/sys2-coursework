import socket

from PIL import Image

UDP_IP = "127.0.0.1"
UDP_PORT = 8080
# BUF_SIZE = 1024
BUF_SIZE = 9000

sock_rx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_rx.bind((UDP_IP, UDP_PORT))

data, addr = sock_rx.recvfrom(BUF_SIZE)
file_name = data.strip()

data, addr = sock_rx.recvfrom(BUF_SIZE)
number_of_segments = int(data)

print("RX File: {0}".format(file_name))

f = open(file_name, "wb")

try:
    for i in range(0, number_of_segments):
        sock_rx.settimeout(2)
        data, addr = sock_rx.recvfrom(BUF_SIZE)
        f.write(data)
        print("rx segment: " + str(i))
    print("Download complete")
    f.close()
    sock_rx.close()
    image = Image.open(file_name)
    image.show()

except socket.timeout:
    print("Oops timeout")
    f.close()
    sock_rx.close()

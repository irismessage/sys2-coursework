import socket

from PIL import Image

# UDP_IP = "127.0.0.1"
UDP_IP = "192.168.100.254"
# UDP_PORT = 8080
UDP_PORT = 8083
# BUF_SIZE = 1024
BUF_SIZE = 9000

try:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock_rx:
        sock_rx.bind((UDP_IP, UDP_PORT))
        sock_rx.settimeout(10)

        data, addr = sock_rx.recvfrom(BUF_SIZE)
        file_name = data.strip()

        data, addr = sock_rx.recvfrom(BUF_SIZE)
        number_of_segments = int(data)

        print(f"RX File: {file_name}")

        with open(file_name, "wb") as f:
            sock_rx.settimeout(2)

            for i in range(0, number_of_segments):
                data, addr = sock_rx.recvfrom(BUF_SIZE)
                f.write(data)
                print(f"rx segment: {i}")
        print("Download complete")

except socket.timeout:
    print("Oops timeout")

else:
    image = Image.open(file_name)
    image.show()

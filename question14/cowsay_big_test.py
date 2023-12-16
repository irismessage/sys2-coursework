import socket
from pathlib import Path


TCP_IP = "192.168.100.1"
TCP_PORT = 1234
BUF_SIZE = 1024
SIZE = 8000  # UPDATE
DATA_FILE_PATH = Path(__file__).parent.joinpath("pg164.txt")


data = []
with open(DATA_FILE_PATH, "r") as data_file:
    while len(data) < SIZE:
        char = data_file.read(1)
        if char != "":
            if (
                (ord(char) > 0x2F and ord(char) < 0x3A)
                or (ord(char) > 0x40 and ord(char) < 0x5B)
                or (ord(char) == 0x20)
                or (ord(char) > 0x60 and ord(char) < 0x7B)
            ):
                data.append(char)
            else:
                data.append(" ")
text = "".join(data)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))
sock.settimeout(2.0)

try:
    print("RX:" + sock.recv(BUF_SIZE).decode("UTF-8"))
    print("TX: helo")
    sock.send(b"helo")
    print("RX:" + sock.recv(BUF_SIZE).decode("UTF-8"))

    sock.send(b"text")
    sock.send(text.encode("UTF-8"))
    sock.send(b"\n")

    try:
        while True:
            data = sock.recv(BUF_SIZE)
            if not data:
                break

            # print("### " + str(len(data)) + " ###")
            print(data.decode("UTF-8"))
    except socket.timeout:
        pass

    sock.send(b"quit\n")
    print("RX:" + sock.recv(BUF_SIZE).decode("UTF-8"))
    sock.close()

except KeyboardInterrupt:
    sock.close()
    print("Exit")

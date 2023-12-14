from sys import argv

if len(argv) == 1:
    print("Enter FTP pasv string")
    input_string = input()
else:
    input_string = argv[1]

input_list = input_string.strip("() ").split(",")
ip_addr = ".".join(input_list[0:4])
port_high = int(input_list[4]) * 256
port_low = int(input_list[5])

output = f"telnet {ip_addr} {port_high}{port_low}"
print(output)

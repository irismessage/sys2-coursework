from sys import argv

if len(argv) == 1:
    print("Enter FTP pasv string")
    input_string = input()
else:
    input_string = argv[1]

input_list = input_string.strip("() ").split(",")
ip_addr_list = input_list[0:4]
ip_addr = ".".join(ip_addr_list)
port_high = int(input_list[4]) * 256
port_low = int(input_list[5])
port = port_high + port_low

output = f"telnet {ip_addr} {port}"
print(output)

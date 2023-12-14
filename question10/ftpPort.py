import sys
if len(sys.argv) == 1:
  print("Enter FTP pasv string")
  inputString = input()
else:
  inputString = sys.argv[1]
inputString = str(inputString).replace('(','')\
              .replace(')','').replace(' ','').split(',')
ip_addr_0 = inputString[0]
ip_addr_1 = inputString[1]
ip_addr_2 = inputString[2]
ip_addr_3 = inputString[3]
port_high = int(inputString[4])*256
port_low  = int(inputString[5])
outputString = "telnet " + ip_addr_0 + '.' + ip_addr_1 + '.' \
               + ip_addr_2 + '.' + ip_addr_3 \
               + ' ' + str(port_high+port_low)
print( outputString )
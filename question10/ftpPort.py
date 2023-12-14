import sys
if len(sys.argv) == 1:
  print("Enter FTP pasv string")
  inputString = input()
else:
  inputString = sys.argv[1]
inputList = inputString.strip('() ').split(',')
ip_addr = inputList[0:4]
port_high = int(inputList[4])*256
port_low  = int(inputList[5])
outputString = "telnet " + '.'.join(ip_addr) \
               + ' ' + str(port_high+port_low)
print( outputString )

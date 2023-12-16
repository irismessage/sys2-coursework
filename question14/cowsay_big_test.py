import socket

TCP_IP = "192.168.100.1"       
TCP_PORT = 1234
BUF_SIZE = 1024
SIZE = 8000                 # UPDATE

sockTX = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockTX.connect((TCP_IP, TCP_PORT))
sockTX.settimeout(2.0) 

dataFile = open("pg164.txt", 'r')
try: 
  print("RX:" + sockTX.recv(BUF_SIZE).decode('UTF-8') )  
  print("TX: helo")
  sockTX.send(b"helo")
  print("RX:" + sockTX.recv(BUF_SIZE).decode('UTF-8') )  

  data=[]    
  while (len(data) < SIZE):
    text = dataFile.read(1)
    if text != '':
      if (ord(text)>0x2F and ord(text)<0x3A) or (ord(text)>0x40 and ord(text)<0x5B) or (ord(text)==0x20) or (ord(text)>0x60 and ord(text)<0x7B):
        data.append( text )
      else:
        data.append( " " )

  sockTX.send( b"text" ) 
  sockTX.send( ''.join(str(x) for x in data).encode('UTF-8') )
  sockTX.send( b"\n" ) 

  try:
    while True:
      data = sockTX.recv(BUF_SIZE)
      if not data:
        break

      #print("### " + str(len(data)) + " ###")	
      print(data.decode('UTF-8'))
  except socket.timeout:
    pass

  sockTX.send( b"quit\n" )   
  print("RX:" + sockTX.recv(BUF_SIZE).decode('UTF-8'))
  sockTX.close()

except KeyboardInterrupt:  
  sockTX.close()
  print("Exit")


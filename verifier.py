import datetime
#!/usr/bin/env python
from socket import AF_INET, SOCK_DGRAM
import sys
import socket
import struct, time

#NOT WRITTEN BY ME
def getNTPTime(host):
        port = 123
        buf = 1024
        address = (host,port)
        msg = '\x1b' + 47 * '\0'
 
        # reference time (in seconds since 1900-01-01 00:00:00)
        TIME1970 = 2208816000+172800 # 1970-01-01 00:00:00
 
        # connect to server
        client = socket.socket( AF_INET, SOCK_DGRAM)
        client.sendto(msg.encode(), address)
        msg, address = client.recvfrom( buf )
        t = struct.unpack( "!12I", msg )[10]
        t-=TIME1970
    
        return t
#WRITTEN BY ME
#SECRET ENCRYPTION GRAPH
def keyGraph(x):
    return int(145.134997*x**2-438.204852*x**5)
    
def isValid(keyTime, keyValue):
    if keyValue != int(str(keyGraph(keyTime))[len(str(keyGraph(keyTime)))-20:]):
      return False
    else:
      return True

if __name__ == '__main__':
  #Gets current time
  curtime = getNTPTime('pool.ntp.org')
  #Asks for the serial key
  key = input("What is the serial key?: ")
  #Formats the serial key to something that the program can read
  keyTime = int(key[:key.find('-')])
  keyValue = int(key[key.find('-')+1:])
  #Checking validity
  if isValid(keyTime, keyValue) == True:
    print("Current UTC time: " + time.ctime(curtime).replace("  "," "))
    print("Expiration date in UTC time: " + time.ctime(keyTime).replace("  "," "))
    print("This key is valid")
  else:
    print("This key is not valid")

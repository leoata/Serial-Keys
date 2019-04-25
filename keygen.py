import datetimefrom socket import AF_INET, SOCK_DGRAM
import sys
import socket
import struct, time
 
#Not written by me
def getNTPTime(host):
        port = 123
        buf = 1024
        address = (host,port)
        msg = '\x1b' + 47 * '\0'
 
 
        # connect to server
        client = socket.socket( AF_INET, SOCK_DGRAM)
        client.sendto(msg.encode(), address)
        msg, address = client.recvfrom( buf )
 
        t = struct.unpack( "!12I", msg )[10]
        t-=(2208816000+172800)

        return t
        
#written by me
def isInt(in1):
        try:
            in1 = int(in1)
            return True
        except Exception:
            return False
 
if __name__ == "__main__":
        tl = input("How long should the key last? (User modifiers: h,d,w,m,y): ")
        curtime = getNTPTime('pool.ntp.org')
        modifierVal = 0
        unitUsed = False
        tl = list(tl)
        for i in tl:
          if isInt(i) == True:
            i = int(i)
          elif unitUsed == False:
            if i == 's':
              modifierVal = (1)
              tl.pop(tl.index('s'))
              unitUsed = True
            elif i == 'h':
              modifierVal = (60*60)
              tl.pop(tl.index('h'))
              unitUsed = True
            elif i == 'd':
              modifierVal = (60*60*24)
              tl.pop(tl.index('d'))
              unitUsed = True
            elif i == 'w':
              modifierVal = (60*60*24*7)
              tl.pop(tl.index('w'))
              unitUsed = True
            elif i == 'm':
              modifierVal = (60*60*24*31)
              tl.pop(tl.index('m'))
              unitUsed = True
            elif i == 'y':
              modifierVal = (60*60*24*365)
              tl.pop(tl.index('y'))
              unitUsed = True
              
        if unitUsed == False:
                print("Incorrect syntax. Use units (d,h,w,m,y)")
                time.sleep(2)
                sys.exit()
        tl = "".join(tl)
        tl = int(tl)
        tl *= modifierVal
              
        

        
        #finalizes serial key before encryption. 
        msg = str(tl+curtime)
        print("Creating serial...")
        
        import random
        #SECRET ENCRYPTION GRAPH (DO NOT SHARE)
        def keyGraph(x):
          return int(145.134997*x**2-438.204852*x**5)
        yValue = str(keyGraph(int(msg)))
        yValue = yValue[len(str(yValue))-20:]
        #Serial Key: Expiration second timestamp-Corresponding Y value
        print("Current time: " + str(curtime))
        print("Expires at " + time.ctime(int(msg)).replace("  "," "))
        print("Serial Key: " + msg + '-' + yValue)

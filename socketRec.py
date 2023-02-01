#!/usr/bin/python2

#netstat -ntp

import socket               # Import socket module
import sys
import string
import thread
import time

def on_new_conn(c,addr):
    msg = ""
    string2find="oo"
    msgnr = 0
    matchFound = 0
    while msg.strip() != "END" :
       msg = c.recv(1024)
       #print 'msg = ',msg[:6]
       if msg.strip() == "END" :
           sendstr= 'Found ' + str(matchFound) + " matches in " + str(msgnr) +' messages!'
           endstr = False
           c.send(sendstr)
           print (time.strftime("%d.%m %H:%M:%S",time.localtime()) + " Closing",addr)
           c.close()
       elif msg[:6] == "MATCH=":
           string2find = msg[6:].strip()
           c.send("now matches '" + string2find + "'")
       else:
           if string2find in msg:
               sendstr = string2find + " found!"
               matchFound += 1
               #print(msg)
           else:
               sendstr = string2find + " NOT found!"
           c.send(sendstr)
           msgnr += 1   




s = socket.socket()         # Create a socket object
host = '192.168.1.36'
port = 12345                # Reserve a port for your service.
s.bind((host, port))

print ('host = ', host)
print ('Port = ', port)
s.listen(10)                 # Now wait for client connection.
endstr = True

while endstr:
   c, addr = s.accept()     # Establish connection with client.
   print (time.strftime("%d.%m %H:%M",time.localtime()) + ' Got connection from', addr)
   thread.start_new_thread(on_new_conn,(c,addr))
   #print 'c = ',c
   #msg = c.recv(250)
   #print 'msg = ',msg
   #msgnr += 1
   #sendstr= 'Thank you for connecting ' + str(msgnr) +':'
   #c.send(sendstr)
   
   #c.close()                # Close the connection
   #sys.exit()
   #endstr = False
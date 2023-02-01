#!/usr/bin/python2

import socket
import random
import time
import f_random
import threading


def isThreadAlive():
  for t in threads:
    if t.isAlive():
      return 1
  return 0

def send_thread(msgnr,match='ab'):
    print("THREADING")
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("192.168.1.36",12345))
    matchstr = "MATCH=" + match
    s.send(matchstr)
    msg = s.recv(250)
    matchnr = 0
    print(msg)
    for i in range (msgnr):
        test_str = f_random.randomword(random.randint(3,100))
        print (test_str)
        if match in test_str:
            matchnr +=1
        s.send(test_str)
        msg = s.recv(500)
        print (msg)
        time.sleep(random.randint(1,3))
    s.send("END")
    msg = s.recv(250)
    #time.sleep(5)
    print (msg)
    print (str(matchnr) + " matches.")
    s.close()


threads = []
for i in range(5):
    match = f_random.randomword(2)
    t=threading.Thread(target=send_thread,args=(70,match))
    threads.append(t)
    t.start()

flag =1
while (flag):
  time.sleep(3)
  flag = isThreadAlive()
    

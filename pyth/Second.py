import socket
import sys

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ser_add=('localhost',65423)
print >> sys.stderr,'connecting to %s port %s' % ser_add
sock.connect(ser_add)

try:
    message='this messgae from client'
    print >> sys.stderr,'sending "%s" ' %message
    sock.sendall(message)

    amnt_re = 0
    amnt_ex = len(message)

    while amnt_re < amnt_ex:
        data=sock.recv(2023)
        amnt_re += len(data)
        print >> sys.stderr ,'received "%s" ' % data

finally:
     print >>  sys.stderr,'closing socket'
     sock.close()

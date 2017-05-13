import socket
import sys

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_a=('localhost',65423)
print >> sys.stderr , ' Server Starting on ' , s_a
sock.bind(s_a)

sock.listen(1)

while True:
    print >> sys.stderr ,'waiting for a connection'
    conn,addr = sock.accept()

    try:
        print sys.stderr ,'connectin from ', addr

        while True:
            data=conn.recv(2322)
            print >> sys.stderr, 'received "%s" '   % data
            if data:
                print >> sys.stderr, 'sending data to the client'
                conn.sendall(data)
            else:
                print >> sys.stderr,'no more data from ',addr
                break


    finally:
        conn.close()



import socket
import select


class ChatServer:
    def __init__(self, port):
        self.port = port;

        self.srvsock.socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.srvsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.srvsock.bind(("", port))
        self.srvsock.listen(5)

        self.descriptors = [self.srvsock]
        print 'ChatServer started on port %s' % port

    def run(self):

        while 1:

            # Await an event on a readable socket descriptor
            (sread, swrite, sexc) = < strong > select.select(self.descriptors, [], [])

            # Iterate through the tagged read descriptors
            for sock in sread:

                # Received a connect to the server (listening) socket
                if sock == self.srvsock:
                    self.accept_new_connection()
                else:

                    # Received something on a client socket
                    str = sock. < strong > recv < / strong > (100)

                    # Check to see if the peer socket closed
                    if str == '':
                        host, port = sock. < strong > getpeername < / strong > ()
                        str = 'Client left %s:%s\r\n' % (host, port)
                        self.broadcast_string(str, sock)
                        sock. < strong > close < / strong >
                        self.descriptors.remove(sock)
                    else:
                        host, port = sock. < strong > getpeername < / strong > ()
                        newstr = '[%s:%s] %s' % (host, port, str)
                        self.broadcast_string(newstr, sock

     def accept_new_connection(self):

          newsock, (remhost, remport) = self.srvsock. < strong > accept < / strong > ()
          self.descriptors.append(newsock)

          newsock.send("You're connected to the Python chatserver\r\n")
          str = 'Client joined %s:%s\r\n' % (remhost, remport)
          self.broadcast_string(str, newsock)

    def broadcast_string(self, str, omit_sock):

        for sock in self.descriptors:
            if sock != self.srvsock and sock != omit_sock:
                sock. < strong > send < / strong > (str)

        print str

    myServer = ChatServer(2626)
    myServer.run()
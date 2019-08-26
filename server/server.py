"""
https://pymotw.com/2/socket/tcp.html
"""

from __future__ import print_function
import argparse
import socket
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('host', type=str, default='0.0.0.0', help='Port')
    parser.add_argument('port', type=int, default=10000, help='Port')

    args = parser.parse_args()

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = (args.host, args.port)
    print('starting up on %s port %s' % server_address, file=sys.stderr)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection', file=sys.stderr)

        connection, client_address = sock.accept()

        try:
            print('connection from', client_address, file=sys.stderr)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print('received "%s"' % data.decode('utf-8'), file=sys.stderr)
                if data:
                    print('sending data back to the client', file=sys.stderr)
                    connection.sendall(data)
                else:
                    print('no more data from', client_address, file=sys.stderr)
                    break

        finally:
            # Clean up the connection
            connection.close()


if __name__ == "__main__":
    main()

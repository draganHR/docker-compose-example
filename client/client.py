"""
https://pymotw.com/2/socket/tcp.html
"""

from __future__ import print_function
import argparse
import socket
import sys
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('host', type=str, default='0.0.0.0', help='Port')
    parser.add_argument('port', type=int, default=10000, help='Port')
    parser.add_argument('--loop', action='store_true', help='Loop')
    parser.add_argument('--sleep', type=int, default=1, help='Sleep in seconds')

    args = parser.parse_args()

    while True:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = (args.host, args.port)
        print('connecting to %s port %s' % server_address, file=sys.stderr)

        sock.connect(server_address)

        try:
            # Send data
            message = 'This is the message.  It will be repeated.'
            print('sending "%s"' % message, file=sys.stderr)

            sock.sendall(message.encode())

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = sock.recv(16)
                amount_received += len(data)
                print('received "%s"' % data.decode('utf-8'), file=sys.stderr)

        finally:
            print('closing socket', file=sys.stderr)
            sock.close()

        if args.loop:
            time.sleep(args.sleep)
        else:
            break


if __name__ == "__main__":
    main()

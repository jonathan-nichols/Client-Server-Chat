import socket

def main():
    host = '127.0.0.1'
    port = 8001
    # create a server socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # bind to localhost
        server.bind((host, port))
        server.listen()
        print(f'Server listening on: localhost on port: {port}')
        # accept client connections to the socket
        client, address = server.accept()
        with client:
            print(f'Connected by {address}\n')
            while True:
                # receive requests from client
                msg = client.recv(4096)
                print(f'Received: {msg}\n')
                # close the socket on empty message
                if not msg:
                    print('Closing server...\n')
                    break
                # send data to the client
                data = input()
                client.sendall(data.encode())



if __name__ == '__main__':
    main()


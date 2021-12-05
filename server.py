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
        # accept client connection to the socket
        client, address = server.accept()
        with client:
            print(f'Connected by {address}')
            print('Type /q to quit')
            print('Waiting for message...')
            while True:
                # receive requests from client
                msg = client.recv(4096).decode()
                print(msg)
                # close the socket on empty message
                if not msg or msg == '/q':
                    print('Closing server...\n')
                    break
                response = ''
                while not response:
                    response = input('>')
                # send response to the client
                client.sendall(response.encode())



if __name__ == '__main__':
    main()


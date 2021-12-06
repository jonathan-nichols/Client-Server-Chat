import socket
import struct

class Server:
    def __init__(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def listen(self, host='127.0.0.1', port=8001):
        self.host = host
        self.port = port
        self.socket.bind((host, port))
        self.socket.listen()
        print(f'Server listening on: localhost on port: {self.port}')

    def accept(self):
        client, address = self.socket.accept()
        print(f'Connected by {address}')
        return client, address

    def receive(self, client):
        # retrieve the message size from first 4 bytes
        recv_size = struct.unpack('i', client.recv(4))[0]
        response = []
        while recv_size > 0:
            response.append(client.recv(4096).decode()) 
            recv_size -= 4096
        return ''.join(response)

    def send(self, client, message):
        # send the message size as first 4 bytes
        data = message.encode()
        client.sendall(struct.pack('i', len(data)))
        client.sendall(data)

    def close(self):
        self.socket.close()
        print('Closing server...\n')

def main():
    # initialize the server
    server = Server()
    server.listen()
    client, address = server.accept()
    print('Type /q to quit')
    print('Waiting for message...')
    while True:
        # receive messages from client
        try:
            message = server.receive(client)
        except struct.error:
            message = ''
        # close the server on quit message
        if not message or message == '/q':
            client.close()
            server.close()
            break
        print(message)
        # get response
        response = ''
        while not response:
            response = input('>')
        # send response to client
        server.send(client, response)


if __name__ == '__main__':
    main()


import socket
import struct

class Client:
    def __init__(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host='127.0.0.1', port=8001):
        self.socket.connect((host, port))

    def receive(self):
        recv_size = struct.unpack('i', self.socket.recv(4))[0]
        response = ''
        while recv_size > 0:
            response += self.socket.recv(4096).decode()
            recv_size -= 4096
        return response

    def send(self, message):
        data = message.encode()
        self.socket.sendall(struct.pack('i', len(data)))
        self.socket.sendall(data)

    def close(self):
        self.socket.close()

def main():
    # initalize the client
    client = Client()
    client.connect()
    print('Type /q to quit')
    print('Enter message to send...')
    while True:
        # get the data to send
        message = ''
        while not message:
            message = input('>')
        client.send(message)
        # receive resposne from server
        try:
            response = client.receive()
            print(response)
        except struct.error:
            response = ''
        # close client on quit message
        if not response or response == '/q':
            client.close()
            break


if __name__ == '__main__':
    main()


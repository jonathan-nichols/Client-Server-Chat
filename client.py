import socket

def main():
    host = '127.0.0.1'
    port = 8001
    # create the socket connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print('Type /q to quit')
        print('Enter message to send...')
        while True:
            msg = ''
            while not msg:
                msg = input('>')
            s.sendall(msg.encode())
            response = s.recv(4096).decode()
            # output data to the console
            print(response)
            # close the connection on quit
            if not response or response == '/q':
                break



if __name__ == '__main__':
    main()


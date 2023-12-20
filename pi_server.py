import socket
import threading


def start_server():
    print("Starting Server")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 1234

    server_socket.bind((host, port))
    server_socket.listen(5)
    while True:
        client_socket, addr = server_socket.accept()

        data = client_socket.recv(1024).decode('utf-8')
        print(data)
        message = "Received"
        client_socket.send(message.encode('utf-8'))
        client_socket.close()


def main():
    server_thread = threading.Thread(target=start_server)
    server_thread.start()


if __name__ == '__main__':
    main()

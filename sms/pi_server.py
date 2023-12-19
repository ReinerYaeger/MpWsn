import socket


def start_server():
    print("asd")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 1234

    # Bind to the port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)

    print("Server listening on {}:{}".format(host, port))

    while True:
        # Establish connection with client
        client_socket, addr = server_socket.accept()
        print('Got connection from', addr)

        # Send a message to the client
        message = "Hello! Thanks for connecting to the server."
        client_socket.send(message.encode('utf-8'))

        # Close the connection
        client_socket.close()

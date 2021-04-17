import socket

from .helper.socket_utils import create_socket, handle_request


def main():
    server_socket = create_socket()

    client_connection = None
    try:
        while True:
            try:
                # Wait for client connections
                client_connection, client_address = server_socket.accept()
                handle_request(client_connection, client_address)
            except socket.timeout:
                pass
    except KeyboardInterrupt:
        if client_connection:
            print("Closing the connection")
            client_connection.close()

    print("Closing the socket")
    server_socket.close()


if __name__ == "__main__":
    main()

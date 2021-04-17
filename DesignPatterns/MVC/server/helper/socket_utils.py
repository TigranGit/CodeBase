import socket
import traceback

from .constants import *
from ..controllers.index import IndexController
from ..controllers.error import ErrorController
from ..controllers.registartion import RegistrationController


def create_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.settimeout(1)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print(f"Listening on port {SERVER_PORT} ...")
    return server_socket


def handle_request(client_connection, client_address):
    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Parse HTTP headers
    headers = request.split("\n")
    body = headers[-1]
    try:
        method, route = headers[0].split()[:2]
    except (IndexError, ValueError):
        method = "GET"
        route = ""

    if route in ("/", "/index", "/index.html"):
        controller = IndexController(client_address)
    elif route in ("/registration", "/registration.html"):
        controller = RegistrationController(client_address)
    else:
        controller = ErrorController(client_address, STATUS_NOT_FOUND)

    try:
        status, content = controller.handle(method, body=body)
    except Exception:
        status = STATUS_SERVER_ERROR
        content = ""
        traceback.print_exc()

    # Send HTTP response
    response = f"HTTP/1.0 {status}\n\n{content}"
    client_connection.sendall(response.encode())
    client_connection.close()

import os
import socket

PORT = 8888


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('10.0.0.2', PORT))
    server_socket.listen(1)
    print "Listening on port " + str(PORT)
    while True:
        client_socket, client_address = server_socket.accept()
        request = client_socket.recv(1024)
        path = request[request.find("GET") + 5:request.find("HTTP") - 1]
        if os.path.isfile(path):
            with open(path, 'rb') as f:
                client_socket.send("""HTTP/1.1 200 OK

""" + f.read())
        else:
            client_socket.send("""HTTP/1.1 404 Not Found

File doesnt exist""")
        client_socket.close()

    server_socket.close()


if __name__ == '__main__':
    main()
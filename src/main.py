import socket
from typing import List

from client_handler import ClientHandler


class MServer(socket.socket):
    clients: List[ClientHandler] = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind(('localhost', 4096))
        self.listen()

    def run(self):
        print("Server running")
        while True:
            conn, _ = self.accept()
            client = ClientHandler(conn, self.clients)
            self.clients.append(client)
            client.run()


if __name__ == '__main__':
    with MServer(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.run()

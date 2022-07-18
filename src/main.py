import socket
from typing import List

from client_handler import ClientHandler


class MServer(socket.socket):
    clients: List[ClientHandler] = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind(('localhost', 4000))
        self.listen()

    def run(self):
        while True:
            conn, _ = self.accept()
            client = ClientHandler(conn, self.clients)
            self.clients.append(client)
            client.run()


if __name__ == '__main__':
    server = MServer(socket.AF_INET, socket.SOCK_STREAM)
    server.run()

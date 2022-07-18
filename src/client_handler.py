import socket
import threading
from typing import List, Any


class ClientHandler:
    conn: socket.socket
    clients: List[Any]

    def __init__(self, conn, clients):
        self.conn = conn
        self.clients = clients

    def run(self):
        threading.Thread(target=self.__run, daemon=True).start()

    def __run(self):
        while self.conn:
            data = self.conn.recv(1024)
            if not data:
                self.conn.close()
                self.clients.remove(self)
                break

            for client in self.clients:
                client.conn.sendall(data)

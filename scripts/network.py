import socket
import pickle


class Network:
    def __init__(self, app):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = app.config["server"]["ip"]
        self.port = 5555
        self.addr = (self.server, self.port)
        self.player = self.connect()

    def get_player(self):
        return self.player

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            data = self.client.recv(4096)
            return pickle.loads(data)

        except socket.error as e:
            print(e)

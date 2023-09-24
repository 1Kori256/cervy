import socket


class Network:
    def __init__(self, app):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = app.config["server"]["ip"]
        self.port = 5555
        self.addr = (self.server, self.port)
        self.data = self.connect()

    def get_data(self):
        return self.data

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
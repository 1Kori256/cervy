import socket
from _thread import *
import sys
import os
import scripts.utilities as utilities

path = os.path.dirname(os.path.abspath(__file__))
config = utilities.load_config(os.path.join(path, "config"))
server = config["server"]["ip"]
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")

data_of_players = ["", ""]

def threaded_client(conn, player):
    conn.send(str.encode(""))
    reply = ""
    while True:
        try:
            data = conn.recv(2048).decode()
            data_of_players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = data_of_players[0]
                else:
                    reply = data_of_players[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
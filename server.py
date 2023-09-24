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

start_data_of_players = ["10_10;10_9;10_8", "20_10;20_9;20_8", "10_20;10_19;10_18", "20_20;20_19;20_18"]
data_of_players = []

import time 
start_time = time.time() 
update_worms = [False, False, False, False]
def game_tick():
    while True:
        if time.time() - start_time >= 0.250:
            start_time = time.time()
            update_worms = [True, True, True, True]

def threaded_client(conn, player):
    data_of_players.append(start_data_of_players[player])
    conn.send("|".join(data_of_players) + "&False&" + player)
    reply = ""
    while True:
        try:
            data = conn.recv(2048).decode()
            data_of_players[player] = data

            if not data:
                free_player_slots.append(player)
                print("Disconnected")
                break
            else:
                reply = "|".join(data_of_players)
                if update_worms[player]:
                    reply += "&True"
                    update_worms[player] = False
                else:
                    reply += "&False"

                #print("Received: ", data)
                #print("Sending : ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()

free_player_slots = [0, 1]
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    if len(free_player_slots) == 0:
        print("No free player slots")
        continue

    current_player = free_player_slots[0]
    free_player_slots.pop(0)
    start_new_thread(threaded_client, (conn, current_player))
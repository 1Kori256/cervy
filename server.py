import socket
from _thread import *
import sys
import os
import scripts.utilities as utilities
import pickle
import time

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


LAST_UPDATE = time.time()


def threaded_client(conn, player_id, game_id):
    global id_count
    conn.send(str.encode(str(player_id)))

    while True:
        try:
            data = conn.recv(4096).decode()

            if game_id in games:
                game = games[game_id]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.reset()
                    elif data != "get":
                        if time.time() - LAST_UPDATE > 0.25:
                            game.update()
                            LAST_UPDATE = time.time()

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[game_id]
        print("Closing Game", game_id)
    except:
        pass

    id_count -= 1
    conn.close()


from scripts.game_instance import GameInstance

games = {}
id_count = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    game_id = id_count // 4 
    if id_count % 4 == 0:
        games[game_id] = GameInstance(game_id)
        player_id = 0
        print("Creating a new game...")
    else:
        player_id = games[game_id].active_players
        games[game_id].active_players += 1


    start_new_thread(threaded_client, (conn, player_id, game_id))
    id_count += 1
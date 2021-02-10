import socket
from _thread import *
import sys

server = "192.168.31.237"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(3)
print("Waiting for a connection, Server Started")

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1]), int(str[2]), int(str[3]), int(str[4]), int(str[5]), int(str[6]), int(str[7]), int(str[8]), int(str[9]), int(str[10]),int(str[11]), int(str[12]), int(str[13]), int(str[14]), int(str[15])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])+ ","+str(tup[2])+","+str(tup[3])+","+str(tup[4])+","+str(tup[5])+","+str(tup[6])+","+str(tup[7])+","+str(tup[8])+","+str(tup[9])+","+str(tup[10])+","+str(tup[11])+","+str(tup[12])+","+str(tup[13])+","+str(tup[14])+","+str(tup[15])

pos = [(0,0, 0, 1, 200, 200, 1, 7, 0, 0, 0, 300, 300, 0, 0, 0),(100,100, 1,1,200, 200, 1 , 7, 0, 0, 0, 300, 300, 0, 0, 0)]

def threaded_client(conn, player):
    #   player=1
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(str.encode(make_pos(reply)))
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

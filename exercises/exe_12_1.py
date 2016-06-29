import socket
import json

HOST = ""
PORT = 50007

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
data = ""
res = ""
req = ""

bookstore = json.loads(open("../data/bookstore.json").read())

while True:
    conn, hostaddr = server.accept()
    req = conn.recv(512)
    search = json.loads(req)
    for book in bookstore:
        if book.get("title") == search.get("title"):
            res = book
    conn.sendall(json.dumps(res))
    conn.close()
    req = ""

import socket
import json

HOST = "localhost"
PORT = 50007

title = raw_input("Give me the title: ")
book = dict()
body = {
    "title": title
}

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(json.dumps(body))
response = ""

while True:
    data = client.recv(512)
    if not data:
        break
    response += data

if len(response) > 0:
    book = json.loads(response)

print json.dumps(book, indent=4)

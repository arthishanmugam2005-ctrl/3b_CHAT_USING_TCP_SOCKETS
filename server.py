import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1" 
port = 5000
server.bind((host, port))
server.listen(1)
print("Server is waiting for connection...")
conn, addr = server.accept()
print("Connected to:", addr)
while True:
    message = conn.recv(1024).decode()
    if message.lower() == "exit":
        print("Client disconnected.")
        break
    print("Client:", message)
    reply = input("You: ")
    conn.send(reply.encode())
    if reply.lower() == "exit":
        break
conn.close()
server.close()
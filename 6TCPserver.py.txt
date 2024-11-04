import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 3333  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = s.accept()  # Accept a connection
    with conn:  # Manage connection lifecycle
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode()  # Receive data from client
            print('Client says:', data)

            if data == 'stop':  # Break the loop if the client says 'stop'
                print("Stopping the server...")
                break

            str2 = input("Enter your message: ")  # Get input from server operator
            conn.sendall(str2.encode())  # Send response to client

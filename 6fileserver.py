import socket

host = "127.0.0.1"
port = 12000
buffer_size = 1024

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)  # Listen for a connection

print("Server is listening for incoming connections...")

while True:
    conn, addr = sock.accept()  # Accept a new connection
    print(f"Connected by {addr}")

    with conn, open("data.txt", "wb") as f:  # Open file in binary write mode
        while True:
            data = conn.recv(buffer_size)
            if not data or data == b"EOF":  # Check for end of file
                print("End of file received.")
                break
            f.write(data)  # Write data to the file

    print("File received and saved as ReceivedFile.txt.")
    break  # Stop the server after one file transfer (optional)

# Close the server socket
sock.close()
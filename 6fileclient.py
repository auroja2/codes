import socket

host = "127.0.0.1"
port = 12000
buffer_size = 1024
file_name = 'data.txt'

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    sock.connect((host, port))

    # Open and read the file in chunks
    with open(file_name, "rb") as f:  # Open in binary mode
        data = f.read(buffer_size)
        while data:
            sock.send(data)  # Send the file data to the server
            data = f.read(buffer_size)  # Read the next chunk

        # Send a termination message to signal the end of file transfer
        sock.send(b"EOF")  # Use a specific byte string to mark end of file
finally:
    # Close the socket
    sock.close()

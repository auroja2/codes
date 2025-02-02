import socket

# Create UDP client
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 8081)

# Read the file in chunks and send over UDP
with open('samplevideo.mp4', 'rb') as f:
    chunk = f.read(4096)
    while chunk:
        udp_client.sendto(chunk, server_address)
        chunk = f.read(4096)


udp_client.sendto(b'EOF',server_address)

print("File sent successfully.")
udp_client.close()
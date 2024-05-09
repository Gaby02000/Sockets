import socket

def servicio():
	print('====== Starting service in 0.0.0.0:12345 ======')
	server_address = ('0.0.0.0', 12345)
	server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server.bind(server_address)
	try:
		while True:
			data, client_address = server.recvfrom(4096)
			print("Received data from {}: {}".format(client_address, data.decode()))
			server.sendto(data, client_address)
	except:
		print('received data is not printable')		
		
	server.close()
	print('====== Service down ======')

def main():
	servicio()

if __name__ == '__main__':
    main()


import socket
MAX=100

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.connect(('0.0.0.0', 12345))
        print("Conectado con UDP!\n")
        
        while True:
            message = input().encode('utf-8')
            sock.sendall(message)
            server_reply = sock.recv(MAX)
            print(server_reply.decode('utf-8'))
            
    except Exception as e:
        print("Error:", e)
        
    finally:
        sock.close()

if __name__ == "__main__":
    main()

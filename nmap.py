import socket
import sys

print("\nTool for mapping open ip ports\n")
host = input("Enter IP adress: ")
start_port = int(input("Enter first port: "))
end_port = int(input("Enter last port: "))


print(f"Scanning host {host} from {start_port} to {end_port}")
for i in range(start_port, end_port + 1):
	s = socket.socket()
	s.settimeout(0.5)
	if s.connect_ex((host, i)) == 0:
		print(f"port {i} open")
	s.close()


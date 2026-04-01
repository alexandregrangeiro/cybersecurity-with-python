import socket
import sys

IWANTALLPORTS = False

def scan(host, port):
	s = socket.socket()
	s.settimeout(0.5) #listen to that port for 0.5s
	ret = s.connect_ex((host, port))
	s.close()
	return ret

#	if result == 0:
#		sys.stdout.write("\n")
#		print(f"port {port} open")
#	elif IWANTALLPORTS: #if you want all ports. self-explanatory. 
#		if result == 111:
#			print(f"port {port} closed")
#		else:
#			print(f"port {port} filtered (code {result})")



print("\nTool for mapping open ip ports\n")
host = input("Enter IP adress: ")
start_port = int(input("Enter first port: "))
end_port = int(input("Enter last port: "))


print(f"Scanning host {host} from {start_port} to {end_port}")

for i in range(start_port, end_port + 1):
	sys.stdout.write(f"\rScanning port {i}...")
	sys.stdout.flush()
	result = scan(host, i)

	if result == 0:
		sys.stdout.write("\r" + " " * 30 + "\r")
		print(f"port {i} open")




print("\nDone scanning.")

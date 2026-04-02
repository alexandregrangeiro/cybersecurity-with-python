import socket
import sys

IWANTALLPORTS = False
ASKTXT = True

def scan(host, port):
	s = socket.socket()
	s.settimeout(0.5) #listen to that port for 0.5s
	ret = s.connect_ex((host, port))
	s.close()
	return ret

def clean_line():
	sys.stdout.write("\r" + " " * 30 + "\r")


ports = {
	"open": [],
	"closed": [],
	"filtered": []
}

print("\nTool for mapping open ip ports\n")
host = input("Enter IP adress: ")
start_port = int(input("Enter first port: "))
end_port = int(input("Enter last port: "))

answer = 'n'
if ASKTXT:
	answer = input("Would you like to create a txt with the output? [y/n(default)] ")
	if answer != 'y' and answer != 'n':
		print(f"{answer} not recognized as valid answer, choosing default (n)")


print(f"Scanning host {host} from {start_port} to {end_port}")

for i in range(start_port, end_port + 1):
	sys.stdout.write(f"\rScanning port {i}...")
	sys.stdout.flush()
	result = scan(host, i)


	if result == 0:
		clean_line()
		print(f"port {i} open")
		ports["open"].append(i)

	elif result == 111:
		if IWANTALLPORTS:
			clean_line()
			print(f"port {i} closed")
		ports["closed"].append(i)
	
	else:
		if IWANTALLPORTS:
			clean_line()
			print(f"port {i} filtered")
		ports["filtered"].append(i)

if answer == 'y':

	with open(f"NMAP {host}", "w") as f:
		f.write(f"Host: {host}\n")
		f.write(f"Range: {start_port}--{end_port}\n\n")

		f.write(f"Open ports: {len(ports["open"])}\n")
		for i in ports["open"]:
			f.write(f"{i}\n")

		f.write(f"Filtered ports: {len(ports["filtered"])}\n")
		for i in ports["filtered"]:
			f.write(f"{i}\n")

		f.write(f"Closed ports: {len(ports["closed"])}\n")
		for i in ports["closed"]:
			f.write(f"{i}\n")


print("\nDone scanning.") 

if len(ports["open"]) == 0:
	print("No open ports found at this host")

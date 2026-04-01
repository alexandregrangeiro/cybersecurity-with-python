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


ports = {
	"open": [],
	"closed": [],
	"filtered": []
}

print("\nTool for mapping open ip ports\n")
host = input("Enter IP adress: ")
start_port = int(input("Enter first port: "))
end_port = int(input("Enter last port: "))
if ASKTXT:
	answer = input("Would you like to create a txt with the output? [y/n(default)] ")
	if answer != 'y' and answer != 'n':
		print(f"{answer} not recognized as valid answer, choosing default (n)")
		answer = 'n'


print(f"Scanning host {host} from {start_port} to {end_port}")

for i in range(start_port, end_port + 1):
	sys.stdout.write(f"\rScanning port {i}...")
	sys.stdout.flush()
	sys.stdout.write("\r" + " " * 30 + "\r")
	result = scan(host, i)


	if result == 0:
		print(f"port {i} open")
		ports["open"].append(i)

	elif result == 111:
		if IWANTALLPORTS:
			print(f"port {i} closed")
		ports["closed"].append(i)
	
	else:
		if IWANTALLPORTS:
			print(f"port {i} filtered")
		ports["filtered"].append(i)





print("\nDone scanning.")

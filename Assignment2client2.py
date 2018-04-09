#**************************#

# CLient No.2 named 'Toor' #

# *************************#





import socket

import sys

import re

from Cryptodome.Cipher import AES



HOST = "localhost"

PORT = 5454

BUFFER = 1024



AES32_KY=b"ad229682b324d71b102b768e3169d3d7"

AES32_IV=b"a4a6f8808346a4a6f3dad779453f0d1c"



print("Waiting for Secret Message....")

connectionB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connectionB.connect((HOST, PORT))

data = connectionB.recv(1024)

encr_msg=data.decode()

connectionB.close()

print("Message from Clients NO. 1 received:", str(encr_msg))

print("Mission accomplished!")
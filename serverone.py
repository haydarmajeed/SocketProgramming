#**************************#
# Server                   #
# *************************#

import socket                                       # Importing socket for TCP connection
import sys                                          # Required Lib
import re                                           # Continuing the connection
import os                                           # Required to support various OS
import random                                       # in case of using rand.  
from Crypto.Cipher import AES                   # encryption cipher 

HOST = "localhost"                                  # Local-host of the machine 
PORT = 5454                                         # Available Port 
BUFFER = 1024                                       # TCP Buffer

print ("Server is awaitng clients to coneect ...")  # Informing client 1 & 2 to connect

AES32_KY=b"ad229682b324d71b102b768e3169d3d7"        # 32 bits AES key
AES32_IV=b"a4a6f8808346a4a6f3dad779453f0d1c"        # Nonce - one-time key 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                       # TCP Socket
s.bind((HOST, PORT))                                                        # Binding to Host & POrt
s.listen(2)                                                                 # LIstening to 2 clients


CONNECTION1, ADDRESS1 = s.accept()                                          # Accepting to connecto to Client one
print("Fist client connected from the following address:", ADDRESS1)        # Inform client one of the connection
CONNECTION2, ADDRESS2 = s.accept()                                          # Accepting to connecto to Client two
print("Second client connected from the following address:", ADDRESS1)      # Inform client one of the connection



while True:
	print("Waiting to receive message from client one")             
	RECEIVED_DATA=CONNECTION1.recv(BUFFER)                                  # Data has been received from Client 1
	ENCRYPTED_TEXT=RECEIVED_DATA                                             
	print("Received an Encrypted Message from CLient One:",ENCRYPTED_TEXT)  
	ENCRYPTION = AES.new(AES32_KY, AES.MODE_EAX,AES32_IV)                   # Decrypting data to send to client 2
	UN_ENCRYPTED_TEXT = ENCRYPTION.decrypt(ENCRYPTED_TEXT) 
	print("Message is being decrypted")                                     # Notification of the decryption
	CONNECTION2.sendall(UN_ENCRYPTED_TEXT)                                  # FOrwaording Cipher text to Client 2
	print("Message has been decrypted and forworded to ClientTwo:")
	break



print("Connection is terminated")                                           # terminating the connection
s.close()

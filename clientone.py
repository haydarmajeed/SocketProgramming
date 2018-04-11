#**************************#
# CLient No.1 named 'Root' #
# *************************#


import socket
import sys
import re
from Crypto.Cipher import AES

HOST = "localhost"
PORT = 5454
BUFFER = 1024

AES32_KY=b"ad229682b324d71b102b768e3169d3d7"
AES32_IV=b"a4a6f8808346a4a6f3dad779453f0d1c"

connectionA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
connectionA.connect((HOST, PORT))

while True:
    Secret_Input=raw_input("Enter your private message to be encrypted: ")    
    print("Message will Encrypt with AES")
    User_Input=Secret_Input.encode() 
    AES_cipher = AES.new(AES32_KY, AES.MODE_EAX,AES32_IV) 
    Encrypted_Message, tag = AES_cipher.encrypt_and_digest(User_Input)
    print("Sending Encrypted Message:",Encrypted_Message)
    connectionA.sendall(Encrypted_Message) 
    connectionA.close()
    break

connectionA.close()
print('Message was sent to the server for Authentication and then to client 2')
print()



#import getpass <> this funtion will hide keystroke when clients as clients are typing their input. it is linked it Secret_Message_Input=getpass.getpass(promot='Enter your private message to be encrypted"


from Crypto.Cipher import AES
import os, time
from Key import *


def pad(words):
	if len(words) % 16 != 0:
		for i in range(16 - (len(words) % 16)):
			words += " "
	return words


def sleep(n):
    time.sleep(n)






#Generates Key
key = getKey()
cipher = AES.new(key, AES.MODE_ECB)
print("Key: {}".format(key))
sleep(2)


def encryptsFile(name):
    global key
    
    #Opens File And Gets Text
    file = open(name, "r")
    text = file.read()
    file.close()

    #PAds Text So its length is
    #A Multiple of 16
    text = pad(text)
    print("\nOrigin text: {}".format(text))
    print("\nFILES CONTENTS: {}".format(text))
    sleep(2)

    #Encrypts Message/Text
    msg = cipher.encrypt(bytes(text.encode()))
    print("\nEncrypted Text {}".format(msg))
    sleep(2)

    #Writes Encrypted Content To Files
    file = open(name, "wb")
    file.write(msg)
    file.close()
    print("\nContents Encrypted")
    sleep(2)


def decryptsFile(name):
    global key
    
    #Displays Encrypted Content
    file = open(name, "rb")
    text = file.read()
    file.close()
    print("\nEncrypted File Contents {}".format(text))
    sleep(2)

    #Decrypts Content From Files
    #With Same Key
    decipher = AES.new(key, AES.MODE_ECB)
    new_msg = decipher.decrypt(text).rstrip()
    new_msg = new_msg.decode()
    print("\nDecrypted text: {}".format(new_msg))
    sleep(2)

    #Writes Contents To File
    print("\nContents Written...")
    file = open(name, "w")
    file.write(new_msg)
    file.close()
    sleep(2)

    #Displays Contents That Are
    #Decrypted
    file = open(name, "r")
    text = file.read()
    file.close()
    print("\nDecrypted File Contents: {}".format(text))


for subdir, dirs, files in os.walk('.'):
    for file in files:
        if '.txt' in file and 'Cle' not in file:
            print("\nFile is <----------- {} ------------>".format(os.path.join(file)))
            encryptsFile(os.path.join(subdir, file))
            decryptsFile(os.path.join(subdir, file))


print("\nDone SO Far")

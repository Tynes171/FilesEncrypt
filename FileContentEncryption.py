from Crypto.Cipher import AES
import os, time


def pad(words):
	if len(words) % 16 != 0:
		for i in range(16 - (len(words) % 16)):
			words += " "
	return words


def sleep(n):
    time.sleep(n)

#Opens File And Gets Text
filename = input("Enter File Name\n")
file = open(filename, "r")
text = file.read()
file.close()


#Generates Key
key = os.urandom(32)
cipher = AES.new(key, AES.MODE_ECB)
print("Key: {}".format(key))
sleep(2)

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
file = open(filename, "wb")
file.write(msg)
file.close()
print("\nContents Encrypted")
sleep(2)


#Displays Encrypted Content
file = open(filename, "rb")
text = file.read()
file.close()
print("\nEncrypted File Contents {}".format(text))
sleep(2)

#Decrypts Content From Files
#With Same Key
decipher = AES.new(key, AES.MODE_ECB)
new_msg = decipher.decrypt(msg).rstrip()
new_msg = new_msg.decode()
print("\nDecrypted text: {}".format(new_msg))
sleep(2)

#Writes Contents To File
print("\nContents Written...")
file = open(filename, "w")
file.write(new_msg)
file.close()
sleep(2)

#Displays Contents That Are
#Decrypted
file = open(filename, "r")
text = file.read()
file.close()
print("\nDecrypted File Contents: {}".format(text))

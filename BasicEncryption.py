#! /usr/bin/python3

from __future__ import print_function
from Crypto.Cipher import AES
import os


def pad(words):
	if len(words) % 16 != 0:
		for i in range(16 - (len(words) % 16)):
			words += " "
	return words



key = os.urandom(32)

cipher = AES.new(key, AES.MODE_ECB)

text = input("Enter a line of text\n")
text = pad(text)

print("Origin text: {}".format(text))

msg = cipher.encrypt(text.encode())

print("Ecrypted Text {}".format(msg))

print("Key: {}".format(key))

decipher = AES.new(key, AES.MODE_ECB)
new_msg = decipher.decrypt(msg).rstrip()
new_msg = new_msg.decode()
print("Decrypted text: {}".format(new_msg))



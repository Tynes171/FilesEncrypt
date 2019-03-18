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

print("ENcrypted Text {}".format(msg))



decipher = AES.new(key, AES.MODE_ECB)

print("Decrypted text: {}".format(decipher.decrypt(msg)))



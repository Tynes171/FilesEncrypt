import os

def keyGen(size = 32):
    return os.urandom(size)

def getKey():
    file = open("Cle.txt", "rb")
    return file.read()

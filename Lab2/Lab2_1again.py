from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def DESencrypter(p,k):
    plaintext=p.encode()
    key=k.encode()
    encryptor=DES.new(key,DES.MODE_ECB)
    padded=pad(plaintext,DES.block_size)
    ciphertext=encryptor.encrypt(padded)
    return ciphertext

def DESdecryptor(c,k):
    key=k.encode()
    decryptor=DES.new(key,DES.MODE_ECB)
    padded=decryptor.decrypt(c)
    plaintext=unpad(padded,DES.block_size)
    return plaintext

def __main__():
    p=input("Enter the plaintext : ")
    k=input("Enter the key : ")
    c=DESencrypter(p,k)
    print(c)
    print(DESdecryptor(c,k))

__main__()
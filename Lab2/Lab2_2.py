from Crypto.Cipher import AES,DES
from Crypto.Util.Padding import pad,unpad
import time

def AESencryptor(p,k):
    plaintext=p.encode()
    key=k.encode()

    encryptor=AES.new(key,AES.MODE_ECB)
    padded=pad(plaintext,AES.block_size)

    ciphertext=encryptor.encrypt(padded)
    return ciphertext

def AESdecryptor(c,k):
    key=k.encode()
    decryptor=AES.new(key,AES.MODE_ECB)
    padded=decryptor.decrypt(c)
    plaintext=unpad(padded,AES.block_size)
    return plaintext


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
    k=input("Enter the key for DES : ")
    k1=input("Enter the key for AES : ")

    AESenc_start=time.time()
    c=AESencryptor(p,k1)
    AESenc_end=time.time()
    AESdec_start=time.time()
    AESdecryptor(c,k1)
    AESdec_end=time.time()

    DESenc_start=time.time()
    c=DESencrypter(p,k)
    DESenc_end=time.time()
    DESdec_start=time.time()
    DESdecryptor(c,k)
    DESdec_end=time.time()

    print("AES encryption : "+str(AESenc_end-AESenc_start))
    print("DES encryption : "+str(DESenc_end-DESenc_start))
    
    print("AES decryption : "+str(AESdec_end-AESdec_start))
    print("DES decryption : "+str(DESdec_end-DESdec_start))

__main__()
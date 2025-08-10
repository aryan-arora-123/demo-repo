from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad

def DESencrypt(p,k):
    key=k.encode()
    plaintext=p.encode()

    padded=pad(plaintext,DES.block_size)
    cipher=DES.new(key,DES.MODE_ECB)

    ciphertext=cipher.encrypt(padded)
    return ciphertext
def DESdecrypt(c,k):
    key=k.encode()
    decrypter=DES.new(key,DES.MODE_ECB)

    padded=decrypter.decrypt(c)
    plaintext=unpad(padded,DES.block_size)
    print("The plaintext is : ",plaintext.decode())

def __main__():
    p=input("Enter the plaintext : ")
    k=input("Enter the key : ")
    c=DESencrypt(p,k)
    print(c)
    DESdecrypt(c,k)
__main__()
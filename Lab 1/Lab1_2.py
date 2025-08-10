def vigenereEncrypt(p,k):
    updatedk=""
    for i in range(0,len(p)):
        updatedk+=k[i%len(k)]
    k=updatedk;
    c=""
    for i in range (0,len(p)):

        c+=chr((ord(p[i])-97+ord(k[i])-97)%26+97)
    return c;

def vigenereDecrypt(c,k):
    updatedk=""
    for i in range(0,len(c)):
        updatedk+=k[i%len(k)]
    k=updatedk
    k=updatedk
    p=""
    for i in range(len(c)):
        p+=chr(((ord(c[i])-97)-(ord(k[i])-97)+26)%26+97)
    return p

def __main__():
    p=input("Enter the plaintext : ")
    k=input("Enter the key : ")
    c=vigenereEncrypt(p,k)
    print("Vigenere : ")
    print("The ciphertext is : ",c)
    print("The decrypted text is : ",vigenereDecrypt(c,k))
    print("\nAutokey : ")
    c=autokeyEncry(p,k)
    print("The ciphertext is : ",c)
    print("The decrypted text is : ",autoKeyDecrypt(c,k))


def autokeyEncry(p,k):
    for i in range(len(p)-len(k)):
        k+=p[i]
    c=""
    for i in range(len(p)):
        c+=chr( (ord(p[i])-97 + ord(k[i])-97) %26 +97 )
    return c

def autoKeyDecrypt(c,k):
    updatedk=""
    p=""
    for i in range (len(c)):
        if i<len(k):
            updatedk+=k[i]
        else:
            updatedk+=p[i-len(k)] ##because key has "<key><plaintext>"  and we have foiund a part of the plaintext so now we can keep constructing the updated key and go on !!!
        p+=chr((ord(c[i])-ord(updatedk[i])+26)%26 +97)
    return p
__main__()
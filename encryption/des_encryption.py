from Crypto.Cipher import DES 
from secrets import token_bytes 

key = token_bytes(8)

def encrypt(msg):
    cipher = DES.new(key,DES.MODE_EAX)
    nonce = cipher.nonce 
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('utf-8'))
    return nonce, ciphertext, tag 

def decrypt(nonce, ciphertext, tag): 
    cipher = DES.new(key, DES.MODE_EAX, nonce = nonce)
    plaintext = cipher.decrypt(ciphertext)

    try:
        cipher.verify(tag)
        return plaintext.decode("utf-8")
    except:
        return False

nonce, ciphertext, tag = encrypt(input("Enter a message: "))
plaintext = decrypt(nonce, ciphertext, tag)

if not plaintext: 
    print("Message is corrupted!")
else: 
    print(f"Plain text: {plaintext}")


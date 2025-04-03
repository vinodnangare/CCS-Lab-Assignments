# importing AES
from Crypto.Cipher import AES

# Corrected encryption key (16 bytes long)
key = b'C&F)H@McQf9TjWnZ'  # Now it's exactly 16 bytes

# create new instance of cipher
cipher = AES.new(key, AES.MODE_EAX)

# data to be encrypted
data = "SANJIVANI".encode()

# nonce is a random value generated each time we instantiate the cipher
nonce = cipher.nonce

# encrypt the data
ciphertext = cipher.encrypt(data)

# print the encrypted data
print("Cipher text:", ciphertext)

# generate new instance with the key and nonce same as encryption cipher
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

# decrypt the data
plaintext = cipher.decrypt(ciphertext)
print("Plain text:", plaintext.decode())

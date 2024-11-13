# import Fernet and MultiFernet modules
from cryptography.fernet import Fernet, MultiFernet

# key generation
key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())

# the MultiFernet takes a list of Fernet instances
f = MultiFernet([key1, key2])

# encryption and token generation
token = f.encrypt(b"Welcome to GeeksForGeeks Python Module!")

# display the ciphertext
print(token)

# decryption of ciphertext to plaintext
d = f.decrypt(token)

#display the plaintext
#decode() method converts byte to string
print(d.decode())

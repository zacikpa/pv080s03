# # How to actually encrypt/decrypt something?
# Let's say we have a message and want to encrypt using Advance Encryption Standard (AES)
# What do we need to do? We need the implementation of AES, which is, thankfully, already
# provided in cryptographic libraries in the programmin languages etc.
# In Python we can use [`cryptography`](https://cryptography.io/en/latest/) library.
#
# Before we start encrypting we will discuss few details.


# +
# To generate keys securely we can use Python's built-in module `secrets`
import secrets

# generate a 128-bit key
key = secrets.token_bytes(16)
print(f"key: {key.hex()}")

# +
# Some encryption modes require padding of the message before it is encrypted.

# +
# FIXME padding?
import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# in order to actually encrypt something we need several things

# the actual message as `bytes`, since most operation will
# happen on `bytes`
message = b"This message will be encrypted.."
# the key
key = secrets.token_bytes(32)
# often the initialization vector for the chosen mode
iv = secrets.token_bytes(16)
mode = modes.CBC(iv)

# now we can build the cipher object and corresponding
# encryptor/decryptor objects
cipher = Cipher(algorithms.AES(key=key), mode=mode)
encryptor = cipher.encryptor()

# often the cryptographic algorithms have two phases:
# 1) _update_, where we feed the data we have into it
# 2) _finalize_, where we tell the algorithm we want to finish
# and receive the actual result
ciphertext = encryptor.update(message) + encryptor.finalize()

# now we can decrypt the message and check that it equals the original one
decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext) + decryptor.finalize()

assert message == plaintext

print(f"   message: {message!r}")
print(f"ciphertext: {ciphertext!r}")
print(f" plaintext: {plaintext!r}")
# -


# # Task
# We have encrypted a message for you using AES-CTR with 32B key. The `nonce` is the first 16B of the ciphertext.
# ```
# key: 74cb437bab249d29a81c90cd293c0239a020c2784b289fc381669cc80fa0d307
# ciphertext: 8ef291ed58710767d154beaf19a00c353c41f53a6fb5baaad97827e6f0547e6e8fb93b886eabfae9724ca47e11fd1801
# ```

# +
# TODO: parse the values into bytes
# key = ____
# nonce = ____
# ciphertext = ____
# TODO: decrypt the message
# plaintext


# FIXME hide the solution:
key = bytes.fromhex("74cb437bab249d29a81c90cd293c0239a020c2784b289fc381669cc80fa0d307")
nonce = bytes.fromhex(
    "8ef291ed58710767d154beaf19a00c353c41f53a6fb5baaad97827e6f0547e6e8fb93b886eabfae9724ca47e11fd1801"
)[:16]
ciphertext = bytes.fromhex(
    "8ef291ed58710767d154beaf19a00c353c41f53a6fb5baaad97827e6f0547e6e8fb93b886eabfae9724ca47e11fd1801"
)[16:]
cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.CTR(nonce))
decryptor = cipher.decryptor()

decryptor.update(ciphertext) + decryptor.finalize()
# -

# # Task
# Testing software implementation is **a necessary practice**. Same applies to testing the implementation of encryption functions like AES. You will now test the correctness of AES implementation.
#
# There are several places, where you can search for test vectors (e.g. [Recommendation for Block
# 2001 Edition Cipher Modes of Operation](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf))

# Here we have copied out some of the test vectors for encryption and decryption.
# ```
# F.2 CBC Example Vectors
# F.2.1 CBC-AES128.Encrypt
#
# Key 2b7e151628aed2a6abf7158809cf4f3c
# IV 000102030405060708090a0b0c0d0e0f
#
# Block #1
# Plaintext 6bc1bee22e409f96e93d7e117393172a
# Ciphertext 7649abac8119b246cee98e9b12e9197d
#
# Block #2
# Plaintext ae2d8a571e03ac9c9eb76fac45af8e51
# Ciphertext 5086cb9b507219ee95db113a917678b2
#
# F.2.4 CBC-AES192.Decrypt
#
# Key 8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b
# IV 000102030405060708090a0b0c0d0e0f
#
# Block #1
# Ciphertext 4f021db243bc633d7178183a9fa071e8
# Plaintext 6bc1bee22e409f96e93d7e117393172a
#
# Block #2
# Ciphertext b4d9ada9ad7dedf4e5e738763f69145a
# Plaintext ae2d8a571e03ac9c9eb76fac45af8e51
# ```

# +
# TODO: finish the following code in order to test the AES-CBC implementation
# in Python's `cryptography`. You don't have to go through all four test vectors.

# TODO: Encryption
key = bytes.fromhex(____)
iv = ____

# Block #1
plaintext = ____
expected_ciphertext = ____

ciphertext = ____
print(ciphertext == expected_ciphertext)

# Block #2

# TODO: Decryption
# Block #1
# Block #2
# -


# ## Why not to use ECB mode
#
# You've probably heard that ECB mode is not secure. Go through the following example and try it out! There is a bit more code to make it interactive. See the comments for clarification.

# +
from PIL import Image
import io
from IPython.display import clear_output, display
import secrets

# First we download a picture of a penguin
response = requests.get("https://upload.wikimedia.org/wikipedia/commons/5/56/Tux.jpg")
# and open it as an image
img = Image.open(io.BytesIO(response.content))

# create `Cipher` object using a random key and ECB mode
cipher = ____
encryptor = ____

img_bytes = img.tobytes()
# encrypt img_bytes
encrypted_img_data = ____
# create a new image using the encrypted_img_data
enc_img = Image.frombytes(data=encrypted_img_data, size=(196, 216), mode="RGB")

# display both
display(img)
display(enc_img)


# +
def send_msg(sender_uco: str, receiver_uco: str, msg: bytes):
    # TA TODO POST to pv080.fi.muni.cz/s03
    reqeusts.post()
    pass


def recv_msg(sender_uco: str, receiver_uco: str) -> bytes:
    # TA TODO get from pv080.fi.muni.cz/s03
    requests.get()
    pass


def generate_key_from_phrase(phrase: str) -> bytes:
    # TA TODO deterministic even if unsecure way of generating a key
    # While it is dangerous to teach them how NOT TO DO it, we will
    # talk about keys, PBKD2 etc. later
    # it
    pass


# TODO:
# 1] send an encrypted message to your classmate
# 2] recv and decrypted a message from your classmate
# Share your keys via a different channel.

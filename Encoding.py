# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Data representation and encodings

# ## Task 1
# Get familiar with the various encodings.

# +
import ipywidgets as widgets

# some heavy lifting for this interactive demo is hidden through imports
from encoding_utils import byte_ui, first, second, third, fourth


def show_bytes(first, second, third, fourth):
    as_binary = f"{first:08b} {second:08b} {third:08b} {fourth:08b}"
    # print((first, second, third, fourth))
    as_bytes = bytes([first, second, third, fourth])
    as_utf8 = as_bytes.decode("utf-8", errors="replace")
    as_ascii = as_bytes.decode("ascii", errors="replace")
    as_hexa = f"{first:02X} {second:02X} {third:02X} {fourth:02X}"
    print(f"as binary: {as_binary}")
    print(f"as   HEXA: {as_hexa}")
    print(f"as  bytes: {as_bytes}")
    print(f'as  UTF-8: "{as_utf8}"')
    print(f'as  ASCII: "{as_ascii}"')


byte_output = widgets.interactive_output(
    show_bytes, {"first": first, "second": second, "third": third, "fourth": fourth}
)

display(byte_ui, byte_output)
# -

# # Convert between various data formats

# In Python (3) strings of the 'str' type are considered strings of [Unicode](https://en.wikipedia.org/wiki/Unicode) characters. These characters represent individual Unicode code-points. These strings by themselves do not have an associated representation as a sequence of bytes. Thus if you want to get a sequence of bytes you need to choose an encoding which can transform the code-points to bytes, such as ASCII or UTF-8. For more on Python strings and Unicode, check [this](https://docs.python.org/3/howto/unicode.html) out.
#
# ## Note about strings and bytes in Python
#
# Python tries to be helpful and so if it is supposed to display a byte value (in a 'bytes' object) that corresponds to a printable ASCII character (e.g. from the English alphabet) it displays **that character** instead of the actual byte value. Let us see this in action. If it is not a printable ASCII character, Python will display its raw value in hexadecimal with the `\x` prefix (see [here](https://stackoverflow.com/questions/54358833/how-does-bytes-repr-representation-work) for details).

# +
# Let us start with a string ASCII message
msg = "A simple string message"

# We can check this using the following assert
print("Message is a 'str':", isinstance(msg, str))

# In order to access the underlying bytes of the `msg` we can _encode_ it.
# We can explicitly say we encode it to ASCII.
print("Message encoded as bytes to ASCII:", msg.encode("ascii"))

# +
# If you ran the previous cell you can see that the value of the printed `msg` is
# b'A simple string message'
# And while we can still read it, it is not _the same_ for Python
print(b"A simple string message" != "A simple string message")

# Because its type is now 'bytes'
print(isinstance("A simple message".encode("ascii"), bytes))
# -

# ## Task 1
# Convert the following data blob of bytes represented as binary (using the `0b` prefix to be explicit) to an ASCII message. Each binary value represents a single ASCII character. That is do `binary -> string (through ASCII)`.

# TODO: find out the message from this blob!
binary_blob = """
0b1001001 0b100000 0b1100001 0b1101101 0b100000
0b1110011 0b1110100 0b1100001 0b1110010 0b1110100
0b1101001 0b1101110 0b1100111 0b100000 0b1110100
0b1101111 0b100000 0b1100111 0b1100101 0b1110100
0b100000 0b1110100 0b1101000 0b1100101 0b100000
0b1101000 0b1100001 0b1101110 0b1100111 0b100000
0b1101111 0b1100110 0b100000 0b1110110 0b1100001
0b1110010 0b1101001 0b1101111 0b1110101 0b1110011
0b100000 0b1100100 0b1100001 0b1110100 0b1100001
0b100000 0b1100101 0b1101110 0b1100011 0b1101111
0b1100100 0b1101001 0b1101110 0b1100111 0b1110011
0b101110
"""

# +
# Hint: what does `split` do? And what about `int(value, number_base)`?
# -

# FIXME REMOVE SOLUTION, DON'T LOOK
individual_binary = binary_blob.strip().split()
byte_values = bytes([int(b, 2) for b in individual_binary])
byte_values.decode("ascii")

# FIXME REMOVE REVERSED SOLUTION, DON'T LOOK
msg = "I am starting to get the hang of various data encodings."
as_bytes = msg.encode("ascii")
as_binary = " ".join([bin(b) for b in as_bytes])
print(as_binary)

# ## Task 2
# Each of the following integers represents a single character in ASCII encoding. Convert them back! Do `integers -> string (through ASCII)`.

integers_blob = """
73 116 32 105 115 32 116 104 101 32 116 104 105 114
100 32 119 101 101 107 32 97 110 100 32 73 32 115
116 105 108 108 32 104 97 118 101 32 122 101 114
111 32 105 100 101 97 32 97 98 111 117 116 32
99 114 121 112 116 111 103 114 97 112 104 121
"""

# +
# FIXME REMOVE SOLUTION, DON'T LOOK
# -

integers = [int(i) for i in integers_blob.strip().split()]
bytes(integers).decode("ascii")

# FIXME REMOVE REVERSED SOLUTION, DON'T LOOK
msg = "It is the third week and I still have zero idea about cryptography"
as_bytes = msg.encode("ascii")
" ".join([str(i) for i in list(as_bytes)])

# ## Task 3
#
# One of the tutors of PV080 got really confused with the encodings and made a mess.<br>
# He took a message and encoded in into ASCII.<br>
# He then looked at those bytes in hexadecimal. This reminded him of ASCII.<br>
# So he then turned those hexadecimal characters to ASCII, AGAIN!<br>
# Finally, he took those bytes and saw that there is another encoding called Base64. So he also used that one.<br>
# Ok, one more thing. He turned those bytes into an ASCII string.<br><br>
#
# Can you help the rest of the tutors to untangle this mess and find the original message? First have a look at the Base64 example below.

# ### A Base64 example

# +
# HINT: Do not worry about Base64. It is actually pretty simple.
from base64 import b64decode, b64encode

message = "message"
# Encode the message into Base64 encoding
# b64decode and b64encode operate on bytes
b64_encoded_msg = b64encode(message.encode("ascii"))

# Decode the message back and then also into string
original_message = b64decode(b64_encoded_msg).decode("ascii")

# Make sure we have gone full circle
assert original_message == message
# -

# ### The mess

# TODO: Try to get to the original message
blob = "NTQ2ODY5NzMyMDZmNmUyMDY5NzMyMDY3NjU3NDc0Njk2ZTY3MjA2MTIwNjI2OTc0MjA2MzZmNmQ3MDZjNjk2MzYxNzQ2NTY0MmUyMDQ0NmYyMDZlNmY3NDIwNmY3NjY1NzI2NDZmMjA3NDY4NjUyMDY1NmU2MzZmNjQ2OTZlNjc3MzJlMmU="
bytes2 = ____
string2 = ____
bytes1 = ____
string1 = ____
print(string1)

# FIXME SOLUTION
bytes.fromhex(b64decode(blob.encode()).decode()).decode()

# FIXME CREATION
msg = "This on is getting a bit complicated. Do not overdo the encodings.."
msg_as_bytes = msg.encode("ascii")
bytes_as_hex = msg_as_bytes.hex()
hex_as_ascii_as_bytes = bytes_as_hex.encode()
b64encode(hex_as_ascii_as_bytes).decode()

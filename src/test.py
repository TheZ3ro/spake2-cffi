from binascii import hexlify as hex
from ctypes import *

libc = CDLL(None)
libc.srand(0)

from spake2 import Spake2_Alice, Spake2_Bob

client_name = b'adb pair client'
server_name = b'adb pair server'

try:
    alice = Spake2_Alice(client_name, server_name)
    bob = Spake2_Bob(server_name, client_name)
except TypeError:
    print('Failed to create SPAKE2 context.')
    exit(-1)

k = bytes([53, 57, 50, 55, 56, 49, 230, 61, 217, 89, 101, 28, 33, 22, 0, 243, 182, 86, 29, 11, 157, 144, 175, 9, 208, 164, 164, 83, 238, 32, 89, 164, 128, 204, 124, 90, 148, 212, 212, 137, 51, 249, 255, 245, 254, 67, 49, 125, 82, 250, 123, 255, 143, 139, 196, 243, 72, 139, 128, 7, 51, 15, 236, 124, 126, 220, 145, 194, 14, 93])

amsg = alice.generate_message(k)
bmsg = bob.generate_message(k)

print(len(amsg), hex(amsg))
print(len(bmsg), hex(bmsg))

akey = alice.process_msg(bmsg)
bkey = bob.process_msg(amsg)

print(len(akey), hex(akey))
print(len(bkey), hex(bkey))

assert(akey == bkey)


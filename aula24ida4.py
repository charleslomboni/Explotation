from subprocess import *
import struct

p = Popen([r'IDA4.exe','f'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

print "Atachar o IDA e pressionar ENTER\n"
raw_input()

# < = little-endian
# L = unsigned long
# https://docs.python.org/2/library/struct.html
str1 = struct.pack("<L", 0x71725553)
str2 = struct.pack("<L", 0x1020005)
str3 = struct.pack("<L", 0x35224158)
flag = struct.pack("<L", 0x90909090)

first = 50 * "A" + str1 + str2 + flag + str3
p.stdin.write(first)

response = p.communicate()[0]
print first
print (response)
